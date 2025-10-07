from flask import Flask, request, jsonify
from CarreraDAO import agregar, ver_todos, actualizar, borrar
from Carrera import Carrera

app = Flask(__name__)

@app.route('/carreras', methods=['POST'])
def crear_carrera():
    data = request.get_json()
    usuario = data.get('usuario')
    contrasena = data.get('contrasena')
    nombre = data.get('nombre')
    duracion = data.get('duracion')
    institucion = data.get('institucion')

    if not all([usuario, contrasena, nombre, duracion, institucion]):
        return jsonify({"success": False, "message": "Faltan datos"}), 400

    try:
        duracion = int(duracion)
        carrera = Carrera(nombre, duracion, institucion)
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
        return jsonify({"success": False, "message": "Faltan credenciales"}), 400

    try:
        carreras = ver_todos(usuario, contrasena)
        data = []
        for c in carreras:
            data.append({
                "id": getattr(c, "id", None),
                "nombre": getattr(c, "nombre", ""),
                "duracion": getattr(c, "duracion", 0),
                "institucion": getattr(c, "institucion", "")
            })
        return jsonify({"success": True, "data": data}), 200
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

    if not all([usuario, contrasena, nombre, duracion, institucion]):
        return jsonify({"success": False, "message": "Faltan datos"}), 400

    try:
        duracion = int(duracion)
        c = Carrera(nombre, duracion, institucion)
        c.id = idcarreras
        resultado = actualizar(c, usuario, contrasena)
        if resultado:
            return jsonify({"success": True, "message": "Carrera actualizada correctamente"}), 200
        else:
            return jsonify({"success": False, "message": "No se encontró la carrera"}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/carreras/<int:idcarreras>', methods=['DELETE'])
def eliminar_carrera(idcarreras):
    data = request.get_json()
    usuario = data.get('usuario')
    contrasena = data.get('contrasena')

    if not usuario or not contrasena:
        return jsonify({"success": False, "message": "Faltan credenciales"}), 400

    try:
        c = Carrera("", 0, "")
        c.id = idcarreras
        borrada = borrar(c, usuario, contrasena)
        if borrada:
            return jsonify({"success": True, "message": "Carrera eliminada correctamente"}), 200
        else:
            return jsonify({"success": False, "message": "No se encontró la carrera"}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)