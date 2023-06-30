from flask import Blueprint, render_template, request, redirect, session, url_for, g
from model.Producto import Producto

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/")
def home():
    user = session.get("admin.auth", None)
    if user is None:
        return render_template("admin/login.html")
    else:
        productos = Producto.obtener_productos()
        return render_template("admin/main.html", productos=productos, usuario = user)
