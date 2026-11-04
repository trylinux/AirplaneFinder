package org.airplanemuseum.finder

import android.content.Context
import androidx.room.*
import org.json.JSONArray
import org.json.JSONObject
import java.io.File
import java.io.FileInputStream
import java.io.InputStream

@Entity(primaryKeys = ["kind", "id"])
data class CatalogRecord(val kind: String, val id: Long, val payload: String)
@Entity
data class CatalogMeta(@PrimaryKey val id: Int = 1, val manifest: String)
@Entity
data class SavedTrip(@PrimaryKey val id: String, val payload: String)

@Dao
interface CatalogDao {
    @Query("SELECT * FROM CatalogRecord ORDER BY kind,id") fun records(): List<CatalogRecord>
    @Query("SELECT * FROM CatalogRecord WHERE kind=:kind ORDER BY id") fun recordsOfKind(kind: String): List<CatalogRecord>
    @Query("SELECT * FROM CatalogMeta WHERE id=1") fun meta(): CatalogMeta?
    @Query("DELETE FROM CatalogRecord") fun clearCatalog()
    @Insert fun insertRecords(records: List<CatalogRecord>)
    @Insert(onConflict = OnConflictStrategy.REPLACE) fun setMeta(meta: CatalogMeta)
    @Query("SELECT * FROM SavedTrip ORDER BY id DESC") fun trips(): List<SavedTrip>
    @Insert(onConflict = OnConflictStrategy.REPLACE) fun saveTrip(trip: SavedTrip)
    @Query("DELETE FROM SavedTrip WHERE id=:id") fun deleteTrip(id: String)
}

@Database(entities = [CatalogRecord::class, CatalogMeta::class, SavedTrip::class], version = 1, exportSchema = true)
abstract class CatalogDatabase : RoomDatabase() {
    abstract fun catalog(): CatalogDao
    fun replace(document: JSONObject, manifest: JSONObject) {
        val rows = SnapshotProtocol.validate(document, manifest)
        runInTransaction {
            catalog().clearCatalog()
            rows.chunked(500).forEach { catalog().insertRecords(it) }
            catalog().setMeta(CatalogMeta(manifest = manifest.toString()))
        }
    }
    fun openDocument(context: Context): InputStream {
        // Stream serialized rows rather than materializing a second object graph and
        // a giant StringBuilder. The production-sized seed exceeds small heaps otherwise.
        val file = File.createTempFile("ui-catalog-", ".json", context.cacheDir)
        try {
            runInTransaction {
                file.bufferedWriter().use { writer ->
                    writer.write("{\"meta\":")
                    writer.write(catalog().meta()?.manifest ?: "{}")
                    for (kind in SnapshotProtocol.kinds) {
                        writer.write(",\"$kind\":[")
                        catalog().recordsOfKind(kind).forEachIndexed { index, record ->
                            if (index > 0) writer.write(",")
                            writer.write(record.payload)
                        }
                        writer.write("]")
                    }
                    writer.write("}")
                }
            }
            return object : FileInputStream(file) {
                override fun close() { try { super.close() } finally { file.delete() } }
            }
        } catch (exception: Exception) { file.delete(); throw exception }
    }
    companion object {
        @Volatile private var instance: CatalogDatabase? = null
        fun get(context: Context): CatalogDatabase = instance ?: synchronized(this) {
            instance ?: Room.databaseBuilder(context.applicationContext, CatalogDatabase::class.java, "catalog.db")
                .build().also { instance = it }
        }
    }
}
