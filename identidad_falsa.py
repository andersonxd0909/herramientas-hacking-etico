# --- PROYECTO 2: IDENTIDADES FALSAS ---
from faker import Faker

fake = Faker('es_ES')

def crear_identidades():
    try:
        num = input("¿Cuántas identidades quieres?: ")
        cantidad = int(num)
        
        for i in range(cantidad):
            print(f"\n--- IDENTIDAD #{i+1} ---")
            print(f"Nombre:    {fake.name()}")
            print(f"Email:     {fake.email()}")
            
            # Corregimos el error del backslash aquí:
            dir_limpia = fake.address().replace('\n', ', ')
            print(f"Dirección: {dir_limpia}")
            
            print(f"Password:  {fake.password(length=10)}")
            print("-" * 25)
            
    except ValueError:
        print("\n[!] Error: Escribe un número entero.")

crear_identidades()