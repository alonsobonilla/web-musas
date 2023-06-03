from flask import jsonify, Blueprint, request
from flask_jwt import jwt_required
from model.Usuario_cliente import Usuario_cliente

api_usuariosCliente = Blueprint('api_usuariosCliente', __name__)
@api_usuariosCliente.route("/api_obtenerusuarios")
@jwt_required()
def api_obtenerusuarios():
    try:
        usuarios= Usuario_cliente.obtener_usuario()
        listaserializable = []
        for usuario in usuarios:
            miobj = Usuario_cliente(usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener usuarios", "error": str(e)}) 
    

@api_usuariosCliente.route("/api_guardarusuario", methods=["POST"])
@jwt_required()
def api_guardarusuario():
    try:
        DNI = request.json["DNI"]
        nombres = request.json["nombres"]
        apellidos = request.json["apellidos"]
        correo = request.json["correo"]
        numTel = request.json["numTel"]
        contraseña = request.json["contraseña"]
        Usuario_cliente.insertar_usuario(DNI, nombres, apellidos, correo, numTel,contraseña)
        return jsonify({"Mensaje":"usuario registrado correctamente"})
    except Exception as e:
        return jsonify({"mensaje": "Error al guardar usuario", "error": str(e)})
    

@api_usuariosCliente.route("/api_eliminarusuario", methods=["POST"])
@jwt_required()
def api_eliminarusuario():
    try:
        Usuario_cliente.eliminar_usuario(request.json["DNI"])
        return jsonify({"Mensaje":"Usuario eliminado correctamente"})
    except Exception as e:
        return jsonify({"mensaje": "Error al eliminar usuario", "error": str(e)})
    

@api_usuariosCliente.route("/api_obtenerusuario/<string:DNI>")
@jwt_required()
def api_obtenerusuario(DNI):
    try:
        usuario = Usuario_cliente.obtener_usuario_dni(DNI)
        listaserializable = []
        miobj = Usuario_cliente(usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5])
        listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener usuario", "error": str(e)})
    