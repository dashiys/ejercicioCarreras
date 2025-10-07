from db_conexion import coneccion_bd
from Carrera import Carrera

def _set_id(obj, valor_id):
    try:
        obj.id = valor_id
        return
    except Exception:
        pass
    try:
        obj.setId(valor_id)
    except Exception:
        pass

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
        _set_id(carrera, cursor.lastrowid)
        return carrera
    except Exception as e:
        print("Error al insertar:", e)
        return None
    finally:
        try:
            cursor.close()
            conexion.close()
        except Exception:
            pass

def ver_todos(usuario, contrasena):
    """Devuelve una lista de objetos Carrera."""
    conexion = coneccion_bd(usuario, contrasena)
    lista = []
    if not conexion or not conexion.is_connected():
        print("No se pudo conectar a la base de datos.")
        return lista
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT idcarreras, nombre, duracion, institucion FROM carreras ORDER BY idcarreras")
        filas = cursor.fetchall() or []
        for fila in filas:
            c = Carrera(fila[1], fila[2], fila[3])
            _set_id(c, fila[0])
            lista.append(c)
        return lista
    except Exception as e:
        print("Error al listar:", e)
        return lista
    finally:
        try:
            cursor.close()
            conexion.close()
        except Exception:
            pass

def actualizar(carrera, usuario, contrasena):
    """Actualiza una carrera existente y devuelve el objeto actualizado o None."""
    idc = getattr(carrera, "id", None)
    if idc is None:
        try:
            idc = carrera.getId()
        except Exception:
            idc = None
    if idc is None:
        print("El objeto Carrera no tiene ID asignado.")
        return None

    conexion = coneccion_bd(usuario, contrasena)
    if not conexion or not conexion.is_connected():
        print("No se pudo conectar a la base de datos.")
        return None
    try:
        cursor = conexion.cursor()
        sql = "UPDATE carreras SET nombre=%s, duracion=%s, institucion=%s WHERE idcarreras=%s"
        datos = (carrera.nombre, carrera.duracion, carrera.institucion, idc)
        cursor.execute(sql, datos)
        conexion.commit()
        if cursor.rowcount == 0:
            print("No se encontró ninguna carrera con ese ID.")
            return None

        cursor.execute("SELECT idcarreras, nombre, duracion, institucion FROM carreras WHERE idcarreras=%s", (idc,))
        fila = cursor.fetchone()
        if fila:
            c = Carrera(fila[1], fila[2], fila[3])
            _set_id(c, fila[0])
            return c
        return None
    except Exception as e:
        print("Error al actualizar:", e)
        return None
    finally:
        try:
            cursor.close()
            conexion.close()
        except Exception:
            pass

def borrar(carrera, usuario, contrasena):
    """Borra la carrera indicada por su ID. Devuelve True si se eliminó."""
    idc = getattr(carrera, "id", None)
    if idc is None:
        try:
            idc = carrera.getId()
        except Exception:
            idc = None
    if idc is None:
        print("El objeto Carrera no tiene ID asignado.")
        return False

    conexion = coneccion_bd(usuario, contrasena)
    if not conexion or not conexion.is_connected():
        print("No se pudo conectar a la base de datos.")
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM carreras WHERE idcarreras=%s", (idc,))
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
        try:
            cursor.close()
            conexion.close()
        except Exception:
            pass
