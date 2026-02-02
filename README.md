# AssetOptimizer-Toolkit 🚀

Este repositorio contiene una colección de scripts en **Python** diseñados para la automatización, procesamiento y optimización técnica de activos visuales destinados a sitios web de alto rendimiento. 

El objetivo principal es garantizar que las imágenes cumplan con los estándares de **Google Lighthouse**, equilibrando una carga ultra-rápida sin sacrificar la nitidez en pantallas de alta densidad (Retina).

## 🛠️ Funcionalidades Principales

* **Conversión a WebP con Analíticas**: Transformación de archivos PNG a WebP utilizando compresión *lossless* y reportando el ahorro exacto en MB y porcentaje.
* **Tratamiento de Transparencias**: Algoritmo que detecta fondos blancos (píxeles con valores RGB > 240) y los convierte automáticamente en canales alfa transparentes.
* **Optimización (Lighthouse Ready)**: Ajuste de dimensiones basado en el ancho de renderizado real del DOM (DPR 1.2x y 2x) para maximizar el performance.
* **Generación de Favicons**: Creación automatizada de `apple-touch-icon` (180x180) y favicons estándar (32x32, 16x16) a partir de un archivo maestro `.ico`.
* **Compresión de Perfil**: Script dedicado para fotos personales, reduciendo drásticamente el peso de archivos originales de alta resolución a formatos web eficientes.

---

## 📋 Estructura de los Scripts

| Archivo | Función |
| :--- | :--- |
| `procesar_logos.py` | Remoción de fondos blancos y conversión a PNG transparente. |
| `convert_to_webp_analytics.py` | Conversión masiva a WebP con reporte detallado de ahorro de espacio. |
| `generate_icons.py` | Generación de activos para navegadores y dispositivos iOS a partir de un `.ico`. |
| `optimizar_perfil.py` | Redimensionamiento (400x400) y compresión de fotos personales. |
| `optimizar_logos.py` | Optimización masiva de logos con anchos objetivos predefinidos. |
| `optimizar_logos_2.py` | Optimización (Display Width * 1.2) para nitidez en pantallas modernas. |
| `optimizar_logos_3.py` | Ajuste final basado en dimensiones exactas extraídas de reportes de Lighthouse. |

---

## 🚀 Instalación y Uso

### 1. Requisitos
Es necesario tener instalado Python 3.x y la biblioteca **Pillow**.

```bash
pip install Pillow
```

### 2. Configuración de Rutas: 
Abre el script que desees utilizar y modifica las variables de ruta (ej. img_folder o base_path) con las direcciones de tus carpetas locales.
```python
# Ejemplo de configuración interna
ORIGEN = r'C:\Users\Juan\OneDrive\Escritorio\Logos'
DESTINO = r'C:\Users\Juan\OneDrive\Escritorio\Logos_Optimized'
```
### 3. Ejecución: 
Corre el script desde tu terminal o IDE:
```bash
# Ejemplo para optimizar logos según dimensiones de Lighthouse
python optimizar_logos_3.py
```

## 💻 Tecnologías Utilizadas
* Lenguaje: Python 3.x
  
* Procesamiento de Imagen: Pillow (PIL)
  
* Formatos Soportados: PNG, JPG, WEBP, ICO.

## 👨‍💻 Autor
Juan Manuel Landa

* Ingeniero en Informática especializado en Business Intelligence, SQL y Data Analytics.

* Residente en Quilmes, Buenos Aires, Argentina.

* [LinkedIn](https://www.linkedin.com/in/juan-manuel-landa/) | [Portfolio ](https://juan-manuel-landa.netlify.app/)
