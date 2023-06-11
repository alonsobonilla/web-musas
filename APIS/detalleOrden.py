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
            miobj = DetalleOrden(deO[0],deO[1],deO[2],deO[3],deO[4],deO[5])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener detalles orden", "error": str(e)})


@api_detalleOrden.route("/api_guardardetalleorden", methods=["POST"])
@jwt_required()
def api_guardardetalleOrden():
    try:
        idproducto = request.json["idproducto"]
        idpedido = request.json["idpedido"]
        cantidad = request.json["cantidad"]

        validar_idPedido = Pedido.validar_idPedido_existente(idpedido)
        validar_idProducto = Producto.obtener_producto_por_id(idproducto)

        if validar_idProducto is None:
            return jsonify({"Mensaje": "El producto no existe"})
        elif not validar_idPedido:
            return jsonify({"Mensaje": "El idpedido no existe"})
        else:
            DetalleOrden.insertar_detalleOrden(idproducto, idpedido, cantidad)
            return jsonify({"Mensaje": "DetalleOrden registrado correctamente"})
    except Exception as e:
        return jsonify({"mensaje": "Error al guardar detalle orden", "error": str(e)})

@api_detalleOrden.route("/api_obtenerdetalleorden/<int:idproducto>/<int:idpedido>")
@jwt_required()
def api_obtenedetalleorden(idproducto,idpedido):
    try:
        listaserializable = []
        deO = DetalleOrden.obtener_detalleOrden_id(idproducto,idpedido)
        validar_idPedido = Pedido.validar_idPedido_existente(idpedido)
        validar_idProducto = Producto.obtener_producto_por_id(idproducto)
        

        if validar_idProducto is None:
            return jsonify({"Mensaje": "El producto no existe"})
        elif not validar_idPedido:
            return jsonify({"Mensaje": "El pedido no existe"})
        elif deO is None:
            return jsonify({"Mensaje": "El detalle de orden no existe"})
        else:
            listaserializable = []
            miobj = DetalleOrden(deO[0],deO[1],deO[2],deO[3],deO[4],deO[5])
            listaserializable.append(miobj.midic.copy())
            return jsonify(listaserializable)
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener detalle orden", "error": str(e)})
