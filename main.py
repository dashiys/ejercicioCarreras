import requests
from db_conexion import coneccion_bd

BASE = "http://127.0.0.1:5000" 

def leer_entero(msg):
    while True:
        val = input(msg).strip()
        if val.isdigit():
            return int(val)
        print("Introduce un número válido.")

def leer_texto(msg):
    while True:
        val = input(msg).strip()
        if val != "":
            return val
        print("No puede estar vacío.")

def menu():
    print("=== CONSUMIDOR DE LA API DE CARRERAS ===")
    usuario = leer_texto("Usuario MySQL: ")
    contrasena = input("Contraseña: ")

    conexion = coneccion_bd(usuario, contrasena)
    if not conexion or not conexion.is_connected():
        print("No se pudo conectar a la base de datos.")
        return
    else:
        print("Conexión exitosa a la base de datos.")
        conexion.close()

    while True:
        print("\n1. Agregar carrera (POST)")
        print("2. Ver todas las carreras (GET)")
        print("3. Actualizar carrera (PUT)")
        print("4. Borrar carrera (DELETE)")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = leer_texto("Nombre: ")
            duracion = leer_entero("Duración (años): ")
            institucion = leer_texto("Institución: ")

            data = {
                "usuario": usuario,
                "contrasena": contrasena,
                "nombre": nombre,
                "duracion": duracion,
                "institucion": institucion
            }
            r = requests.post(f"{BASE}/carreras", json=data)
            print("", r.json())

        elif opcion == "2":
            params = {"usuario": usuario, "contrasena": contrasena}
            r = requests.get(f"{BASE}/carreras", params=params)
            respuesta = r.json()
            if respuesta.get("success"):
                print("\n--- CARRERAS ---")
                for c in respuesta.get("data", []):
                    print(f"ID: {c['id']} | {c['nombre']} ({c['duracion']} años) - {c['institucion']}")
            else:
                print("", respuesta.get("message"))

        elif opcion == "3":
            idc = leer_entero("ID de la carrera a actualizar: ")
            nombre = leer_texto("Nuevo nombre: ")
            duracion = leer_entero("Nueva duración (años): ")
            institucion = leer_texto("Nueva institución: ")

            data = {
                "usuario": usuario,
                "contrasena": contrasena,
                "nombre": nombre,
                "duracion": duracion,
                "institucion": institucion
            }
            r = requests.put(f"{BASE}/carreras/{idc}", json=data)
            print("", r.json())

        elif opcion == "4":
            idc = leer_entero("ID de la carrera a borrar: ")
            data = {"usuario": usuario, "contrasena": contrasena}
            r = requests.delete(f"{BASE}/carreras/{idc}", json=data)
            print("", r.json())

        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")





if __name__ == "__main__":
    menu()