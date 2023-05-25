from flask import Blueprint, render_template, redirect, request, session, url_for, g
from controllers.admin import admin
from model.Producto import Producto
from model.CategoriaProducto import CategoriaProducto

productos = Blueprint("productos", __name__, url_prefix='/productos')

@productos.route("/")
def home():
    usuario = session.get("admin.auth")
    productos = Producto.obtener_productos()
    return render_template("admin/productos/index.html", productos = productos, usuario = usuario)

@productos.route("/agregar_producto")
def formulario_agregar():
    usuario = session.get("admin.auth")
    nombreCategorias = CategoriaProducto.obtener_categorias()
    return render_template("admin/productos/agregar_producto.html", categorias = nombreCategorias, usuario = usuario)

@productos.route("/guardar_producto", methods=["POST"])
def guardar():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    existencias = request.form["existencias"]
    Producto.insertar_producto( nombre, descripcion, precio, existencias)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/")

@productos.route("/eliminar_producto", methods=["POST"])
def eliminar():
    Producto.eliminar_producto(request.form["id"])
    return redirect("/")


@productos.route("/formulario_editar_producto/<int:id>")
def editar(id):
    # Obtener el disco por ID
    producto = Producto.obtener_producto_por_id(id)
    return render_template("admin/productos/editar_producto.html", producto=producto)


@productos.route("/actualizar_producto", methods=["POST"])
def actualizar():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    existencias = request.form["existencias"]
    Producto.actualizar_producto(nombre, descripcion, precio, existencias, id)
    return redirect("/")


@productos.before_request
def verificacion_usuario_logueado():
    user_id = session.get("admin.auth")

    if user_id is None:
        return redirect(url_for("admin.home"))
