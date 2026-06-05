#!/bin/bash
# Comprime imágenes para web (compatible con Bash 3.2 de macOS).
# Uso: ./compress-images.sh /ruta/a/carpeta/con/imagenes

set -e
DEST="$(cd "$(dirname "$0")" && pwd)/assets/images"
SRC="${1:-.}"

if [[ ! -d "$SRC" ]]; then
  echo "ERROR: La carpeta no existe: $SRC"
  echo "Uso: ./compress-images.sh /ruta/a/tus/imagenes"
  exit 1
fi

mkdir -p "$DEST"

compress_one() {
  local src_name="$1"
  local dest_name="$2"
  local max_px="${3:-1600}"
  local src="$SRC/$src_name"
  local dest="$DEST/$dest_name"

  if [[ ! -f "$src" ]]; then
    echo "SKIP (no existe): $src_name"
    return 0
  fi

  sips -Z "$max_px" "$src" --out "$dest" >/dev/null 2>&1 || cp "$src" "$dest"
  echo "OK: $dest_name ($(du -h "$dest" | awk '{print $1}'))"
}

echo "Destino: $DEST"
echo "Origen:  $SRC"
echo "---"

compress_one "logo.png"                         "logo.png"                         400
compress_one "OXY-LOGO_Mesa-de-trabajo-1.png"   "OXY-LOGO_Mesa-de-trabajo-1.png"   400
compress_one "OXY-LOGO-02.png"                  "OXY-LOGO-02.png"                  800
compress_one "ibum-2.png"                       "ibum-2.png"                       400
compress_one "IMAGEN-CIRUGIA.jpg"               "IMAGEN-CIRUGIA.jpg"               1600
compress_one "IMAGEN-PARALISIS-CEREBRAL.jpg"   "IMAGEN-PARALISIS-CEREBRAL.jpg"   1600
compress_one "IMAGEN-AUTISMO.jpg"               "IMAGEN-AUTISMO.jpg"               1600
compress_one "IMAGEN-CANCER.jpg"                "IMAGEN-CANCER.jpg"                1600
compress_one "IMAGEN-STROKE.jpg"                "IMAGEN-STROKE.jpg"                1600
compress_one "IMAGEN-DIABETES.jpg"              "IMAGEN-DIABETES.jpg"              1600
compress_one "IMAGEN-MIGRANA.jpg"               "IMAGEN-MIGRANA.jpg"               1600
compress_one "IMAGEN-DEPORTE.jpg"               "IMAGEN-DEPORTE.jpg"               1600
compress_one "fibromialgia.jpg"                 "fibromialgia.jpg"                 1600
compress_one "2024-07-31.jpg"                   "2024-07-31.jpg"                   1600
compress_one "IMG-20240510-WA0014.jpg"            "IMG-20240510-WA0014.jpg"          1600

echo "---"
echo "Listo. Archivos en assets/images:"
du -h "$DEST"/* 2>/dev/null | sort -rh
