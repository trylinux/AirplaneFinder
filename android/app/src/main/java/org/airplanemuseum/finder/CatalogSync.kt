package org.airplanemuseum.finder

import android.content.Context
import androidx.work.*
import org.json.JSONObject
import java.net.HttpURLConnection
import java.net.URL
import java.time.Instant
import java.util.concurrent.TimeUnit

object CatalogSync {
    const val WORK = "catalog-refresh"
    private val seedLock = Any()
    fun seed(context: Context) = synchronized(seedLock) {
        val database = CatalogDatabase.get(context)
        if (database.catalog().meta() == null) {
            val manifest = context.assets.open("seed/manifest.json").bufferedReader().use { JSONObject(it.readText()) }
            // AAPT transparently expands assets ending in .gz; retain exact checksum bytes.
            val packed = context.assets.open("seed/catalog.snapshot").use { SnapshotProtocol.readLimited(it, SnapshotProtocol.MAX_PACKED) }
            database.replace(SnapshotProtocol.decode(packed, manifest), manifest)
        }
    }
    fun enqueue(context: Context, manual: Boolean = false) {
        val work = OneTimeWorkRequestBuilder<CatalogWorker>()
            .setConstraints(Constraints.Builder().setRequiredNetworkType(NetworkType.CONNECTED).build())
            .setBackoffCriteria(BackoffPolicy.EXPONENTIAL, 30, TimeUnit.SECONDS).build()
        WorkManager.getInstance(context).enqueueUniqueWork(WORK, if (manual) ExistingWorkPolicy.REPLACE else ExistingWorkPolicy.KEEP, work)
    }
    fun schedule(context: Context) {
        val work = PeriodicWorkRequestBuilder<CatalogWorker>(12, TimeUnit.HOURS)
            .setConstraints(Constraints.Builder().setRequiredNetworkType(NetworkType.CONNECTED).build()).build()
        WorkManager.getInstance(context).enqueueUniquePeriodicWork("catalog-periodic", ExistingPeriodicWorkPolicy.KEEP, work)
    }
    fun status(context: Context): JSONObject {
        val settings = context.getSharedPreferences("sync", Context.MODE_PRIVATE)
        val result = CatalogDatabase.get(context).catalog().meta()?.let { JSONObject(it.manifest) } ?: JSONObject()
        result.put("last_checked", settings.getString("last_checked", null))
        result.put("error", settings.getString("error", null))
        val works = WorkManager.getInstance(context).getWorkInfosForUniqueWork(WORK).get() +
            WorkManager.getInstance(context).getWorkInfosForUniqueWork("catalog-periodic").get()
        result.put("running", works.any { it.state == WorkInfo.State.RUNNING })
        result.put("queued", works.any { it.state == WorkInfo.State.ENQUEUED && it.tags.contains(CatalogWorker::class.java.name) })
        return result
    }
    private fun download(path: String, maximum: Int): ByteArray {
        val connection = URL(BuildConfig.CATALOG_BASE_URL + path).openConnection() as HttpURLConnection
        connection.connectTimeout = 15000
        connection.readTimeout = 30000
        connection.instanceFollowRedirects = false
        connection.setRequestProperty("User-Agent", "AircraftFinder-Android/${BuildConfig.VERSION_NAME}")
        connection.setRequestProperty("Accept-Encoding", "identity")
        try {
            check(connection.responseCode == 200) {
                when (connection.responseCode) {
                    404, 503 -> "The website has not published an offline catalog yet. Your saved catalog is available."
                    429 -> "The update service is busy. Android will retry later."
                    else -> "Catalog service returned HTTP ${connection.responseCode}. Your saved catalog is available."
                }
            }
            return connection.inputStream.use { SnapshotProtocol.readLimited(it, maximum) }
        } finally { connection.disconnect() }
    }
    fun refresh(context: Context) = synchronized(seedLock) {
        seed(context)
        val manifest = JSONObject(String(download("/api/v1/offline/manifest", 64 * 1024), Charsets.UTF_8))
        require(manifest.getInt("schema_version") == 1) { "Update the app to read this catalog version." }
        val revision = manifest.getString("revision")
        require(revision.matches(Regex("[0-9a-f]{64}")))
        val path = "/api/v1/offline/snapshots/$revision.json.gz"
        require(manifest.getString("download_path") == path) { "Invalid catalog download location." }
        val database = CatalogDatabase.get(context)
        val old = database.catalog().meta()?.let { JSONObject(it.manifest) }
        if (revision != old?.optString("revision")) {
            val bytes = download(path, SnapshotProtocol.MAX_PACKED)
            database.replace(SnapshotProtocol.decode(bytes, manifest), manifest)
        }
        context.getSharedPreferences("sync", Context.MODE_PRIVATE).edit()
            .putString("last_checked", Instant.now().toString()).remove("error").apply()
    }
}

class CatalogWorker(context: Context, parameters: WorkerParameters) : Worker(context, parameters) {
    override fun doWork(): Result = try {
        CatalogSync.refresh(applicationContext)
        Result.success()
    } catch (exception: Exception) {
        applicationContext.getSharedPreferences("sync", Context.MODE_PRIVATE).edit()
            .putString("error", exception.message?.take(200) ?: "Update failed; previous catalog retained.").apply()
        // Periodic work supplies future attempts; cap retries of an explicit refresh.
        if (runAttemptCount < 3) Result.retry() else Result.failure()
    }
}
