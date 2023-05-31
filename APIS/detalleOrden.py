#obtener, insertar, obtener por id

from flask import jsonify, Blueprint, request
from model.DetalleOrden import DetalleOrden

api_detalleOrden = Blueprint('api_detalleOrden',__name__)
@api_detalleOrden.route("/api_obtener_detalleorden")

def api_obtenerusuarios():
    try:
        detallesorden = DetalleOrden.obtener_detalleOrden()
        listaserializable = []
        for deO in detallesorden:
            miobj = DetalleOrden(deO[0],deO[1],deO[2],deO[3],deO[4],deO[5])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify ({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

#def 



#def
 