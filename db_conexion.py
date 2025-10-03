import mysql.connector

def coneccion_bd(user, password):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user=user,
            password=password,
            database="carreras"
        )
        if connection.is_connected():
            return connection
    except mysql.connector.Error as err:
        return None