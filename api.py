from flask import Flask, request, jsonify
from CarreraDAO import agregar, ver_todos, actualizar, borrar
from Carrera import Carrera

app = Flask(__name__)

@app.route('/carreras', methods=['POST'])
def crear_carrera():
    data = request.get_json()

    nombre = data.get('nombre')
    duracion = data.get('duracion')
    institucion = data.get('institucion')
    usuario = data.get('usuario')
    contrasena = data.get('contrasena')

    if not all([nombre, duracion, institucion, usuario, contrasena]):
        return jsonify({"success": False, "message": "Faltan datos requeridos"}), 400

    try:
        carrera = Carrera(nombre=nombre, duracion=int(duracion), institucion=institucion)
        resultado = agregar(carrera, usuario, contrasena)

        if resultado:
            return jsonify({"success": True, "message": "Carrera agregada correctamente"}), 201
        else:
            return jsonify({"success": False, "message": "Error al agregar la carrera"}), 500
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@app.route('/carreras', methods=['GET'])
def obtener_carreras():
    usuario = request.args.get('usuario')
    contrasena = request.args.get('contrasena')

    if not usuario or not contrasena:
        return jsonify({"success": False, "message": "Debe proporcionar usuario y contraseña"}), 400

    try:
        connection_data = ver_todos(usuario, contrasena)
        return jsonify({"success": True, "message": "Listado de carreras mostrado en consola"}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
    
@app.route('/carreras/<int:idcarreras>', methods=['PUT'])
def modificar_carrera(idcarreras):
    data = request.get_json()
    usuario = data.get('usuario')
    contrasena = data.get('contrasena')
    nombre = data.get('nombre')
    duracion = data.get('duracion')
    institucion = data.get('institucion')

    if not usuario or not contrasena:
        return jsonify({"success": False, "message": "Usuario y contraseña requeridos"}), 400

    try:
        resultado = actualizar(idcarreras, usuario, contrasena, nombre, duracion, institucion)
        if resultado:
            return jsonify({"success": True, "message": "Carrera actualizada correctamente"}), 200
        else:
            return jsonify({"success": False, "message": "No se encontró la carrera o no se realizaron cambios"}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@app.route('/carreras/<int:idcarreras>', methods=['DELETE'])
def eliminar_carrera(idcarreras):
    data = request.get_json()
    usuario = data.get('usuario')
    contrasena = data.get('contrasena')

    if not usuario or not contrasena:
        return jsonify({"success": False, "message": "Usuario y contraseña requeridos"}), 400

    try:
        resultado = borrar(idcarreras, usuario, contrasena)
        if resultado:
            return jsonify({"success": True, "message": "Carrera eliminada correctamente"}), 200
        else:
            return jsonify({"success": False, "message": "No se encontró la carrera con ese ID"}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == 'main':
    app.run(debug=True)