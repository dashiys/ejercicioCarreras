from db_conexion import coneccion_bd
from Carrera import Carrera

def agregar(carrera, usuario, contrasena):
    """Agrega una carrera y devuelve el objeto con su ID asignado."""
    conexion = coneccion_bd(usuario, contrasena)
    if not conexion or not conexion.is_connected():
        print("No se pudo conectar a la base de datos.")
        return None
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO carreras (nombre, duracion, institucion) VALUES (%s, %s, %s)"
        datos = (carrera.nombre, carrera.duracion, carrera.institucion)
        cursor.execute(sql, datos)
        conexion.commit()
        carrera.id = cursor.lastrowid
        return carrera
    except Exception as e:
        print("Error al insertar:", e)
        return None
    finally:
        cursor.close()
        conexion.close()


def ver_todos(usuario, contrasena):
    """Devuelve una lista de objetos Carrera."""
    conexion = coneccion_bd(usuario, contrasena)
    lista = []
    if not conexion or not conexion.is_connected():
        print("No se pudo conectar a la base de datos.")
        return lista
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT idcarreras, nombre, duracion, institucion FROM carreras")
        filas = cursor.fetchall()
        for fila in filas:
            c = Carrera(fila[1], fila[2], fila[3], fila[0])
            lista.append(c)
        return lista
    except Exception as e:
        print("Error al listar:", e)
        return lista
    finally:
        cursor.close()
        conexion.close()


def actualizar(carrera, usuario, contrasena):
    """Actualiza una carrera existente y devuelve el objeto actualizado o None."""
    if carrera.id is None:
        print("El objeto Carrera no tiene ID asignado.")
        return None
    conexion = coneccion_bd(usuario, contrasena)
    if not conexion or not conexion.is_connected():
        print("No se pudo conectar a la base de datos.")
        return None
    try:
        cursor = conexion.cursor()
        sql = "UPDATE carreras SET nombre=%s, duracion=%s, institucion=%s WHERE idcarreras=%s"
        datos = (carrera.nombre, carrera.duracion, carrera.institucion, carrera.id)
        cursor.execute(sql, datos)
        conexion.commit()
        if cursor.rowcount == 0:
            print("No se encontró ninguna carrera con ese ID.")
            return None
        # Leer la versión actualizada
        cursor.execute("SELECT idcarreras, nombre, duracion, institucion FROM carreras WHERE idcarreras=%s", (carrera.id,))
        fila = cursor.fetchone()
        if fila:
            return Carrera(fila[1], fila[2], fila[3], fila[0])
        return None
    except Exception as e:
        print("Error al actualizar:", e)
        return None
    finally:
        cursor.close()
        conexion.close()


def borrar(carrera, usuario, contrasena):
    """Borra la carrera indicada por su ID. Devuelve True si se eliminó."""
    if carrera.id is None:
        print("El objeto Carrera no tiene ID asignado.")
        return False
    conexion = coneccion_bd(usuario, contrasena)
    if not conexion or not conexion.is_connected():
        print("No se pudo conectar a la base de datos.")
        return False
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM carreras WHERE idcarreras=%s"
        cursor.execute(sql, (carrera.id,))
        conexion.commit()
        if cursor.rowcount > 0:
            return True
        else:
            print("No se encontró la carrera para borrar.")
            return False
    except Exception as e:
        print("Error al borrar:", e)
        return False
    finally:
        cursor.close()
        conexion.close()

