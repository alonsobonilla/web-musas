from flask import Blueprint, render_template, request, redirect, session, url_for, g
from model.Producto import Producto

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/")
def home():
    user_id = session.get("admin.auth")

    if user_id is None:
        return render_template("admin/login.html")
    else:
        productos = Producto.obtener_productos()
        return render_template("admin/index.html", productos=productos, usuario = user_id)

@admin.route("/agregar_producto")
def formulario_agregar_producto():
    return render_template("admin/agregar_producto.html")


@admin.route("/guardar_producto", methods=["POST"])
def guardar_producto():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    existencias = request.form["existencias"]
    Producto.insertar_producto( nombre, descripcion, precio, existencias)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/")

@admin.route("/eliminar_producto", methods=["POST"])
def eliminar_producto():
    Producto.eliminar_producto(request.form["id"])
    return redirect("/")


@admin.route("/formulario_editar_producto/<int:id>")
def editar_producto(id):
    # Obtener el disco por ID
    producto = Producto.obtener_producto_por_id(id)
    return render_template("admin/editar_producto.html", producto=producto)


@admin.route("/actualizar_producto", methods=["POST"])
def actualizar_producto():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    existencias = request.form["existencias"]
    Producto.actualizar_producto(nombre, descripcion, precio, existencias, id)
    return redirect("/")


