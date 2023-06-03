#insertar, eliminar, obtener, actualizar, obtener por id
from flask import jsonify, Blueprint, request
from model.CategoriaProducto import CategoriaProducto


api_categoriaProducto = Blueprint('api_categoriaProducto',__name__)


@api_categoriaProducto.route("/api_obtenercategorias")
def api_obtenercategorias():
    try:
        categorias=CategoriaProducto.obtener_categorias()
        listaserializable = []
        for categoria in categorias:
            miobj = CategoriaProducto(categoria[0],categoria[1],categoria[2])
            listaserializable.append(miobj.midic.copy())
        return jsonify({"Mensaje":"Categorias obtenidas correctamente", "status:":"1", "Categoria":listaserializable})
    
    except:
        return jsonify ({"Mensaje":"Error al obtener categoria"})


@api_categoriaProducto.route("/api_eliminarcategoria")
def api_eliminarcategoria():
    try:
        CategoriaProducto.eliminar_categoria(request.json["idCategoria"])
        return jsonify({"Mensaje": "Categoria elimada correctamente", "status:":"1"})
        return
    except:
        return jsonify({"Mensaje":"Error al eliminar categoria"})
   
@api_categoriaProducto.route("/api_insertarcategoria", methods=["POST"])
def api_insertarcategoria():
    try:
        nombre = request.json["nombreCategoria"]
        descripcion = request.json["descripcion"]
        CategoriaProducto.insertar_categoria(nombre,descripcion)
        return jsonify({"Mensaje":"Categoria registrada correctamente", "status:":"1"})
    except:
        return jsonify({"Mensaje":"Error al registrar categoria"})
   
@api_categoriaProducto.route("/api_actualizarcategoria")
def api_actualizarcategoria():
    try:
        idCategoria = request.json["idCategoria"]
        nombre = request.json["nombreCategoria"]
        descripcion = request.json["descripcion"]
        CategoriaProducto.actualizar_categoria(nombre,descripcion,idCategoria)    
        return jsonify({"Mensaje":"Categoria actualizada correctamente", "status:":"1"})
    except:
        return jsonify({"Mensaje":"Error al actualizar categoria", "status:":"0"})


@api_categoriaProducto.route("/api_obtenercategoriaid/<int:idCategoria>")
def api_obtenercategoriaid(idCategoria):
    try:
        categorias=CategoriaProducto.obtener_categoria_por_id(idCategoria)
        listaserializable = []
        miobj = CategoriaProducto(categorias[0],categorias[1],categorias[2])
        listaserializable.append(miobj.midic.copy())
        return jsonify({"Mensaje":"Categoria obtenida correctamente", "status:":"1", "categoria":listaserializable})
    except:
        return jsonify ({"Mensaje":"Error al obtener categoria", "status:":"0"})

