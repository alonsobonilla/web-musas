from flask import Blueprint, render_template, redirect, request, session, url_for
from model.Usuario import Usuario
usuarios = Blueprint('usuarios', __name__, url_prefix='/usuarios')


@usuarios.route("/")
def home():
    usuarios = Usuario.obtener_usuario()
    usuario = session.get("admin.auth")
    return render_template("admin/usuarios/index.html", usuarios = usuarios, usuario = usuario)

@usuarios.route("/agregar")
def form_agregar():
    usuario = session.get("admin.auth")
    return render_template("admin/usuarios/agregar.html", usuario = usuario)

@usuarios.route("/editar/<id>")
def form_editar(id):
    usuario = session.get("admin.auth")
    userUsuario = Usuario.obtener_usuario_id(id)
    return render_template("admin/usuarios/editar.html", usuario = usuario, userUsuario = userUsuario)

@usuarios.route("/actualizar", methods=["POST"])
def actualizar():
    dni = request.form["dni"]
    correo = request.form["correo"]
    numTel = request.form["telefono"]
    contra = request.form["contraseña"]
    Usuario.actualizar_usuario(correo, numTel,contra,dni, False)
    return redirect(url_for("admin.usuarios.home"))

@usuarios.route("/eliminar", methods=["POST"])
def eliminar():
    id = request.form["id"]
    Usuario.eliminar_usuario_id(id)
    return redirect(url_for("admin.usuarios.home"))

@usuarios.route("/guardar", methods=["POST"])
def guardar():
    dni = request.form["dni"]
    nombres = request.form["nombres"]
    apellidos = request.form["apellidos"]
    correo = request.form["correo"]
    numTel = request.form["telefono"]
    contra = request.form["contraseña"]
    Usuario.insertar_usuario(dni, nombres, apellidos, correo, numTel, contra, False)
    return redirect(url_for("admin.usuarios.home"))