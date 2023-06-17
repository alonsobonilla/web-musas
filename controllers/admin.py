from flask import Blueprint, render_template, request, redirect, session, url_for, g
from model.Producto import Producto

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/")
def home():
    nombre = session.get("admin.auth")
    if nombre is None:
        return render_template("admin/login.html")
    else:
        productos = Producto.obtener_productos()
        return render_template("admin/main.html", productos=productos, usuario = nombre)
