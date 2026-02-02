import os
from PIL import Image

# Configuración de los logos y sus anchos objetivos
target_widths = {
    "logo_copo_nieve.webp": 140,
    "logo_esquema_estrella.webp": 140,
    "logo_redshift.webp": 140,
    "logo_r.webp": 140,
    "logo_microstrategy.webp": 250,
    "logo_looker.webp": 200,
    "logo_alation.webp": 250,
    "logo_azure_cognitive_services.webp": 140,
    "logo_datarobot.webp": 250,
    "logo_airflow.webp": 140,
    "logo_sql_server.webp": 140,
    "logo_tableau.webp": 140,
    "logo_scrum.webp": 140,
    "logo_python.webp": 140,
    "logo_informatica.webp": 140,
    "logo_soda.webp": 140,
    "logo_power_bi.webp": 140,
    "logo_ssis.webp": 200,
}

# RUTAS CON PREFIJO 'r' PARA EVITAR ERRORES EN WINDOWS
img_folder = r"C:\Users\Juan\OneDrive\Escritorio\Logos"
output_folder = r"C:\Users\Juan\OneDrive\Escritorio\Logos\Optimized"

# Crear la carpeta de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def optimizar_logos():
    print(f"--- Iniciando proceso de optimización en {img_folder} ---")
    ahorro_total_kb = 0
    
    for filename, target_width in target_widths.items():
        file_path = os.path.join(img_folder, filename)
        
        if os.path.exists(file_path):
            try:
                with Image.open(file_path) as img:
                    width_percent = (target_width / float(img.size[0]))
                    target_height = int((float(img.size[1]) * float(width_percent)))
                    img_resized = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                    
                    output_path = os.path.join(output_folder, filename)
                    img_resized.save(output_path, "WEBP", quality=80, method=6)
                    
                    size_old = os.path.getsize(file_path) / 1024
                    size_new = os.path.getsize(output_path) / 1024
                    ahorro_total_kb += (size_old - size_new)
                    
                    print(f"✅ {filename}: {size_old:.1f}KB -> {size_new:.1f}KB ({((1 - size_new/size_old)*100):.1f}% menos)")
            
            except Exception as e:
                print(f"❌ Error procesando {filename}: {e}")
        else:
            print(f"⚠️ No se encontró: {filename}")

    print(f"\n--- Optimización terminada ---")
    print(f"Ahorro total estimado: {ahorro_total_kb:.1f} KB")
    print(f"Archivos listos en: {output_folder}")

if __name__ == "__main__":
    optimizar_logos()