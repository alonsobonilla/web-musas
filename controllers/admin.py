from flask import Blueprint, render_template, session, g
from model.Producto import Producto

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route("/")
def home():
    user = g.user
    if user is None:
        return render_template("admin/login.html")
    else:
        productos = Producto.obtener_productos()
        return render_template("admin/main.html", productos=productos, usuario=user)


@admin.before_request
def verificacion_usuario_logueado():
    user = session.get("admin.auth")
    if user is not None:
        g.user = user
