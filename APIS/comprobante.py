#insertar, obtener todos, obtener por dni
from flask import Blueprint, request, jsonify
from flask_jwt import jwt_required
from model.Pedido import Pedido
from model.DetalleOrden import DetalleOrden
from model.Comprobante import Comprobante

api_comprobante = Blueprint('api_comprobante', __name__)


@api_comprobante.route('/insertar_comprobante', methods=['POST'])
def insertar_comprobante():
    try:
        idPedido = request.json["idPedido"]
        numComprobante = request.json["numComprobante"]


        Comprobante.insertar(idPedido, numComprobante)
        return jsonify({"Mensaje":"Comprobante registrado correctamente", "status:":"1"})
    except Exception as ex:
        return jsonify({"Mensaje":"Error al registrar el Comprobante", "status:":"0", "errror":str(ex)})
   


@api_comprobante.route("/obtener_comprobante")
def obtener_comprobante():
    try:
        comprobantes = Comprobante.obtener_comprobante()
        listaComprobante = []
        for comprobante in comprobantes:
            miobj = Comprobante(comprobante[0], comprobante[1], comprobante[2], comprobante[3], comprobante[4], comprobante[5], comprobante[6], comprobante[7], comprobante[8], comprobante[9])
            listaComprobante.append(miobj)
        return jsonify({"Mensaje": "Comprobantes encontrados", "Comprobantes": listaComprobante})
    except Exception as e:
        return jsonify({"Mensaje": "Error al obtener comprobante", "errror": str(e)})

@api_comprobante.route('/obtener_comprobante_id')
def obtener_comprobante():
    try:
        comprobante