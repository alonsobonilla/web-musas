from flask import Blueprint, render_template, session
from model.Pedido import Pedido
pedidos = Blueprint("pedido", __name__, url_prefix="/pedidos")

@pedidos.route("/")
def home():
    user = session.get("admin.auth")
    pedidos = Pedido.get_pedidos()
    return render_template("admin/pedidos/index.html", usuario = user, pedidos = pedidos)