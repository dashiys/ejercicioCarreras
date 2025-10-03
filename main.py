from CarreraDAO import agregar, ver_todos, actualizar, borrar
from Carrera import Carrera

def menu_principal():
    print("=== SISTEMA DE GESTIÓN DE CARRERAS ===")

    user = input("Usuario de MySQL: ")
    password = input("Contraseña: ")

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar carrera")
        print("2. Ver todas las carreras")
        print("3. Actualizar carrera")
        print("4. Borrar carrera")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la carrera: ")
            duracion = input("Duración (años): ")
            while not duracion.isdigit():
                print("Por favor, ingresa un número entero válido para la duración.")
                duracion = input("Duración (años): ")
            duracion = int(duracion)
            institucion = input("Institución: ")
            
            carrera = Carrera(nombre=nombre, duracion=duracion, institucion=institucion)
            if agregar(carrera, user, password):
                print("Carrera agregada correctamente.")
            else:
                print("Error al agregar la carrera.")

        elif opcion == "2":
            print("\n--- LISTA DE CARRERAS ---")
            ver_todos(user, password)

        elif opcion == "3":
            id_update = input("ID de la carrera a actualizar: ")
            while not id_update.isdigit():
                print("Por favor, ingresa un número entero válido para el ID.")
                id_update = input("ID de la carrera a actualizar: ")
            id_update = int(id_update)
            nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
            duracion = input("Nueva duración (años, dejar vacío para no cambiar): ")
            if duracion and not duracion.isdigit():
                while not duracion.isdigit():
                    print("Por favor, ingresa un número entero válido para la duración.")
                    duracion = input("Nueva duración (años, dejar vacío para no cambiar): ")
            institucion = input("Nueva institución (dejar vacío para no cambiar): ")

            nombre = nombre if nombre else None
            duracion = int(duracion) if duracion else None
            institucion = institucion if institucion else None

            if actualizar(id_update, user, password, nombre, duracion, institucion):
                print("Carrera actualizada correctamente.")
            else:
                print("No se encontró la carrera con ese ID.")

        elif opcion == "4":
            id_delete = input("ID de la carrera a borrar: ")
            while not id_delete.isdigit():
                print("Por favor, ingresa un número entero válido para el ID.")
                id_delete = input("ID de la carrera a borrar: ")
            id_delete = int(id_delete)
            if borrar(id_delete, user, password):
                print("Carrera eliminada correctamente.")
            else:
                print("No se encontró la carrera con ese ID.")

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


menu_principal()
