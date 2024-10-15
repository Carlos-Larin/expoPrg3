from PIL import Image, ImageChops, ImageEnhance, ImageOps, ImageDraw, ImageFont
import os

# Función del constructor
def tilin():
    # Verificar si la carpeta "imagenes" existe
    if not os.path.exists("imagenes"):
        os.makedirs("imagenes")

    # Cargar la imagen
    imagen = Image.open("imagenes/XD.jpg")
    
    # Invertir colores
    imageninvertida = ImageChops.invert(imagen)
    imageninvertida.save("imagenes/XD_colores.jpg")
    
    # Resaltar luces (aumentar brillo)
    enhancer = ImageEnhance.Brightness(imagen)
    imagen = enhancer.enhance(1.5)  # Aumentar brillo en un 50%
    imagen.save("imagenes/XD_luces.jpg")

    # Crear un efecto espejo
    cloveEspejo = ImageOps.mirror(imagen)
    cloveEspejo.save("imagenes/XD_espejo.jpg")

    # Agregar texto a la imagen original
    draw = ImageDraw.Draw(imagen)
    
    # Cargar una fuente con tamaño grande (ej. Arial, 40)
    try:
        font = ImageFont.truetype("arial.ttf", 40)  # Cambia el tamaño aquí para hacerlo más grande o más pequeño
    except IOError:
        font = ImageFont.load_default()  # Usar la fuente predeterminada si no se encuentra la fuente "arial.ttf"
    
    draw.text((100, 100), "¡No pikees mid!", fill="white", font=font)  # Agregar texto con la fuente cargada
    imagen.save("imagenes/XD_letras.jpg")

if __name__ == "__main__":
    tilin()
