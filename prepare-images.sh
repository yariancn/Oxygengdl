#!/bin/bash
# Prepara y comprime todas las imágenes del sitio OXYGENGDL.
# Compatible con Bash 3.2 (macOS).

set -e
DEST="$(cd "$(dirname "$0")" && pwd)/assets/images"
HBOT="/Users/yariancuenca/Documents/HBOT"
DL="/Users/yariancuenca/Downloads"

mkdir -p "$DEST"

compress() {
  local src="$1"
  local dest="$2"
  local max_px="${3:-1600}"

  if [[ ! -f "$src" ]]; then
    echo "SKIP (no existe): $src"
    return 0
  fi

  sips -Z "$max_px" "$src" --out "$dest" >/dev/null 2>&1 || cp "$src" "$dest"
  echo "OK: $(basename "$dest") <- $(basename "$src") ($(du -h "$dest" | awk '{print $1}'))"
}

echo "Preparando imágenes en: $DEST"
echo "---"

# Logos
compress "$DL/OXY LOGO_Mesa de trabajo 1.png"  "$DEST/OXY-LOGO_Mesa-de-trabajo-1.png" 400
compress "$DL/OXY LOGO-02.png"                   "$DEST/OXY-LOGO-02.png"                  800
compress "$HBOT/logo.png"                        "$DEST/logo.png"                         400
compress "$DL/ibum-2.png"                        "$DEST/ibum-2.png"                       400

# Tratamientos (originales en HBOT, nombres con espacios)
compress "$HBOT/IMAGEN CIRUGIA PLASTICA.jpg"     "$DEST/IMAGEN-CIRUGIA.jpg"              1200
compress "$HBOT/IMAGEN PARALISIS CEREBRAL.jpg"  "$DEST/IMAGEN-PARALISIS-CEREBRAL.jpg"   1200
compress "$HBOT/IMAGEN AUTISMO.jpg"              "$DEST/IMAGEN-AUTISMO.jpg"              1200
compress "$HBOT/IMAGEN CANCER.jpg"               "$DEST/IMAGEN-CANCER.jpg"               1200
compress "$HBOT/IMAGEN STROKE.jpg"               "$DEST/IMAGEN-STROKE.jpg"               1200
compress "$HBOT/IMAGEN DIABETES.jpg"             "$DEST/IMAGEN-DIABETES.jpg"             1200
compress "$HBOT/IMAGEN NEUROLOGIA.jpg"           "$DEST/IMAGEN-MIGRANA.jpg"              1200
compress "$HBOT/IMAGEN DEPORTE.jpg"              "$DEST/IMAGEN-DEPORTE.jpg"              1200
compress "$HBOT/fibromialgia.jpg"                "$DEST/fibromialgia.jpg"                1200

# Instalaciones
compress "$DL/2024-07-31.jpg"                  "$DEST/2024-07-31.jpg"                  1200
compress "$HBOT/IMG-20240510-WA0014.jpg"         "$DEST/IMG-20240510-WA0014.jpg"         1200

echo "---"
echo "Resumen final:"
du -h "$DEST"/* 2>/dev/null | sort -rh
echo "---"
TOTAL=$(du -sh "$DEST" | awk '{print $1}')
echo "Total carpeta imágenes: $TOTAL"
