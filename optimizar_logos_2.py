import os
from PIL import Image

# Mapeo de imagen -> Ancho objetivo optimizado (Display Width * 1.2)
# Esto satisface a Lighthouse sin sacrificar nitidez en pantallas normales
target_specs = {
    # Logos de Habilidades y Certificaciones (Ajuste Quirúrgico)
    "logo_alation.webp": 172,        # 143px * 1.2
    "logo_datarobot.webp": 174,      # 145px * 1.2
    "logo_looker.webp": 116,         # 97px * 1.2
    "logo_azure_cognitive_services.webp": 53, # 44px * 1.2
    "logo_microstrategy2.webp": 80, 
    "logo_sql_server.webp": 100,
    
    # Otros Recursos (Ajuste Quirúrgico)
    "Logo_We_Plan.webp": 198, # 165px * 1.2
    "UADE.webp": 82,              # 68px * 1.2
    "Juan_Manuel.webp": 384
}

# RUTAS EXACTAS
img_folder = r"C:\Users\Juan\OneDrive\Escritorio\Imagenes"
output_folder = r"C:\Users\Juan\OneDrive\Escritorio\Imagenes\Optimized"

def optimizar_quirurgico():
    print(f"--- Iniciando optimización ultra-fina ---")
    ahorro_total_kb = 0
    encontradas = 0

    for rel_path, target_width in target_specs.items():
        file_path = os.path.join(img_folder, rel_path.replace("/", os.sep))
        
        if os.path.exists(file_path):
            try:
                encontradas += 1
                with Image.open(file_path) as img:
                    width_percent = (target_width / float(img.size[0]))
                    target_height = int((float(img.size[1]) * float(width_percent)))
                    
                    img_resized = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                    
                    out_file_path = os.path.join(output_folder, rel_path.replace("/", os.sep))
                    os.makedirs(os.path.dirname(out_file_path), exist_ok=True)
                    
                    # CAMBIO CLAVE: Calidad a 60 y método de compresión máximo (6)
                    img_resized.save(out_file_path, "WEBP", quality=60, method=6)
                    
                    size_old = os.path.getsize(file_path) / 1024
                    size_new = os.path.getsize(out_file_path) / 1024
                    ahorro_total_kb += (size_old - size_new)
                    
                    print(f"✅ {rel_path}: {size_old:.1f}KB -> {size_new:.1f}KB")
            
            except Exception as e:
                print(f"❌ Error en {rel_path}: {e}")
        else:
            print(f"⚠️ No encontrada: {rel_path}")

    print(f"\n--- Resumen Final ---")
    print(f"Ahorro extra logrado: {ahorro_total_kb:.1f} KB")
    print(f"Archivos listos en: {output_folder}")

if __name__ == "__main__":
    optimizar_quirurgico()