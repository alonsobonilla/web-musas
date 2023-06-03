#obtener, insertar, actualizar, eliminar, obtener por categoria, obtener por id

from flask import Blueprint, request, jsonify
from flask_jwt import jwt_required
from model.Producto import Producto
from model.CategoriaProducto import CategoriaProducto

api_productos = Blueprint('api_productos', __name__)

@api_productos.route("/get_productos")
@jwt_required()
def get_productos():
    productos = Producto.obtener_productos()
    return jsonify({"Mensaje":"Productos obtenidos correctamente", "status:":"1", "productos":productos})

@api_productos.route("/get_producto/<int:id>")
@jwt_required()
def get_producto(id):
    try:
        producto = Producto.obtener_producto_por_id(id)
        if producto is not None:
            return jsonify({"Mensaje":"Producto obtenido correctamente", "status:":"1", "producto":producto})
        return jsonify({"Mensaje":"No existe el producto", "status:":"0"})
    except Exception as ex:
        return jsonify({"Mensaje":"Error al obtener el producto", "status:":"0", "errror":str(ex)})

@api_productos.route("/get_productos_categoria/<int:id>")
@jwt_required()
def get_productos_tipo(id):
    try:
        validate_idCategoria = CategoriaProducto.obtener_categoria_por_id(id)

        if validate_idCategoria is not None:
            productos = Producto.getProductosCategoria(id)
            if productos is not None:
                return jsonify({"Mensaje":"Productos obtenidos correctamente", "status:":"1", "productos":productos})
            return jsonify({"Mensaje":"No existen productos", "status:":"0"})
        return jsonify({"Mensaje":"No existe la categoria", "status:":"0"})
    except Exception as ex:
        return jsonify({"Mensaje":"Error al obtener los productos", "status:":"0", "errror":str(ex)})

@api_productos.route("/insertar_producto", methods=["POST"])
@jwt_required()
def insertar_producto():
    try:
        nombre = request.json["nombre"]
        descripcion = request.json["descripcion"]
        precio = request.json["precio"]
        existencias = request.json["existencias"]
        idCategoria = request.json["idCategoria"]

        validate_idCategoria = CategoriaProducto.obtener_categoria_por_id(idCategoria)

        if validate_idCategoria is not None:
            validate_insert = Producto.insertar_producto(nombre, descripcion, precio, existencias, idCategoria)
            if validate_insert == False:
                return jsonify({"Mensaje":"Todos los campos obligatorios", "status:":"0"})
            return jsonify({"Mensaje":"Producto registrado correctamente", "status:":"1"})
        return jsonify({"Mensaje":"No existe la categoria", "status:":"0"})
    except Exception as ex: 
        return jsonify({"Mensaje":"Error al registrar el producto", "status:":"0", "errror":str(ex)})
    
    
@api_productos.route("/actualizar_producto", methods=["POST"])
@jwt_required()
def actualizar_producto():
    try:
        idProducto = request.json["idProducto"]
        nombre = request.json["nombre"]
        descripcion = request.json["descripcion"]
        precio = request.json["precio"]
        existencias = request.json["existencias"]
        idCategoria = request.json["idCategoria"]

        validate_idProducto = Producto.obtener_producto_por_id(idProducto)
        if validate_idProducto is not None:
            
            if idCategoria != "":
                validate_idCategoria = CategoriaProducto.obtener_categoria_por_id(idCategoria)
                if validate_idCategoria is not None:
                    Producto.actualizar_producto(nombre, descripcion, precio, existencias,idProducto, idCategoria)
                else:
                    return jsonify({"Mensaje":"No existe la categoría", "status:":"0"})  
            else:
                Producto.actualizar_producto(nombre, descripcion, precio, existencias,idProducto, idCategoria)
            return jsonify({"Mensaje":"Producto actualizado correctamente", "status:":"1"})
        return jsonify({"Mensaje":"No existe el producto", "status:":"0"})
    except Exception as ex:
        return jsonify({"Mensaje":"Error al actualizar el producto", "status:":"0", "errror":str(ex)})

@api_productos.route("/eliminar_producto/", methods=["POST"])
@jwt_required()
def eliminar_producto():
    try:
        idProducto = request.json["idProducto"]
        producto = Producto.obtener_producto_por_id(idProducto)
        if producto is not None:
            Producto.eliminar_producto(idProducto)
            return jsonify({"Mensaje":"Producto eliminado correctamente", "status:":"1"})
        return jsonify({"Mensaje":"No existe el producto", "status:":"0"})
    except Exception as ex:
        return jsonify({"Mensaje":"Error al eliminar el producto", "status:":"0", "errror":str(ex)})
