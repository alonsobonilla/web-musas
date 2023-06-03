#insertar, obtener  (id comprobante , id producto)

from flask import jsonify, Blueprint, request
from flask_jwt import jwt_required
from model.DetalleComprobante import detalleComprobante

api_detalleComprobante = Blueprint('api_detalleComprobante',__name__)


@api_detalleComprobante.route("/api_obtenerdetalleComprobante")
@jwt_required()
def api_obtenerusuarios():
    try:
        detallesorden = detalleComprobante.obtener_detalleComprobante()
        listaserializable = []
        for deO in detallesorden:
            miobj = detalleComprobante(deO[0],deO[1],deO[2],deO[3],deO[4],deO[5])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify ({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})


@api_detalleComprobante.route("/api_guardardetalleComprobante")
@jwt_required()
def api_guardardetalleComprobante():

    try:
        idproducto = request.json["idproducto"]
        idpedido = request.json["idpedido"]
        nomP = request.json["nombreProducto"]
        precioU = request.json["precioUnidad"]
        cantidad = request.json["cantidad"]
        precioT = request.json["precioTotal"]
        detalleComprobante.insertar_detalleComprobante(idproducto,idpedido,nomP,precioU,cantidad,precioT)
        return jsonify({"Mensaje":"usuario registrado correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})


@api_detalleComprobante.route("/api_obtenerdetalleComprobante/<int:idproducto>/<int:idpedido>")
@jwt_required()
def api_obtenerdetalleComprobante(idproducto,idpedido):
    try:
        deO = detalleComprobante.obtener_detalleComprobante_id(idproducto,idpedido)
        listaserializable = []
        miobj = detalleComprobante(deO[0],deO[1],deO[2],deO[3],deO[4],deO[5])
        listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

