#insertar, obtener por dni, obtener todos
from flask import Blueprint, request, jsonify
from flask_jwt import jwt_required
from model.Pedido import Pedido
from model.Usuario import Usuario

api_registro_pedidos = Blueprint('api_registro_pedidos', __name__)

@api_registro_pedidos.route('/obtener_pedidos', methods=['GET'])
@jwt_required()
def obtener_pedidos():
    try:
        pedidos = Pedido.get_pedidos()
        return jsonify({'message': 'Pedidos obtenidos correctamente', 'status':'1','pedidos': pedidos})
    except Exception as ex:
        return jsonify({'message': 'Error al obtener los pedidos', 'status':'0', 'error':str(ex)})

@api_registro_pedidos.route('/obtener_pedidos_por_dni/<string:dni>')
@jwt_required()
def obtener_pedidos_por_dni(dni):
    try:
        usuario = Usuario.obtener_usuario_dni_tipo(dni, True)

        if usuario is not None:
            idUsuario = usuario[0]
            pedidos = Pedido.get_pedidos_por_id(idUsuario)
        else:
            pedidos = Pedido.get_pedidos_por_dni(dni)
        
        if pedidos is not None:
            return jsonify({'message': 'Pedidos obtenidos correctamente', 'status':'1','pedidos': pedidos})
        return jsonify({'message': 'No se encontraron pedidos', 'status':'0'})
    except Exception as ex:
        return jsonify({'message': 'Error al obtener los pedidos', 'status':'0', 'error':str(ex)})

@api_registro_pedidos.route('/insertar_pedido', methods=['POST'])
@jwt_required()
def insertar_pedido():
    try:
        idUsuario = request.json['idUsuario']
        dniNoRegistrado = request.json['dniNoRegistrado'].strip()
        numeroTelefono = request.json['numeroTelefono']
        horaRecojo = request.json['horaRecojo']
        estadoBoleta = request.json['estadoBoleta']
        billeteraDigital = request.json['billeteraDigital']
        
        validate_dni = Usuario.obtener_usuario_id_tipo(idUsuario, True)
        if validate_dni is not None:
            dni = validate_dni[0]
            Pedido.insertar_peidido_usuario_registrado( idUsuario, dni, numeroTelefono, horaRecojo, estadoBoleta, billeteraDigital)
        else:
            Pedido.insertar_pedido_usuario_no_registrado( dniNoRegistrado, numeroTelefono, horaRecojo, estadoBoleta, billeteraDigital)
        
        return jsonify({'message': 'Pedido registrado correctamente', 'status':'1'})
    except Exception as ex:
        return jsonify({'message': 'Error al registrar el pedido', 'status':'0', 'error':str(ex)})

@api_registro_pedidos.route('/actualizar_estado_recojo', methods=['POST'])
@jwt_required()
def actualizar_estado_recojo():
    try:
        keyPedido = request.json['keyPedido']
        validate = Pedido.actualizar_estado_recojo(keyPedido)
        if validate == True:
            return jsonify({'message': 'Estado de recojo actualizado correctamente', 'status':'1'})
        else:
            return jsonify({'message': 'keyPedido incorrecta', 'status':'0'})
    except Exception as ex:
        return jsonify({'message': 'Error al actualizar el estado de recojo', 'status':'0', 'error':str(ex)})