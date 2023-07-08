from flask import jsonify, Blueprint, request
from flask_jwt import jwt_required
from model.Usuario import Usuario

api_usuarios = Blueprint('api_usuarios', __name__)
@api_usuarios.route("/api_obtenerusuarios")
@jwt_required()
def api_obtenerusuarios():
    try:
        usuarios= Usuario.obtener_usuarios()
        listaserializable = []
        for usuario in usuarios:
            miobj = Usuario(usuario[1],usuario[2],usuario[3],usuario[4],usuario[5],usuario[6], usuario[7])
            listaserializable.append(miobj.midic.copy())
        return jsonify({"mensaje": "Usuarios encontrados", "usuarios": listaserializable})
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener usuarios", "error": str(e)}) 


@api_usuarios.route("/api_guardarusuario", methods=["POST"])
@jwt_required()
def api_guardarusuario():
    try:
        DNI = request.json["DNI"]
        nombres = request.json["nombres"]
        apellidos = request.json["apellidos"]
        correo = request.json["correo"]
        numTel = request.json["numTel"]
        contraseña = request.json["contraseña"]
        tipoUsuario = request.json["tipoUsuario"]
        usuario = Usuario.obtener_usuario_dni_tipo(DNI,tipoUsuario)

        if usuario is None:
            Usuario.insertar_usuario(DNI, nombres, apellidos, correo, numTel,contraseña,tipoUsuario)
            return jsonify({"Mensaje":"usuario registrado correctamente"})
        else: 
            return jsonify({"Mensaje":"usuario ya existe "})
        
    except Exception as e:
        return jsonify({"mensaje": "Error al guardar usuario", "error": str(e)})
    

@api_usuarios.route("/api_eliminarusuario", methods=["POST"])
@jwt_required()
def api_eliminarusuario():
    try:
        dni = request.json["DNI"]
        tipoUsuario = request.json["tipoUsuario"]
        usuario = Usuario.obtener_usuario_dni_tipo(dni,tipoUsuario)

        if usuario is None:
            Usuario.eliminar_usuario(dni, tipoUsuario)
            return jsonify({"Mensaje":"Usuario eliminado correctamente"})
        else: 
            return jsonify({"Mensaje":"El usuario no existe"})
      
    except Exception as e:
        return jsonify({"mensaje": "Error al eliminar usuario", "error": str(e)})
    

@api_usuarios.route("/api_obtenerusuario", methods=["POST"])
@jwt_required()
def api_obtenerusuario_por_dni_tipo():  
    try:
        dni = request.json["DNI"]
        tipoUsuario = request.json["tipoUsuario"]
        usuario = Usuario.obtener_usuario_dni_tipo(dni, tipoUsuario)
        if usuario is not None:
            listaserializable = []
            miobj = Usuario(usuario[1],usuario[2],usuario[3],usuario[4],usuario[5],usuario[6], usuario[7])
            listaserializable.append(miobj.midic.copy())
            return jsonify({"mensaje":"Usuario encontrado", "usuario": listaserializable})
        return jsonify({"mensaje":"Usuario no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener usuario", "error": str(e)})

