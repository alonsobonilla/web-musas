from flask import Blueprint, render_template, redirect, request, session, url_for
from model.Usuario import Usuario
usuarios = Blueprint('usuarios', __name__, url_prefix='/usuarios')


@usuarios.route("/")
def home():
    usuarios = Usuario.get_usuarios()
    usuario = session.get("admin.auth")
    return render_template("admin/usuarios/index.html", usuarios = usuarios, usuario = usuario)

@usuarios.route("/agregar")
def form_agregar():
    usuario = session.get("admin.auth")
    return render_template("admin/usuarios/agregar.html", usuario = usuario)

@usuarios.route("/editar/<id>")
def form_editar(id):
    usuario = session.get("admin.auth")
    userUsuario = Usuario.get_usuario(id)
    return render_template("admin/usuarios/editar.html", usuario = usuario, userUsuario = userUsuario)

@usuarios.route("/eliminar", methods=["POST"])
def eliminar():
    id = request.form["id"]
    Usuario.delete_usuario(id)
    return redirect(url_for("admin.usuarios.home"))

@usuarios.route("/guardar", methods=["POST"])
def guardar():
    usuario = request.form["nombreUsuario"]
    contraseña = request.form["contraseña"]
    Usuario.insert_usuario(usuario, contraseña)
    return redirect(url_for("admin.usuarios.form_agregar"))