# PROYECTO: EL ESCUDO (CIFRADO)
from cryptography.fernet import Fernet

# Crear la llave de seguridad
llave = Fernet.generate_key()
cipher = Fernet(llave)

texto = input("Escribe el mensaje secreto: ").encode()
bloqueado = cipher.encrypt(texto)

print(f"\n[+] MENSAJE CIFRADO: {bloqueado.decode()}")
print(f"[+] LLAVE PARA DESBLOQUEAR: {llave.decode()}")
# NOTA: Sin esa llave, nadie puede leer el mensaje.

#pip install cryptography