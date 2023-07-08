# insertar, obtener todos, obtener por dni
from flask import Blueprint, request, jsonify
from flask_jwt import jwt_required
from model.DetalleOrden import DetalleOrden
from model.Comprobante import Comprobante
from model.Usuario import Usuario

api_comprobante = Blueprint('api_comprobante', __name__)


@api_comprobante.route("/obtener_comprobantes")
@jwt_required()
def obtener_comprobante():
    try:
        comprobantes = Comprobante.obtener_comprobante()
        listaComprobante = []
        for comprobante in comprobantes:
            miobj = Comprobante(comprobante[0], comprobante[1], comprobante[2], comprobante[3], comprobante[4],
                                comprobante[5], comprobante[6], comprobante[7], comprobante[8], comprobante[9])
            listaComprobante.append(miobj.midic.copy())
        return jsonify({"Mensaje": "Comprobantes encontrados", "Comprobantes": listaComprobante})
    except Exception as e:
        return jsonify({"Mensaje": "Error al obtener comprobante", "error": str(e)})


@api_comprobante.route('/obtener_comprobante_cliente/<int:id>')
@jwt_required()
def obtener_comprobante_cliente(id):
    try:
        validarUsuario = Usuario.validar_usuario_id(id)

        if validarUsuario:
            comprobantes = Comprobante.obtener_comprobante_idUsuario(id)
            lista = []
            if comprobantes is not None:
                for comprobante in comprobantes:
                    miobj = Comprobante(comprobante[0], comprobante[1], comprobante[2], comprobante[3], comprobante[4],
                                        comprobante[5], comprobante[6], comprobante[7], comprobante[8], comprobante[9])
                    lista.append(miobj.midic.copy())
                return jsonify({"Mensaje": "Comprobante obtenido correctamente", "status:": "1", "Comprobante:": lista})
            return jsonify({"Mensaje": "No se encontro comprobante", "status": "0"})
        return jsonify({"Mensaje": "Usuario no existe", "status": "0"})
    except Exception as e:
        return jsonify({"Mensaje": "Error al obtener comprobante", "status": "0", "error": str(e)})
