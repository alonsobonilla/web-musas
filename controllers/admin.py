from flask import Blueprint, render_template, request, redirect, flash, jsonify
from model.Producto import Producto

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/")
def home():
    productos = Producto.obtener_productos()
    return render_template("admin/productos.html", productos=productos)

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


