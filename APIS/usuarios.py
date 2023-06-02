from flask import jsonify, Blueprint, request
from model.Usuario_cliente import Usuario_cliente

api_usuariosCliente = Blueprint('api_usuariosCliente', __name__)
@api_usuariosCliente.route("/api_obtenerusuarios")
def api_obtenerusuarios():
    try:
        usuarios= Usuario_cliente.obtener_usuario()
        listaserializable = []
        for usuario in usuarios:
            miobj = Usuario_cliente(usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify ({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"}) 
    

@api_usuariosCliente.route("/api_guardarusuario", methods=["POST"])
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
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})
    

@api_usuariosCliente.route("/api_eliminarusuario", methods=["POST"])
def api_eliminarusuario():
    try:
        Usuario_cliente.eliminar_usuario(request.json["DNI"])
        return jsonify({"Mensaje":"Usuario eliminado correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})
    

@api_usuariosCliente.route("/api_obtenerusuario/<string:DNI>")
def api_obtenerusuario(DNI):
    try:
        usuario = Usuario_cliente.obtener_usuario_dni(DNI)
        listaserializable = []
        miobj = Usuario_cliente(usuario[0],usuario[1],usuario[2],usuario[3],usuario[4])
        listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener usuario", "error": str(e)})
    