from flask import Blueprint, jsonify, request
from model.Transaccion import Transaccion
from flask_jwt import jwt_required
transaccion = Blueprint('transaccion', __name__)

@transaccion.route('/transaccion_compra', methods=['POST'])
@jwt_required()
def transaccion_compra():
    datosPedido = request.json["datosPedido"]
    productos = request.json["productos"]

    try:
        rpta = Transaccion.insertarCompra(datosPedido, productos)

        if rpta:
            return jsonify({"mensaje": "Compra registrada correctamente", "status":"1"})
    except Exception as e:
        return jsonify({"mensaje": "Error al registrar la compra", "status":"0", "error": str(e)})

@transaccion.route('/transaccion_comprobante', methods=['POST'])
@jwt_required()
def transaccion_comprobante():
    idPedido = request.json["idPedido"]
    keyPedido = request.json["keyPedido"]
    try:
        rpta = Transaccion.insertarComprobante(idPedido, keyPedido)
        if rpta:
            return jsonify({"mensaje": "Comprobante registrado correctamente", "status":"1"})
        return jsonify({"mensaje": "KeyPedido incorrecto", "status":"0"})
    except Exception as e:
        return jsonify({"mensaje": "Error al registrar el comprobante", "status":"0", "error": str(e)})