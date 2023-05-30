#obtener, insertar, actualizar, eliminar, obtener por categoria, obtener por id

from flask import Blueprint, request, jsonify
from model.Producto import Producto
from model.CategoriaProducto import CategoriaProducto

api_productos = Blueprint('api_productos', __name__)

@api_productos.route("/get_productos")
def get_productos():
    return Producto.get_productos()

@api_productos.route("/insertar_producto")
def insertar_producto():
    nombre = request.json["nombre"]
    descripcion = request.json["descripcion"]
    precio = request.json["precio"]
    existencias = request.json["existencias"]
    idCategoria = request.json["idCategoria"]

    validate_idCategoria = CategoriaProducto.obtener_categoria_por_id(idCategoria)

    if validate_idCategoria is not None:
        Producto.insertar_producto(nombre, descripcion, precio, existencias, idCategoria)
        return jsonify({"Mensaje":"Producto registrado correctamente", "status:":"1"})
    
    
    
