from db_conexion import coneccion_bd
from Carrera import Carrera

def agregar(carrera, usuario, contrasena):
    connection = coneccion_bd(usuario, contrasena)
    if connection.is_connected():
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO carreras (nombre, duracion, institucion) VALUES (%s, %s, %s)"
                val = (carrera.getNombre(), carrera.getDuracion(), carrera.getInstitucion())
                cursor.execute(sql, val)
                connection.commit()
                return True
        except Exception as e:
            print(e)
        finally:
            connection.close()


def ver_todos(usuario, contrasena):
    sql = "SELECT idcarreras, nombre, duracion, institucion FROM carreras ORDER BY idcarreras"
    connection = coneccion_bd(usuario, contrasena)
    if connection.is_connected():
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                rows = cursor.fetchall()
                return [Carrera(idcarreras=row[0], nombre=row[1], duracion=row[2], institucion=row[3]) for row in rows]
        except Exception as e:
            print(e)
        finally:
            connection.close()

def actualizar(idcarreras, usuario, contrasena, nombre=None, duracion=None, institucion=None):
    campos = []
    valores = []
    if nombre is not None:
        campos.append("nombre = %s")
        valores.append(nombre)
    if duracion is not None:
        campos.append("duracion = %s")
        valores.append(duracion)
    if institucion is not None:
        campos.append("institucion = %s")
        valores.append(institucion)

    if not campos:
        return False

    valores.append(idcarreras)
    sql = f"UPDATE carreras SET {', '.join(campos)} WHERE idcarreras = %s"

    connection = coneccion_bd(usuario, contrasena)
    if connection.is_connected():
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, tuple(valores))
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(e)
        finally:
            connection.close()


def borrar(idcarreras, usuario, contrasena):
    sql = "DELETE FROM carreras WHERE idcarreras = %s"
    connection = coneccion_bd(usuario, contrasena)
    if connection.is_connected():
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (idcarreras,))
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(e)
        finally:
            connection.close()
