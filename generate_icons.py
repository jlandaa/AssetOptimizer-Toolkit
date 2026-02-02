import os
from PIL import Image

def generate_from_ico(source_ico_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Directorio creado: {output_folder}")

    try:
        with Image.open(source_ico_path) as img:
            # Un .ico puede tener varias capas. Buscamos la más grande.
            # Convertimos a RGBA para asegurar compatibilidad con PNG.
            img = img.convert("RGBA")
            
            # 1. Apple Touch Icon (180x180)
            apple_icon = img.resize((180, 180), Image.Resampling.LANCZOS)
            apple_icon.save(os.path.join(output_folder, "apple-touch-icon.png"), "PNG")
            print("✓ apple-touch-icon.png generado (Nota: puede verse pixelado si el origen es pequeño)")

            # 2. Favicons PNG para navegadores modernos
            for size in [32, 16]:
                fav_png = img.resize((size, size), Image.Resampling.LANCZOS)
                fav_png.save(os.path.join(output_folder, f"favicon-{size}x{size}.png"), "PNG")
                print(f"✓ favicon-{size}x{size}.png generado")

    except Exception as e:
        print(f"Error procesando el icono: {e}")

if __name__ == "__main__":
    # Ruta donde tienes tu icono actual en el escritorio
    ruta_ico = r"C:\Users\Juan\OneDrive\Escritorio\Logos\favicon_sol.ico"
    # Carpeta de destino en tu proyecto
    generate_from_ico(ruta_ico, "./img/Logos/")