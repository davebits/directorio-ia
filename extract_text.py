import os
from pdfminer.high_level import extract_text

# Nombre del archivo PDF
pdf_path = "documento_prueba.pdf"

# Extraer texto del PDF
texto_extraido = extract_text(pdf_path)

# Verificar si se extrajo texto
print("Texto extraído:")
print(texto_extraido)

# Crear ruta de salida dinámicamente
directorio_actual = os.path.dirname(os.path.abspath(__file__))  # Obtiene la carpeta del script
ruta_salida = os.path.join(directorio_actual, "texto_extraido.txt")

# Guardar el texto en un archivo .txt
with open(ruta_salida, "w", encoding="utf-8") as f:
    f.write(texto_extraido)

print(f"Archivo creado en: {ruta_salida}")
