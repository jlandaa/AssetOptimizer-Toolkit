import os
from PIL import Image

def convert_png_to_webp_with_analytics(source_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Carpeta creada: {output_dir}")

    # Filtrar archivos .png
    files = [f for f in os.listdir(source_dir) if f.lower().endswith('.png')]

    if not files:
        print(f"Atencion: No se encontraron archivos PNG en: {source_dir}")
        print("Verifica que la carpeta Logos tenga imagenes PNG dentro.")
        return

    total_old_bytes = 0
    total_new_bytes = 0
    converted_count = 0

    print(f"--- Iniciando conversion de {len(files)} archivos ---\n")

    for filename in files:
        source_path = os.path.join(source_dir, filename)
        output_filename = os.path.splitext(filename)[0] + ".webp"
        output_path = os.path.join(output_dir, output_filename)

        try:
            with Image.open(source_path) as img:
                img.save(output_path, "WEBP", lossless=True, method=6)
            
            old_size = os.path.getsize(source_path)
            new_size = os.path.getsize(output_path)
            
            total_old_bytes += old_size
            total_new_bytes += new_size
            converted_count += 1
            
            ahorro_individual = (1 - (new_size / old_size)) * 100
            print(f"OK: {filename} -> {output_filename} (-{ahorro_individual:.1f}%)")
            
        except Exception as e:
            print(f"Error con {filename}: {e}")

    if converted_count > 0:
        ahorro_total_bytes = total_old_bytes - total_new_bytes
        ahorro_mb = ahorro_total_bytes / (1024 * 1024)
        porcentaje_total = (1 - (total_new_bytes / total_old_bytes)) * 100

        print("\n" + "="*40)
        print("RESUMEN DE OPTIMIZACION")
        print("="*40)
        print(f"Archivos procesados: {converted_count}")
        print(f"Ahorro total de espacio: {ahorro_mb:.4f} MB")
        print(f"Eficiencia promedio: {porcentaje_total:.2f}%")
        print(f"Los archivos estan en: {output_dir}")
        print("="*40)

# --- CONFIGURACION ---
# Usamos r'' para que Windows no de error con las barras invertidas
ORIGEN = r'C:\Users\Juan\OneDrive\Escritorio\Logos'
DESTINO = r'C:\Users\Juan\OneDrive\Escritorio\Logos_Webp'

convert_png_to_webp_with_analytics(ORIGEN, DESTINO)