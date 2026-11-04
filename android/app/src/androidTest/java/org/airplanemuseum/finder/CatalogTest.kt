package org.airplanemuseum.finder

import androidx.room.Room
import androidx.test.core.app.ApplicationProvider
import androidx.test.ext.junit.runners.AndroidJUnit4
import org.json.JSONArray
import org.json.JSONObject
import org.junit.Assert.*
import org.junit.Test
import org.junit.runner.RunWith
import java.security.MessageDigest
import java.util.zip.GZIPOutputStream

@RunWith(AndroidJUnit4::class)
class CatalogTest {
    @Test fun bundledSeedIsCompleteAndValid() {
        val context = ApplicationProvider.getApplicationContext<android.content.Context>()
        val metadata = context.assets.open("seed/manifest.json").bufferedReader().use { JSONObject(it.readText()) }
        val bytes = context.assets.open("seed/catalog.snapshot").use { SnapshotProtocol.readLimited(it, SnapshotProtocol.MAX_PACKED) }
        val records = SnapshotProtocol.validate(SnapshotProtocol.decode(bytes, metadata), metadata)
        assertTrue(records.isNotEmpty())
    }
    private fun document(): JSONObject {
        val data = JSONObject().put("schema_version", 1).put("catalog_id", "test")
            .put("generated_at", "2026-11-04T00:00:00Z").put("source", "Test fixture")
        SnapshotProtocol.kinds.forEach { data.put(it, JSONArray()) }
        data.getJSONArray("aircraft").put(JSONObject().put("id", 1).put("manufacturer", "Test").put("model", "X"))
        data.getJSONArray("museums").put(JSONObject().put("id", 1).put("name", "Museum").put("country", "US"))
        data.getJSONArray("exhibits").put(JSONObject().put("id", 1).put("aircraft_id", 1).put("museum_id", 1))
        return data
    }
    private fun manifest(data: JSONObject): JSONObject {
        val result = JSONObject()
        for (field in listOf("schema_version", "catalog_id", "generated_at", "source")) result.put(field, data.get(field))
        return result.put("counts", JSONObject().also { counts -> SnapshotProtocol.kinds.forEach { counts.put(it, data.getJSONArray(it).length()) } })
    }
    private fun rejects(block: () -> Unit) {
        try { block(); fail("Invalid snapshot accepted") } catch (_: IllegalArgumentException) {}
    }
    @Test fun replacementIsAtomicAndPreservesTrips() {
        val database = Room.inMemoryDatabaseBuilder(ApplicationProvider.getApplicationContext(), CatalogDatabase::class.java).build()
        try {
            val data = document()
            database.replace(data, manifest(data))
            val streamed = database.openDocument(ApplicationProvider.getApplicationContext()).bufferedReader().use { JSONObject(it.readText()) }
            assertEquals(1, streamed.getJSONArray("aircraft").length())
            assertEquals("test", streamed.getJSONObject("meta").getString("catalog_id"))
            database.catalog().saveTrip(SavedTrip("trip1", "{\"name\":\"My trip\"}"))
            val invalid = document()
            invalid.getJSONArray("exhibits").getJSONObject(0).put("aircraft_id", 999)
            rejects { database.replace(invalid, manifest(invalid)) }
            assertEquals(3, database.catalog().records().size)
            val empty = document()
            SnapshotProtocol.kinds.forEach { empty.put(it, JSONArray()) }
            database.replace(empty, manifest(empty))
            assertEquals(0, database.catalog().records().size)
            assertEquals("trip1", database.catalog().trips().single().id)
        } finally { database.close() }
    }
    @Test fun corruptDownloadsNeverDecode() {
        val data = document(); val manifest = manifest(data)
        val raw = data.toString().toByteArray()
        val output = java.io.ByteArrayOutputStream()
        GZIPOutputStream(output).use { it.write(raw) }
        val packed = output.toByteArray()
        val hash = MessageDigest.getInstance("SHA-256").digest(packed).joinToString("") { "%02x".format(it) }
        manifest.put("sha256", hash).put("revision", hash).put("byte_size", packed.size).put("uncompressed_size", raw.size)
        assertEquals("test", SnapshotProtocol.decode(packed, manifest).getString("catalog_id"))
        packed[0] = 0
        rejects { SnapshotProtocol.decode(packed, manifest) }
    }
    @Test fun duplicatesDraftsAndPrivateCollectionsAreRejected() {
        val duplicate = document()
        duplicate.getJSONArray("aircraft").put(duplicate.getJSONArray("aircraft").getJSONObject(0))
        rejects { SnapshotProtocol.validate(duplicate, manifest(duplicate)) }
        val private = document().put("users", JSONArray())
        rejects { SnapshotProtocol.validate(private, manifest(private)) }
        val draft = document()
        draft.getJSONArray("history").put(JSONObject().put("id", 1).put("aircraft_id", 1).put("title", "Draft").put("is_published", false))
        rejects { SnapshotProtocol.validate(draft, manifest(draft)) }
    }
}
