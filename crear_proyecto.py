# --- PROYECTO 1: OCULTAR SECRETO ---
import stepic
from PIL import Image

def ejecutar():
    try:
        # Abrir la imagen original
        img = Image.open("imagen.png")
        
        # Pedir el mensaje al usuario
        secreto = input("Mensaje que quieres ocultar: ")
        
        # Convertir a bytes y mezclar con la imagen
        datos = secreto.encode('utf-8')
        img_nueva = stepic.encode(img, datos)
        
        # Guardar la imagen con el secreto
        img_nueva.save("secreto.png")
        print("\n[+] Hecho: Se creó 'secreto.png' con tu mensaje.")
        
    except FileNotFoundError:
        print("\n[!] Error: Pon una foto llamada 'imagen.png' en esta carpeta.")

ejecutar()