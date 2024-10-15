from PIL import Image, ImageChops, ImageEnhance, ImageOps, ImageDraw, ImageFont
import os

#función del bob constructor
def tilin():
    """
    #verificar si la carpeta "imagenes" existe 
    if not os.path.exists("imagenes"):
        os.makedirs("imagenes")
    """

    #cargar la imagen
    imagen = Image.open("imagenes/XD.jpg")
    
    #invertir colores
    imageninvertida = ImageChops.invert(imagen)
    imageninvertida.save("imagenes/XD_colores.jpg")
    
    #resaltar luces (aumentar brillo)
    enhancer = ImageEnhance.Brightness(imagen)
    imagen = enhancer.enhance(1.5)  # Aumentar brillo en un 50%
    imagen.save("imagenes/XD_luces.jpg")

    #crear un efecto espejo
    cloveEspejo = ImageOps.mirror(imagen)
    cloveEspejo.save("imagenes/XD_espejo.jpg")

    #agregar texto a la imagen original
    draw = ImageDraw.Draw(imagen)
    
    #cargar una fuente con tamaño grande (ej. Arial, 40)
    try:
        font = ImageFont.truetype("arial.ttf", 40)  #cambia el tamaño aquí para hacerlo más grande o más pequeño
    except IOError:
        font = ImageFont.load_default()  #usar la fuente predeterminada si no se encuentra la fuente "arial.ttf"
    
    draw.text((100, 100), "¡No pikees mid!", fill="white", font=font)  #agregar texto con la fuente cargada
    imagen.save("imagenes/XD_letras.jpg")

#aqui lanzamos el codigo inzano
if __name__ == "__main__":
    tilin()
