# --- MI SUITE DE CIBERSEGURIDAD ---
import os

def mostrar_menu():
    print("\n" + "="*30)
    print("   TOOLKIT DE SEGURIDAD v1.0")
    print("="*30)
    print("1. Ocultar Mensaje (Esteganografía)")
    print("2. Generar Identidades Falsas")
    print("3. Cifrar con Llave Maestra (AES)")
    print("4. Escanear Dispositivos en Red")
    print("5. Extraer Metadatos de Fotos")
    print("0. Salir")
    print("="*30)

while True:
    mostrar_menu()
    opcion = input("Elige una misión: ")

    if opcion == "1":
        os.system('python "1_Esteganografia/crear_proyecto.py"')
    elif opcion == "2":
        os.system('python "2_Generador_Datos/identidad_falsa.py"')
    elif opcion == "3":
        os.system('python "3_Criptografia/encriptador.py"')
    elif opcion == "4":
        os.system('python "4_Escaneo_Red/escaner_red.py"')
    elif opcion == "5":
        os.system('python "5_Forense_Fotos/info_foto.py"')
    elif opcion == "0":
        print("Cerrando sistema...")
        break
    else:
        print("Opción no válida.")
        
#pip install stepic Pillow Faker cryptography
#2314