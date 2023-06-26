from flask import Blueprint, jsonify, request
from model.Transaccion import Transaccion
transaccion = Blueprint('transaccion', __name__)

@transaccion.route('/transaccion_compra', methods=['POST'])
def transaccion_compra():
    datosPedido = request.json["datosPedido"]
    productos = request.json["productos"]

    try:
        rpta = Transaccion.insertarCompra(datosPedido, productos)

        if rpta:
            return jsonify({"mensaje": "Compra registrada correctamente", "status":"1"})
    except Exception as e:
        return jsonify({"mensaje": "Error al registrar la compra", "status":"0", "error": str(e)})