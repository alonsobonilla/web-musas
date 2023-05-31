#insertar, eliminar, obtener, actualizar
from flask import Blueprint, jsonify, request
from model.Usuario import Usuario

api_admin = Blueprint('api_admin', __name__)

@api_admin.route('/delete_usuario_admin', methods=['POST'])
def delete():
    try:
        idAdmin = request.json["idAdmin"]

        validate_id = Usuario.get_usuario(idAdmin)
        if validate_id is not None:
            Usuario.delete_usuario(idAdmin)
            return jsonify({"mensaje": "Usuario eliminado exitosamente"})
        return jsonify({"mensaje": "Usuario no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "Error al eliminar usuario", "error": str(e)})

@api_admin.route('/get_usuario_admin/<int:idAdmin>')
def get_usuario_id(idAdmin):
    try:
        usuario = Usuario.get_usuario(idAdmin)
        if usuario is not None:
            rpta = Usuario(usuario[0], usuario[1], usuario[2]).diccionario.copy()
            return jsonify({"mensaje": "Usuario encontrado", "usuario": rpta})
        return jsonify({"mensaje": "Usuario no encontrado"})
    except Exception as e: 
        return jsonify({"mensaje": "Error al obtener usuario", "error": str(e)})

@api_admin.route('/get_usuario_admin/<string:username>')
def get_usuario_username(username):
    try:
        usuario = Usuario.get_username(username)
        if usuario is not None:
            rpta = Usuario(usuario[0], usuario[1], usuario[2]).diccionario.copy()
            return jsonify({"mensaje": "Usuario encontrado", "usuario": rpta})
        return jsonify({"mensaje": "Usuario no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener usuario", "error": str(e)})
    
@api_admin.route('/get_usuarios_admin')
def get_usuarios():
    try:
        usuarios = Usuario.get_usuarios()
        rpta = []
        for usuario in usuarios:
            rpta.append(Usuario(usuario[0], usuario[1], usuario[2]).diccionario.copy())
        return jsonify({"mensaje": "Usuarios encontrados", "usuarios": rpta})
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener usuarios", "error": str(e)})

@api_admin.route('/insert_usuario_admin', methods=['POST'])
def insert():
    try:
        usuario = request.json["usuario"]
        contraseña = request.json["contraseña"]

        validate_usuario = Usuario.get_username(usuario)

        if validate_usuario is None:
            Usuario.insert_usuario(usuario, contraseña)
            return jsonify({"mensaje": "Usuario registrado exitosamente"})
        return jsonify({"mensaje": "Usuario ya existe"})
    except Exception as e:
        return jsonify({"mensaje": "Error al registrar usuario", "error": str(e)})

@api_admin.route('/update_usuario_admin', methods=['POST'])
def update():
    try:
        usuario = request.json["usuario"]
        contraseña = request.json["contraseña"]

        validate_usuario = Usuario.get_username(usuario)

        if validate_usuario is not None:
            Usuario.update_usuario( usuario, contraseña)
            return jsonify({"mensaje": "Contraseña actualizada exitosamente"})
        return jsonify({"mensaje": "Usuario no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "Error al actualizar usuario", "error": str(e)})