from flask import Blueprint, render_template
from model.Producto import Producto

cliente = Blueprint('cliente', __name__)

@cliente.route("/")
def home():
#     # simples = Producto.getProductosTipo(1)
#     # mixtas = Producto.getProductosTipo(2)
#     # alopobres = Producto.getProductosTipo(3)
#     # especiales = Producto.getProductosTipo(4)
    return render_template("client/index.html")
#     # , simples = simples, mixtas = mixtas, alopobres = alopobres, especiales = especiales)

@cliente.route("/<tipo>")
def verMas(tipo):
    productos = []
    if tipo == "simples":
        productos = Producto.getProductosTipo(1)
    elif tipo == "mixtas":
        productos = Producto.getProductosTipo(2)
    elif tipo == "alopobre":
        productos = Producto.getProductosTipo(3)
    elif tipo == "especiales":
        productos = Producto.getProductosTipo(4)
    
    return render_template("client/verMas.html", productos = productos)