from CarreraDAO import agregar, ver_todos, actualizar, borrar
from Carrera import Carrera

def leer_entero(msg):
    while True:
        val = input(msg).strip()
        if val.isdigit():
            return int(val)
        print("Error: introduce un número entero válido.")

def leer_texto(msg):
    while True:
        val = input(msg).strip()
        if val != "":
            return val
        print("Error: el campo no puede estar vacío.")

def set_id_seguro(obj, valor_id):
    try:
        obj.id = valor_id
    except Exception:
        try:
            obj.setId(valor_id)
        except Exception:
            pass

def menu():
    print("=== GESTIÓN DE CARRERAS ===")
    usuario = leer_texto("Usuario de MySQL: ")
    contrasena = input("Contraseña: ")

    while True:
        print("\n1. Agregar carrera")
        print("2. Ver todas las carreras")
        print("3. Actualizar carrera")
        print("4. Borrar carrera")
        print("5. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            try:
                nombre = leer_texto("Nombre: ")
                duracion = leer_entero("Duración (años): ")
                institucion = leer_texto("Institución: ")
                carrera = Carrera(nombre, duracion, institucion)
                creada = agregar(carrera, usuario, contrasena)
                if creada:
                    print("Carrera agregada:", creada)
                else:
                    print("No se pudo agregar (revisa conexión/credenciales/BD).")
            except Exception as e:
                print("Error inesperado al agregar:", e)

        elif opcion == "2":
            try:
                carreras = ver_todos(usuario, contrasena)
                if not carreras:
                    print("(Sin registros o error de conexión)")
                else:
                    print("\n--- LISTA DE CARRERAS ---")
                    for c in carreras:
                        print(c)
            except Exception as e:
                print("Error al listar:", e)
                print("(Sin registros o error de conexión)")

        elif opcion == "3":
            try:
                idc = leer_entero("ID de la carrera a actualizar: ")

                print("Deja vacío para mantener el valor actual.")
                nombre = input("Nuevo nombre: ").strip()
                dur_txt = input("Nueva duración (años): ").strip()
                institucion = input("Nueva institución: ").strip()

                if nombre == "":
                    nombre = leer_texto("Nombre (obligatorio para actualizar): ")
                if dur_txt == "":
                    duracion = leer_entero("Duración (años) (obligatorio para actualizar): ")
                else:
                    if not dur_txt.isdigit():
                        print("Duración no válida.")
                        continue
                    duracion = int(dur_txt)
                if institucion == "":
                    institucion = leer_texto("Institución (obligatoria para actualizar): ")

                c = Carrera(nombre, duracion, institucion)
                set_id_seguro(c, idc)

                nueva = actualizar(c, usuario, contrasena)
                if nueva:
                    print("Carrera actualizada:", nueva)
                else:
                    print("No se pudo actualizar (ID inexistente o error).")
            except Exception as e:
                print("Error inesperado al actualizar:", e)

        elif opcion == "4":
            try:
                idc = leer_entero("ID de la carrera a borrar: ")
                c = Carrera("", 0, "")
                set_id_seguro(c, idc)
                ok = borrar(c, usuario, contrasena)
                if ok:
                    print(f"Carrera borrada (id: {idc})")
                else:
                    print("No se pudo borrar (ID inexistente o error).")
            except Exception as e:
                print("Error inesperado al borrar:", e)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Elige 1-5.")

if __name__ == "__main__":
    menu()
