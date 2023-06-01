#insertar, obtener por dni, obtener todos
from flask import Blueprint, request, jsonify
from model.Pedido import Pedido
from model.Usuario_cliente import Usuario_cliente

api_registro_pedidos = Blueprint('api_registro_pedidos', __name__)

@api_registro_pedidos.route('/obtener_pedidos', methods=['GET'])
def obtener_pedidos():
    try:
        pedidos = Pedido.get_pedidos()
        return jsonify({'message': 'Pedidos obtenidos correctamente', 'status':'1','pedidos': pedidos})
    except Exception as ex:
        return jsonify({'message': 'Error al obtener los pedidos', 'status':'0', 'error':str(ex)})

@api_registro_pedidos.route('/obtener_pedidos_por_dni', methods=['POST'])
def obtener_pedidos_por_dni():
    try:
        dni = request.json['dni']
        pedidos = Pedido.get_pedidos_por_dni(dni)
        return jsonify({'message': 'Pedidos obtenidos correctamente', 'status':'1','pedidos': pedidos})
    except Exception as ex:
        return jsonify({'message': 'Error al obtener los pedidos', 'status':'0', 'error':str(ex)})

@api_registro_pedidos.route('/insertar_pedido', methods=['POST'])
def insertar_pedido():
    try:
        dniUsuario = request.json['dniUsuario']
        dniNoRegistrado = request.json['dniNoRegistrado'].strip()
        numeroTelefono = request.json['numeroTelefono']
        horaRecojo = request.json['horaRecojo']
        estadoBoleta = request.json['estadoBoleta']
        billeteraDigital = request.json['billeteraDigital']
        
        validate_dni = Usuario_cliente.obtener_usuario_dni(dniUsuario)
        if validate_dni is not None:
            Pedido.insertar_peidido_usuario_registrado( dniUsuario, numeroTelefono, horaRecojo, estadoBoleta, billeteraDigital)
        else:
            Pedido.insertar_pedido_usuario_no_registrado( dniNoRegistrado, numeroTelefono, horaRecojo, estadoBoleta, billeteraDigital)
        
        return jsonify({'message': 'Pedido registrado correctamente', 'status':'1'})
    except Exception as ex:
        return jsonify({'message': 'Error al registrar el pedido', 'status':'0', 'error':str(ex)})

@api_registro_pedidos.route('/actualizar_estado_recojo', methods=['POST'])
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