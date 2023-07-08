# insertar, obtener por (idpedido, idproducto, idcrema
from flask import Blueprint, request, jsonify
from flask_jwt import jwt_required
from model.DetalleCremas import DetalleCremas
from model.Pedido import Pedido
from model.Producto import Producto


api_detalleCremas = Blueprint('api_detalleCremas', __name__)


@api_detalleCremas.route("/obtener_detalleCremas/<int:idPedido>/<int:idDetalleOrden>")
@jwt_required()
def obtener_detalleCremas(idPedido, idDetalleOrden):
    try:
        detalleCrema = DetalleCremas.obtener_detalleCremas_idPedido(
            idPedido, idDetalleOrden)
        lista = []
        if detalleCrema is not None:
            for detalle in detalleCrema:
                lista.append(DetalleCremas(
                    detalle[0], detalle[1], detalle[2]).midic.copy())
                return jsonify({"Mensaje": "Detalle crema obtenida correctamente", "status:": "1", "Detalle crema": lista})
        return jsonify({"Mensaje": "El detalle crema no existe", "Status": "0"})
    except Exception as ex:
        return jsonify({"Mensaje": "Error al obtener detalle crema", "status:": "0", "error": str(ex)})
