#obtener, insertar, obtener por id

from flask import jsonify, Blueprint, request
from model.DetalleOrden import DetalleOrden

api_detalleOrden = Blueprint('api_detalleOrden',__name__)
@api_detalleOrden.route("/api_obtenerdetalleorden")

def api_obtenerusuarios():
    try:
        detallesorden = DetalleOrden.obtener_detalleOrden()
        listaserializable = []
        for deO in detallesorden:
            miobj = DetalleOrden(deO[0],deO[1],deO[2],deO[3],deO[4],deO[5])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify ({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})


@api_detalleOrden.route("/api_guardardetalleorden")
def api_guardardetalleOrden():

    try:
        idproducto = request.json["idproducto"]
        idpedido = request.json["idpedido"]
        nomP = request.json["nombreProducto"]
        precioU = request.json["precioUnidad"]
        cantidad = request.json["cantidad"]
        precioT = request.json["precioTotal"]
        DetalleOrden.insertar_detalleOrden(idproducto,idpedido,nomP,precioU,cantidad,precioT)
        return jsonify({"Mensaje":"usuario registrado correctamente"})
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})


@api_detalleOrden.route("/api_obtenerdetalleorden/<int:idproducto>/<int:idpedido>")
def api_obtenedetalleorden(idproducto,idpedido):
    try:
        deO = DetalleOrden.obtener_detalleOrden_id(idproducto,idpedido)
        listaserializable = []
        miobj = DetalleOrden(deO[0],deO[1],deO[2],deO[3],deO[4],deO[5])
        listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})
