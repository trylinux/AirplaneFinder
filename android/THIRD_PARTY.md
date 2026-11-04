# Bundled assets

Assets are included locally so airplane mode does not remove fonts, icons, or
globe rendering. No CDN requests are needed at runtime.

| Asset | Version/source | License included |
| --- | --- | --- |
| Three.js | r128, matching the website; CDN bytes verified against the website's SHA-384 integrity value | `app/src/main/assets/vendor/THREE-LICENSE.txt` (MIT) |
| Font Awesome Free | 6.5.1, matching the website; CSS verified against its SHA-384 integrity value | `app/src/main/assets/vendor/fontawesome/LICENSE.txt` (font/code/icon terms) |
| Inter variable font | Google Fonts `ofl/inter/Inter[opsz,wght].ttf` | `app/src/main/assets/vendor/Inter-OFL.txt` (OFL) |
| Museum globe and boundary GeoJSON | Existing repository `static/js` and `static/data` assets | See their source and repository attribution |

AndroidX and Kotlin dependencies are resolved by Gradle from Google/Maven Central
with versions pinned in the build files. Build outputs and downloaded dependency
caches are not committed. The Gradle wrapper and Room schema are checked in.
