import os
from PIL import Image

# RUTAS CONFIGURADAS
base_path = r"C:\Users\Juan\OneDrive\Escritorio\Logos"
output_folder = r"C:\Users\Juan\OneDrive\Escritorio\Logos\Optimized"

# Dimensiones objetivo extraídas del reporte de Lighthouse
targets = {
    "logo_microstrategy.webp": (132, 29), # Original: 250x54
    "logo_tableau.webp": (51, 29),       # Original: 140x78
    "logo_sql_server.webp": (36, 29),    # Original: 100x80
    "logo_power_bi.webp": (51, 29)       # Original: 140x78
}

def optimize_portfolio_logos():
    # Verificación de entorno: Crear carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Carpeta de salida inicializada: {output_folder}")

    for filename, target_size in targets.items():
        input_path = os.path.join(base_path, filename)
        output_path = os.path.join(output_folder, filename)

        if os.path.exists(input_path):
            try:
                with Image.open(input_path) as img:
                    # Uso de filtro Lanczos para preservar la nitidez de los logos
                    optimized_img = img.resize(target_size, Image.Resampling.LANCZOS)
                    
                    # Guardado optimizado en WebP
                    optimized_img.save(output_path, "WEBP", quality=90)
                    print(f"Procesado: {filename} -> {target_size[0]}x{target_size[1]}px")
            except Exception as e:
                print(f"Error técnico al procesar {filename}: {e}")
        else:
            print(f"Archivo faltante en origen: {filename}")

if __name__ == "__main__":
    print("Iniciando optimización de activos para el portfolio...")
    optimize_portfolio_logos()
    print("Proceso finalizado. Los archivos están listos en la carpeta Optimized.")