import os
from PIL import Image

def remove_white_background(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".png", ".jpeg")):
            img = Image.open(os.path.join(input_folder, filename)).convert("RGBA")
            datas = img.getdata()

            newData = []
            for item in datas:
                # Si el píxel es muy cercano al blanco (255, 255, 255)
                if item[0] > 240 and item[1] > 240 and item[2] > 240:
                    newData.append((255, 255, 255, 0)) # Transparente
                else:
                    newData.append(item)

            img.putdata(newData)
            name = os.path.splitext(filename)[0] + ".png"
            img.save(os.path.join(output_folder, name), "PNG")
            print(f"Procesado: {name}")

# Uso: Cambia las rutas por las de tu proyecto
remove_white_background(r'C:\Users\Juan\OneDrive\Escritorio\Logos', r'C:\Users\Juan\OneDrive\Escritorio\Logos_Transparente')