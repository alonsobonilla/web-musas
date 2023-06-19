#insertar, obtener por (idpedido, idproducto, idcrema
from flask import Blueprint, request, jsonify
from flask_jwt import jwt_required
from model.DetalleCremas import DetalleCremas
from model.Pedido import Pedido
from model.Producto import Producto


api_detalleCremas = Blueprint('api_detalleCremas', __name__)

@api_detalleCremas.route("/insertar_detalleCrema", methods = ["POST"])

def insertar_detalleCremas():
    try:
        idPedido = request.json["idPedido"]
        idProducto = request.json["idProducto"]
        idCrema = request.json["idCrema"]
        catProducto = Producto.obtener_producto_por_id(idCrema)["nombreCategoria"]
        if catProducto == "Cremas":
            DetalleCremas.insertar_detalleCremas(idPedido,idProducto,idCrema)
            return jsonify({"Mensaje":"Detalle crema registrada correctamente", "status:":"1"})
        return jsonify({"Mensaje":"El idCrema no corresponde a la categoria cremas", "Status":"0"})
    except Exception as ex:
        return jsonify({"Mensaje":"Error al registrar detalle crema", "Status":"0", "errror":str(ex)})

@api_detalleCremas.route("/obtener_detalleCremas/<int:idPedido>/<int:idProducto>")

def obtener_detalleCremas(idPedido,idProducto):
    try:
        detalleCrema = DetalleCremas.obtener_detalleCremas_idPedido(idPedido,idProducto)
        lista = []
        for detalle in detalleCrema:
            lista.append(DetalleCremas(detalle[0],detalle[1],detalle[2],detalle[3]).midic.copy())
            return jsonify({"Mensaje":"Detalle crema obtenida correctamente", "status:":"1", "Detalle crema":lista})
        return jsonify({"Mensaje":"El detalle crema no existe", "Status":"0"})
    except Exception as ex:
        return jsonify({"Mensaje":"Error al obtener detalle crema", "status:":"0", "errror":str(ex)})
