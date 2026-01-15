# --- PROYECTO 1: LEER SECRETO ---
import stepic
from PIL import Image

def leer():
    try:
        # 1. Abrir la imagen que tiene el mensaje oculto
        img = Image.open("secreto.png")
        
        # 2. Extraer los datos (decodificar)
        mensaje = stepic.decode(img)
        
        # 3. Mostrar el resultado
        print("\n" + "="*25)
        print("   MENSAJE RECUPERADO")
        print("="*25)
        print(mensaje)
        print("="*25)
        
        # Pausa para que no se cierre si lo usas como .exe
        input("\nPresiona Enter para salir...")

    except FileNotFoundError:
        print("\n[!] Error: No se encontró el archivo 'secreto.png'.")
        print("Primero debes correr 'crear_proyecto.py'.")

# Ejecutar el lector
leer()