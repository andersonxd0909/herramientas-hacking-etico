# PROYECTO: ANALISTA DE RED
import os

# Tu red suele ser 192.168.1 o 192.168.0
# Ahora el usuario puede poner su propia red
red = input("Ingresa los primeros tres octetos de tu red (ej. 192.168.1): ")

print(f"Buscando dispositivos en {red}.x...")

for i in range(1, 11): # Prueba las primeras 10 direcciones
    ip = f"{red}.{i}"
    # 'ping' envía una señal para ver si alguien responde
    comando = os.system(f"ping -n 1 -w 100 {ip} > nul")
    
    if comando == 0:
        print(f"[!] DISPOSITIVO CONECTADO: {ip}")
    else:
        print(f"[-] {ip} libre")