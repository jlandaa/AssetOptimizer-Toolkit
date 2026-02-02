from PIL import Image
import os

# Rutas absolutas actualizadas con el nombre de carpeta correcto (Mayúsculas)
ruta_entrada = r"C:\Users\Juan\OneDrive\Escritorio\Perfil\Juan_Manuel.webp"
ruta_salida = r"C:\Users\Juan\OneDrive\Escritorio\Perfil\Juan_Manuel_opt.webp"

try:
    # Abrir la imagen original (2.7 MB)
    with Image.open(ruta_entrada) as img:
        # Redimensionar a 400x400 para alta densidad de píxeles (Retina)
        img_redimensionada = img.resize((400, 400), Image.LANCZOS)
        
        # Guardar en formato WebP con compresión de calidad 80
        img_redimensionada.save(ruta_salida, "WEBP", quality=80)
        
        # Validación de resultados
        peso_original = os.path.getsize(ruta_entrada) / 1024
        peso_final = os.path.getsize(ruta_salida) / 1024
        
        print("--- Proceso Exitoso ---")
        print(f"Peso original: {peso_original:.2f} KB")
        print(f"Peso final: {peso_final:.2f} KB")
        print(f"Ahorro aproximado: {peso_original - peso_final:.2f} KB")

except FileNotFoundError:
    print(f"Error: No se encontró la imagen en {ruta_entrada}. Verifica el nombre del archivo.")
except Exception as e:
    print(f"Error inesperado: {e}")