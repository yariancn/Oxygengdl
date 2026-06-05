#!/bin/bash
# Comprime imágenes para web antes de subir a GitHub.
# Uso: ./compress-images.sh /ruta/a/carpeta/con/imagenes/originales

set -e
DEST="$(cd "$(dirname "$0")" && pwd)/assets/images"
SRC="${1:-.}"

mkdir -p "$DEST"

compress_one() {
  local src="$1"
  local dest="$2"
  local max_px="${3:-1600}"

  if [[ ! -f "$src" ]]; then
    echo "SKIP (no existe): $src"
    return
  fi

  mkdir -p "$(dirname "$dest")"
  sips -Z "$max_px" "$src" --out "$dest" >/dev/null 2>&1 || cp "$src" "$dest"
  echo "OK: $(basename "$dest") ($(du -h "$dest" | cut -f1))"
}

echo "Destino: $DEST"
echo "Origen:  $SRC"
echo "---"

# Ajusta estos nombres según tus archivos originales
declare -A MAP=(
  ["logo.png"]="logo.png"
  ["OXY-LOGO_Mesa-de-trabajo-1.png"]="OXY-LOGO_Mesa-de-trabajo-1.png"
  ["OXY-LOGO-02.png"]="OXY-LOGO-02.png"
  ["ibum-2.png"]="ibum-2.png"
  ["IMAGEN-CIRUGIA.jpg"]="IMAGEN-CIRUGIA.jpg"
  ["IMAGEN-PARALISIS-CEREBRAL.jpg"]="IMAGEN-PARALISIS-CEREBRAL.jpg"
  ["IMAGEN-AUTISMO.jpg"]="IMAGEN-AUTISMO.jpg"
  ["IMAGEN-CANCER.jpg"]="IMAGEN-CANCER.jpg"
  ["IMAGEN-STROKE.jpg"]="IMAGEN-STROKE.jpg"
  ["IMAGEN-DIABETES.jpg"]="IMAGEN-DIABETES.jpg"
  ["IMAGEN-MIGRANA.jpg"]="IMAGEN-MIGRANA.jpg"
  ["IMAGEN-DEPORTE.jpg"]="IMAGEN-DEPORTE.jpg"
  ["fibromialgia.jpg"]="fibromialgia.jpg"
  ["2024-07-31.jpg"]="2024-07-31.jpg"
  ["IMG-20240510-WA0014.jpg"]="IMG-20240510-WA0014.jpg"
)

for dest_name in "${!MAP[@]}"; do
  src_name="${MAP[$dest_name]}"
  compress_one "$SRC/$src_name" "$DEST/$dest_name" 1600
done

echo "---"
echo "Listo. Revisa tamaños:"
du -h "$DEST"/* 2>/dev/null | sort -rh
