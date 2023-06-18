from flask import Blueprint, render_template, session, request
from model.Producto import Producto
from model.CategoriaProducto import CategoriaProducto
cliente = Blueprint('cliente', __name__)

@cliente.route("/")
def home():
    user = session.get("cliente.auth", None)
    categorias = CategoriaProducto.obtener_categorias()

#     # simples = Producto.getProductosTipo(1)
#     # mixtas = Producto.getProductosTipo(2)
#     # alopobres = Producto.getProductosTipo(3)
#     # especiales = Producto.getProductosTipo(4)
    return render_template("client/index.html", cliente = user, categorias = categorias)
#     # , simples = simples, mixtas = mixtas, alopobres = alopobres, especiales = especiales)

@cliente.route("/productos/<string:categoria>")
def productos_categoria(categoria):
    user = session.get("cliente.auth", None)
    productos = Producto.getProductosCategoria(categoria)
    return render_template("client/productos.html", cliente = user, productos = productos, categoria = categoria)

@cliente.route("/formulario_registro_cliente")
def formulario_registro_cliente():
     return render_template("client/registro.html")



# @cliente.route("/<tipo>")
# def verMas(tipo):
#     productos = []
#     if tipo == "simples":
#         productos = Producto.getProductosTipo(1)
#     elif tipo == "mixtas":
#         productos = Producto.getProductosTipo(2)
#     elif tipo == "alopobre":
#         productos = Producto.getProductosTipo(3)
#     elif tipo == "especiales":
#         productos = Producto.getProductosTipo(4)
    
#     return render_template("client/verMas.html", productos = productos)