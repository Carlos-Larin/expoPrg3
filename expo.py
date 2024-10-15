from PIL import Image, ImageChops, ImageEnhance, ImageOps, ImageDraw, ImageFont
import os

#función del bob constructor
def tilin():

    #cargar la imagen
    imagen = Image.open("imagenes/arthur.jpg")
    
    #invertir colores
    imageninvertida = ImageChops.invert(imagen)
    imageninvertida.save("imagenes/arthur_colores.jpg")
    
    #resaltar luces (aumentar brillo)
    enhancer = ImageEnhance.Brightness(imagen)
    imagen = enhancer.enhance(1.5)  # Aumentar brillo en un 50%
    imagen.save("imagenes/arthur_luces.jpg")

    #crear un efecto espejo
    cloveEspejo = ImageOps.mirror(imagen)
    cloveEspejo.save("imagenes/arthur_espejo.jpg")

    #agregar texto a la imagen original
    draw = ImageDraw.Draw(imagen)
    
    #cargar una fuente con tamaño grande (ej. Arial, 40)
    try:
        font = ImageFont.truetype("arial.ttf", 40)  #cambia el tamaño aquí para hacerlo más grande o más pequeño
    except IOError:
        font = ImageFont.load_default()  #usar la fuente predeterminada si no se encuentra la fuente "arial.ttf"
    
    draw.text((100, 100), "¡tengo miedo!", fill="white", font=font)  #agregar texto con la fuente cargada
    imagen.save("imagenes/arthur_letras.jpg")

#aqui lanzamos el codigo inzano
if __name__ == "__main__":
    tilin()
