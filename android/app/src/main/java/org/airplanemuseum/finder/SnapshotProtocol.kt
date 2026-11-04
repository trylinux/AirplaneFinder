package org.airplanemuseum.finder

import org.json.JSONObject
import java.io.InputStream
import java.security.MessageDigest
import java.util.zip.GZIPInputStream

object SnapshotProtocol {
    val kinds = listOf("aircraft", "museums", "exhibits", "types", "facts", "history")
    const val MAX_PACKED = 16 * 1024 * 1024
    const val MAX_RAW = 64 * 1024 * 1024
    fun readLimited(stream: InputStream, maximum: Int): ByteArray {
        val output = java.io.ByteArrayOutputStream()
        val buffer = ByteArray(16384)
        while (true) {
            val n = stream.read(buffer)
            if (n < 0) break
            require(output.size() + n <= maximum) { "Download exceeds the supported size." }
            output.write(buffer, 0, n)
        }
        return output.toByteArray()
    }
    fun decode(bytes: ByteArray, manifest: JSONObject): JSONObject {
        require(manifest.getInt("schema_version") == 1) { "Update the app to read this catalog version." }
        require(bytes.size == manifest.getInt("byte_size")) { "Incomplete download; previous catalog retained." }
        val hash = MessageDigest.getInstance("SHA-256").digest(bytes).joinToString("") { "%02x".format(it) }
        require(hash == manifest.getString("sha256") && hash == manifest.getString("revision")) { "Catalog checksum mismatch." }
        val raw = GZIPInputStream(bytes.inputStream()).use { readLimited(it, MAX_RAW) }
        require(raw.size == manifest.getInt("uncompressed_size")) { "Catalog size mismatch." }
        return JSONObject(String(raw, Charsets.UTF_8))
    }
    private fun id(row: JSONObject, field: String = "id"): Long {
        val value = row.get(field)
        require(value is Int || value is Long) { "Invalid record ID." }
        return (value as Number).toLong().also { require(it > 0 && it <= Int.MAX_VALUE) }
    }
    fun validate(document: JSONObject, manifest: JSONObject): List<CatalogRecord> {
        require(document.getInt("schema_version") == 1 && manifest.getInt("schema_version") == 1)
        for (key in listOf("catalog_id", "generated_at", "source")) require(document.getString(key) == manifest.getString(key))
        require(document.keys().asSequence().toSet() == (kinds + listOf("schema_version", "catalog_id", "generated_at", "source")).toSet())
        val identities = mutableMapOf<String, Set<Long>>()
        val records = mutableListOf<CatalogRecord>()
        for (kind in kinds) {
            val array = document.getJSONArray(kind)
            require(array.length() == manifest.getJSONObject("counts").getInt(kind))
            require(array.length() <= 200000)
            val ids = mutableSetOf<Long>()
            for (index in 0 until array.length()) {
                val row = array.getJSONObject(index)
                val recordId = id(row)
                require(ids.add(recordId)) { "Duplicate catalog ID." }
                if (kind in listOf("types", "history")) require(row.opt("is_published") == true) { "Unpublished data rejected." }
                if (kind == "facts") require(row.opt("is_active") != false)
                val required = when (kind) {
                    "aircraft" -> listOf("manufacturer", "model")
                    "museums" -> listOf("name", "country")
                    "facts" -> listOf("fact")
                    "history" -> listOf("title")
                    "types" -> listOf("display_name", "description")
                    else -> emptyList()
                }
                required.forEach { require(row.opt(it) is String) { "Invalid text field." } }
                records.add(CatalogRecord(kind, recordId, row.toString()))
            }
            identities[kind] = ids
        }
        for (record in records) {
            val row = JSONObject(record.payload)
            fun reference(field: String, kind: String) {
                if (row.has(field) && !row.isNull(field)) require(id(row, field) in identities.getValue(kind)) { "Broken catalog relationship." }
            }
            if (record.kind == "exhibits") {
                require(row.has("aircraft_id") && row.has("museum_id"))
                reference("aircraft_id", "aircraft"); reference("museum_id", "museums")
            }
            if (record.kind == "history") require(row.has("aircraft_id") && !row.isNull("aircraft_id"))
            if (record.kind in listOf("history", "facts")) reference("aircraft_id", "aircraft")
            if (record.kind == "aircraft") reference("type_id", "types")
        }
        return records
    }
}
