#obtener, insertar, obtener por id

from flask import jsonify, Blueprint, request
from flask_jwt import jwt_required
from model.DetalleOrden import DetalleOrden
from model.Producto import Producto
from model.Pedido import Pedido

api_detalleOrden = Blueprint('api_detalleOrden',__name__)
@api_detalleOrden.route("/api_obtenerdetalleorden")
@jwt_required()
def api_obtenerdetalleorden():
    try:
        detallesorden = DetalleOrden.obtener_detalleOrden()
        listaserializable = []
        for deO in detallesorden:
            miobj = DetalleOrden(deO[0],deO[1],deO[2],deO[3],deO[4],deO[5],deO[6])
            listaserializable.append(miobj.midic.copy())

        return jsonify({"Mensaje":"detalles obtenidos correctamente", "status:":"1", "detalles": listaserializable})
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener detalles orden", "error": str(e)})


@api_detalleOrden.route("/api_obtenerdetalleorden/<int:idDetalleOrden>/<int:idpedido>")
@jwt_required()
def api_obtenedetalleorden(idDetalleOrden,idpedido):
    try:
        listaserializable = []
        deO = DetalleOrden.obtener_detalleOrden_id(idDetalleOrden,idpedido)
        validar_idPedido = Pedido.validar_idPedido_existente(idpedido)

        if not validar_idPedido:
            return jsonify({"Mensaje": "El pedido no existe"})
        elif deO is None:
            return jsonify({"Mensaje": "El detalle de orden no existe"})
        else:
            listaserializable = []
            miobj = DetalleOrden(deO[0],deO[1],deO[2],deO[3],deO[4],deO[5],deO[6])
            listaserializable.append(miobj.midic.copy())
            return jsonify({"Mensaje":"detalle de orden obtenido correctamente", "status:":"1", "detalle": listaserializable})
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener detalle orden", "error": str(e)})
