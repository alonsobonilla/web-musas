from flask import Blueprint, render_template, session, redirect, url_for
from model.Producto import Producto
from model.CategoriaProducto import CategoriaProducto
cliente = Blueprint('cliente', __name__)

@cliente.route("/")
def home():
    user = session.get("cliente.auth", None)
    categorias = CategoriaProducto.obtener_categorias()
    productos = Producto.obtener_productos_limite()
    if user:
        return render_template("client/index.html", cliente = user["nombres"], categorias = categorias, productos=productos)
    return render_template("client/index.html", categorias = categorias, productos=productos)

@cliente.route("/productos/<string:categoria>")
def productos_categoria(categoria):
    user = session.get("cliente.auth", None)
    categorias = CategoriaProducto.obtener_categorias()
    productos = Producto.getProductosCategoria(categoria)
    if user:
        return render_template("client/productos.html", cliente = user["nombres"], productos = productos, categoria = categoria, categorias = categorias)
    return render_template("client/productos.html", productos = productos, categoria = categoria, categorias = categorias)

@cliente.route("/formulario_registro_cliente")
def formulario_registro_cliente():
     return render_template("client/registro.html")

@cliente.route("/producto/<int:id>")
def comprar_producto(id):
    user = session.get("cliente.auth", None)
    producto = Producto.obtener_producto_por_id(id)
    cremas = Producto.getProductosCategoria("Cremas")
    if producto is None:
        return redirect(url_for("cliente.home"))
    if user:
        return render_template("client/seleccion-producto.html", cliente = user["nombres"], producto=producto, cremas = cremas)
    return render_template("client/seleccion-producto.html", producto=producto, cremas = cremas)

@cliente.route("/carrito")
def pag_carrito():
    user = session.get("cliente.auth", None)
    if user:
        return render_template("client/carrito.html", cliente = user["nombres"])
    return render_template("client/carrito.html")

@cliente.route("/compra")
def pag_compra():
    user = session.get("cliente.auth", None)
    if user:
        return render_template("client/compra.html", sesion = user, cliente = user["nombres"], apellidos = user["apellidos"], telefono = user["telefono"], dni= user["dni"], idUsuario = user["idUsuario"])
    return render_template("client/compra.html")
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