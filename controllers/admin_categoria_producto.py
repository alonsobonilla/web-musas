from flask import  Blueprint, request, render_template, redirect, session, url_for, g
from controllers.admin import admin
from model.CategoriaProducto import CategoriaProducto

categoria_producto = Blueprint("categoria", __name__, url_prefix='/categorias')


@categoria_producto.route("/")
def home():
    categoria = CategoriaProducto.obtener_categorias()
    return render_template("admin/categoria/index.html", categorias=categoria, usuario = g.user)

@categoria_producto.route("/agregar")
def agregar():
    return render_template("admin/categoria/agregar.html", usuario = g.user)

@categoria_producto.route("/guardar_categoria", methods=["POST"])
def guardar():
    nombreCategoria = request.form["nombreCategoria"]
    descripcion = request.form["descripcion"]
    CategoriaProducto.insertar_categoria( nombreCategoria, descripcion)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect(url_for('admin.categoria.home'))

@categoria_producto.route("/eliminar", methods=["POST"])
def eliminar():
    CategoriaProducto.eliminar_categoria(request.form["idCategoria"])
    return redirect(url_for("admin.categoria.home"))

@categoria_producto.route("/editar_categoria/<int:id>")
def editar(id):
    # Obtener el categoria por ID
    categoria = CategoriaProducto.obtener_categoria_por_id(id)
    return render_template("admin/categoria/editar.html", categoria=categoria, usuario = g.user)

@categoria_producto.route("/actualizar", methods=["POST"])
def actualizar():
    id = request.form["idCategoria"]
    nombreCategoria = request.form["nombreCategoria"]
    descripcion = request.form["descripcion"]
    CategoriaProducto.actualizar_categoria( nombreCategoria, descripcion, id)
    return redirect(url_for("admin.categoria.home"))

@categoria_producto.before_request
def verificacion_usuario_logueado():
    user_id = session.get("admin.auth")

    if user_id is None:
        return redirect(url_for("admin.home"))
    else:
        g.user = user_id
