package org.airplanemuseum.finder

import android.Manifest
import android.content.Intent
import android.content.pm.PackageManager
import android.graphics.Color
import android.location.Location
import android.location.LocationListener
import android.location.LocationManager
import android.net.Uri
import android.os.Bundle
import android.os.Build
import android.os.Handler
import android.os.Looper
import android.webkit.*
import android.widget.TextView
import android.widget.FrameLayout
import androidx.webkit.*
import androidx.activity.ComponentActivity
import androidx.activity.OnBackPressedCallback
import androidx.activity.result.contract.ActivityResultContracts
import org.json.JSONArray
import org.json.JSONObject
import java.util.UUID
import java.util.concurrent.Executors

class MainActivity : ComponentActivity() {
    private lateinit var web: WebView
    private val io = Executors.newSingleThreadExecutor()
    private val main = Handler(Looper.getMainLooper())
    private var locationReply: ((JSONObject) -> Unit)? = null
    private var locationListener: LocationListener? = null
    private var lastRefresh = 0L
    private val origin = "https://appassets.androidplatform.net"
    private val locationPermissions = registerForActivityResult(ActivityResultContracts.RequestMultiplePermissions()) { granted ->
        if (granted[Manifest.permission.ACCESS_COARSE_LOCATION] == true) locate()
        else {
            locationReply?.invoke(JSONObject().put("error", "Location permission denied. You can enter coordinates instead."))
            locationReply = null
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        window.decorView.setBackgroundColor(Color.rgb(15, 23, 42))
        web = WebView(this)
        web.setBackgroundColor(Color.rgb(15, 23, 42))
        val frame = FrameLayout(this)
        frame.addView(web, FrameLayout.LayoutParams(FrameLayout.LayoutParams.MATCH_PARENT, FrameLayout.LayoutParams.MATCH_PARENT))
        frame.setOnApplyWindowInsetsListener { view, insets ->
            if (Build.VERSION.SDK_INT >= 30) {
                val bars = insets.getInsets(android.view.WindowInsets.Type.systemBars() or android.view.WindowInsets.Type.displayCutout() or android.view.WindowInsets.Type.ime())
                view.setPadding(bars.left, bars.top, bars.right, bars.bottom)
            } else {
                @Suppress("DEPRECATION")
                view.setPadding(insets.systemWindowInsetLeft, insets.systemWindowInsetTop,
                    insets.systemWindowInsetRight, insets.systemWindowInsetBottom)
            }
            insets
        }
        setContentView(frame)
        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                if (web.canGoBack()) web.goBack() else finish()
            }
        })
        web.settings.javaScriptEnabled = true
        web.settings.domStorageEnabled = true
        web.settings.allowFileAccess = false
        web.settings.allowContentAccess = false
        web.settings.mixedContentMode = WebSettings.MIXED_CONTENT_NEVER_ALLOW
        WebView.setWebContentsDebuggingEnabled(BuildConfig.DEBUG)
        val loader = WebViewAssetLoader.Builder()
            .addPathHandler("/assets/", WebViewAssetLoader.AssetsPathHandler(this))
            .addPathHandler("/static/", WebViewAssetLoader.PathHandler { path ->
                try {
                    val mime = when { path.endsWith(".css") -> "text/css"; path.endsWith(".js") -> "application/javascript"; else -> "application/json" }
                    WebResourceResponse(mime, "UTF-8", assets.open("static/$path"))
                } catch (_: Exception) { null }
            }).build()
        web.webViewClient = object : WebViewClientCompat() {
            override fun shouldInterceptRequest(view: WebView, request: WebResourceRequest): WebResourceResponse? {
                val uri = request.url
                if (uri.scheme != "https" || uri.host != "appassets.androidplatform.net") return blocked()
                if (request.method != "GET") return blocked()
                if (uri.path == "/api/catalog") return try {
                    CatalogSync.seed(this@MainActivity)
                    WebResourceResponse("application/json", "UTF-8", 200, "OK", mapOf("Cache-Control" to "no-store"),
                        CatalogDatabase.get(this@MainActivity).openDocument(this@MainActivity))
                } catch (exception: Exception) {
                    if (BuildConfig.DEBUG) android.util.Log.e("AircraftFinder", "Local catalog read failed", exception)
                    WebResourceResponse("application/json", "UTF-8", 500, "Error", emptyMap(), "{\"error\":\"Could not read catalog\"}".byteInputStream())
                }
                if (uri.path == "/api/v1/museums/globe") return jsonResponse {
                    CatalogSync.seed(this@MainActivity)
                    val dao = CatalogDatabase.get(this@MainActivity).catalog()
                    val counts = mutableMapOf<Long, Int>()
                    for (record in dao.recordsOfKind("exhibits")) {
                        val e = JSONObject(record.payload)
                        if (e.optString("display_status") == "on_display") counts[e.getLong("museum_id")] = (counts[e.getLong("museum_id")] ?: 0) + 1
                    }
                    val result = JSONArray()
                    for (record in dao.recordsOfKind("museums")) {
                        val m = JSONObject(record.payload)
                        if (!m.isNull("latitude") && !m.isNull("longitude")) result.put(m.put("aircraft_count", counts[m.getLong("id")] ?: 0))
                    }
                    result
                }
                return loader.shouldInterceptRequest(uri) ?: blocked()
            }
            override fun shouldOverrideUrlLoading(view: WebView, request: WebResourceRequest): Boolean {
                if (request.url.toString().startsWith("$origin/assets/index.html")) return false
                if (request.isForMainFrame) openExternal(request.url.toString())
                return true
            }
        }
        if (!WebViewFeature.isFeatureSupported(WebViewFeature.WEB_MESSAGE_LISTENER)) {
            setContentView(TextView(this).apply { setText(R.string.update_webview) })
            return
        }
        if (WebViewFeature.isFeatureSupported(WebViewFeature.WEB_MESSAGE_LISTENER)) WebViewCompat.addWebMessageListener(web, "AircraftNative", setOf(origin)) { _, message, source, mainFrame, reply ->
            if (!mainFrame || source.toString().trimEnd('/') != origin) return@addWebMessageListener
            val raw = message.data ?: return@addWebMessageListener
            if (raw.length > 256000) return@addWebMessageListener
            val request = try { JSONObject(raw) } catch (_: Exception) { return@addWebMessageListener }
            val requestId = request.optString("id").take(80)
            fun respond(result: JSONObject) { main.post {
                if (WebViewFeature.isFeatureSupported(WebViewFeature.WEB_MESSAGE_LISTENER))
                    reply.postMessage(JSONObject().put("id", requestId).put("result", result).toString())
            } }
            when (request.optString("action")) {
                "location" -> { locationReply?.invoke(JSONObject().put("error", "A new location request replaced this one.")); locationReply = ::respond; locate() }
                "openUrl" -> { openExternal(request.optString("url")); respond(JSONObject().put("ok", true)) }
                else -> io.execute {
                    try {
                        CatalogSync.seed(this)
                        val dao = CatalogDatabase.get(this).catalog()
                        val result = when (request.optString("action")) {
                            "status" -> CatalogSync.status(this)
                            "sync" -> { CatalogSync.enqueue(this, manual = true); JSONObject().put("ok", true) }
                            "trips" -> JSONObject().put("trips", JSONArray(dao.trips().map { JSONObject(it.payload) }))
                            "saveTrip" -> {
                                val payload = request.getJSONObject("trip")
                                require(payload.getString("name").trim().length in 1..100)
                                require(payload.getJSONArray("stops").length() in 1..8)
                                require(payload.toString().length <= 200000)
                                require(dao.trips().size < 100) { "Remove a saved trip before adding another." }
                                val id = UUID.randomUUID().toString()
                                payload.put("id", id)
                                dao.saveTrip(SavedTrip(id, payload.toString()))
                                JSONObject().put("ok", true)
                            }
                            "deleteTrip" -> { dao.deleteTrip(request.getString("tripId")); JSONObject().put("ok", true) }
                            else -> error("Unsupported operation.")
                        }
                        respond(result)
                    } catch (exception: Exception) { respond(JSONObject().put("error", exception.message ?: "Operation failed.")) }
                }
            }
        }
        web.loadUrl("$origin/assets/index.html")
        CatalogSync.schedule(this)
    }
    private fun blocked() = WebResourceResponse("text/plain", "UTF-8", 403, "Forbidden", emptyMap(), "Unavailable".byteInputStream())
    private fun jsonResponse(load: () -> Any): WebResourceResponse = try {
        WebResourceResponse("application/json", "UTF-8", 200, "OK", mapOf("Cache-Control" to "no-store"), load().toString().byteInputStream())
    } catch (exception: Exception) {
        if (BuildConfig.DEBUG) android.util.Log.e("AircraftFinder", "Local catalog could not be opened", exception)
        WebResourceResponse("application/json", "UTF-8", 500, "Error", emptyMap(), "{\"error\":\"Local catalog could not be opened.\"}".byteInputStream())
    }
    private fun openExternal(value: String) {
        val uri = Uri.parse(value)
        if (uri.scheme !in listOf("https", "http") || uri.host.isNullOrBlank() || uri.userInfo != null) return
        try { startActivity(Intent(Intent.ACTION_VIEW, uri).addCategory(Intent.CATEGORY_BROWSABLE)) }
        catch (_: Exception) { android.widget.Toast.makeText(this, "No browser is installed.", android.widget.Toast.LENGTH_SHORT).show() }
    }
    private fun locate() {
        if (checkSelfPermission(Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            locationPermissions.launch(arrayOf(Manifest.permission.ACCESS_COARSE_LOCATION, Manifest.permission.ACCESS_FINE_LOCATION))
            return
        }
        val manager = getSystemService(LOCATION_SERVICE) as LocationManager
        locationListener?.let { manager.removeUpdates(it) }
        fun finish(location: Location?, error: String? = null) {
            locationListener?.let { manager.removeUpdates(it) }
            locationListener = null
            val result = if (location != null) JSONObject().put("latitude", location.latitude).put("longitude", location.longitude)
                .put("accuracy_m", location.accuracy) else JSONObject().put("error", error ?: "Location unavailable. Select a museum as your starting point.")
            locationReply?.invoke(result); locationReply = null
        }
        val listener = object : LocationListener {
            override fun onLocationChanged(location: Location) { finish(location) }
            override fun onProviderEnabled(provider: String) {}
            override fun onProviderDisabled(provider: String) {}
            @Deprecated("Legacy callback") override fun onStatusChanged(provider: String?, status: Int, extras: Bundle?) {}
        }
        locationListener = listener
        val providers = listOf(LocationManager.GPS_PROVIDER, LocationManager.NETWORK_PROVIDER).filter { manager.isProviderEnabled(it) }
        if (providers.isEmpty()) { finish(null); return }
        try {
            providers.forEach { manager.requestLocationUpdates(it, 1000L, 0f, listener, Looper.getMainLooper()) }
            main.postDelayed({ if (locationListener === listener) finish(null, "Location timed out. Choose a starting museum or coordinates.") }, 20000)
        } catch (_: SecurityException) { finish(null, "Location permission is required for Near Me.") }
    }
    override fun onResume() {
        super.onResume()
        if (System.currentTimeMillis() - lastRefresh > 15 * 60 * 1000) { CatalogSync.enqueue(this); lastRefresh = System.currentTimeMillis() }
    }
    override fun onDestroy() {
        locationListener?.let { (getSystemService(LOCATION_SERVICE) as LocationManager).removeUpdates(it) }
        locationReply = null
        web.destroy(); io.shutdown(); super.onDestroy()
    }
}
