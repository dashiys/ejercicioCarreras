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
            duracion = int(input("Duración (años): "))
            institucion = input("Institución: ")
            carrera = Carrera(nombre=nombre, duracion=duracion, institucion=institucion)
            if agregar(carrera, user, password):
                print("Carrera agregada correctamente.")
            else:
                print("Error al agregar la carrera.")

        elif opcion == "2":
            carreras = ver_todos(user, password)
            if carreras:
                print("\n--- LISTA DE CARRERAS ---")
                for c in carreras:
                    print(c)
            else:
                print("No hay carreras registradas.")

        elif opcion == "3":
            id_update = int(input("ID de la carrera a actualizar: "))
            nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
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
            id_delete = int(input("ID de la carrera a borrar: "))
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
