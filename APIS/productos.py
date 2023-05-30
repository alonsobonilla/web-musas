#obtener, insertar, actualizar, eliminar, obtener por categoria, obtener por id

from flask import Blueprint
from model.Producto import Producto

api_productos = Blueprint('api_productos', __name__)

@api_productos.route("/get_productos")
def get_productos():
    return Producto.get_productos()
