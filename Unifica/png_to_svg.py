import base64
from pathlib import Path

# Leer el archivo PNG
png_path = Path('../imagenes/800px-Exert-large.png')

with open(png_path, 'rb') as f:
    png_data = f.read()

# Convertir a base64
png_base64 = base64.b64encode(png_data).decode('utf-8')

# Obtener dimensiones originales (opcional, requiere PIL)
try:
    from PIL import Image
    img = Image.open(png_path)
    width, height = img.size
    print(f"Dimensiones originales: {width}x{height}px")
except ImportError:
    # Valores por defecto si no hay PIL
    width, height = 800, 800
    print("PIL no disponible, usando dimensiones por defecto")

# Dimensiones deseadas para el SVG (puedes cambiarlas)
svg_width = 64  # píxeles
svg_height = 64  # píxeles

# O usar un porcentaje del original
# svg_width = width // 4
# svg_height = height // 4

# Crear SVG con PNG embebido
svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" 
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{svg_width}" 
     height="{svg_height}" 
     viewBox="0 0 {svg_width} {svg_height}">
  <image 
    width="{svg_width}" 
    height="{svg_height}" 
    xlink:href="data:image/png;base64,{png_base64}"
  />
</svg>'''

# Guardar SVG
svg_path = Path('../imagenes/exert.svg')
with open(svg_path, 'w', encoding='utf-8') as f:
    f.write(svg_content)

print(f"✓ SVG creado: {svg_path}")
print(f"✓ Dimensiones del SVG: {svg_width}x{svg_height}px")
print(f"\nPara cambiar las dimensiones, edita las variables svg_width y svg_height en el script")
