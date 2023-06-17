#insertar, obtener  (id comprobante , id producto)

from flask import jsonify, Blueprint, request
from model.DetalleComprobante import detalleComprobante
from model.Producto import Producto
from model.Comprobante import Comprobante

api_detalleComprobante = Blueprint('api_detalleComprobante',__name__)
@api_detalleComprobante.route("/api_obtenerdetalleComprobante")

def api_obtenerdetallecomprobante():
    try:
        detalleC = detalleComprobante.obtener_detalleComprobante()
        listaserializable = []
        for deC in detalleC:
            miobj = detalleComprobante(deC[0],deC[1],deC[2],deC[3],deC[4],deC[5])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify ({"Mensaje":"Error al obtener detalle de comprobante"})


@api_detalleComprobante.route("/api_guardardetalleComprobante", methods=["POST"])
def api_guardardetalleComprobante():
    try:
        idcomprobante = request.json["idComprobante"]
        idproducto = request.json["idProducto"]
        cantidad = request.json["cantidad"]
        validar_idProducto = Producto.obtener_producto_por_id(idproducto)
        validar_idComprobante = Comprobante.validar_idComprobante_existente(idcomprobante)

        if validar_idProducto == None or validar_idComprobante == None:
            return jsonify ({"Mensaje":"Error al guardar detalle de comprobante No existe el producto o el comprobante"})
        
        detalleComprobante.insertar_detalleComprobante(idcomprobante,idproducto,cantidad)
        return jsonify({"Mensaje":"Detalle Comprobante registrado correctamente"})
    except:
        return jsonify({"Mensaje":"Error al insertar detalle de comprobante"})


@api_detalleComprobante.route("/api_obtenerdetalleComprobante/<int:idcomprobante>/<int:idproducto>")
def api_obtenerdetalleComprobante(idcomprobante,idproducto):
    try:
        deC = detalleComprobante.obtener_detalleComprobante_id(idcomprobante,idproducto)
        validar_idProducto = Producto.obtener_producto_por_id(idproducto)
        validar_Comprobante = Comprobante.validar_idComprobante_existente(idcomprobante)
        listaserializable = []

        if validar_idProducto is None:
            return jsonify({"Mensaje": "El producto no existe"})
        elif not validar_Comprobante:
            return jsonify({"Mensaje": "El Comprobante no existe"})
        elif deC is None:
              return jsonify({"Mensaje": "El detalle de comprobante no existe"})
        else:
            miobj = detalleComprobante(deC[0],deC[1],deC[2],deC[3],deC[4],deC[5])
            listaserializable.append(miobj.midic.copy())
            return jsonify(listaserializable)
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener detalle orden", "error": str(e)})



