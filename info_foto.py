# PROYECTO: HACKER DE METADATOS
from PIL import Image
from PIL.ExifTags import TAGS

def leer_datos():
    # Pon una foto real aquí para ver sus datos
    archivo = "foto_prueba.jpg" 
    try:
        img = Image.open(archivo)
        info = img._getexif()
        if info:
            for id_tag, valor in info.items():
                tag = TAGS.get(id_tag, id_tag)
                print(f"{tag}: {valor}")
        else:
            print("La foto no tiene datos ocultos (está limpia).")
    except:
        print("No se pudo abrir la imagen.")

leer_datos()