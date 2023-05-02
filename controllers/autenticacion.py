from flask import Flask, request, render_template, redirect, Blueprint, session, url_for, flash
from model.Autenticacion import Autenticacion

auth = Blueprint("auth", __name__, url_prefix = "/auth")

@auth.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contraseña = request.form["contraseña"]
        
        user = Autenticacion.login(usuario, contraseña)
        
        if not isinstance(user, str):
            session.clear()
            session["user_id"] = user["dni"]
            
            if(user["tipo_user"] == "admin"):
                return redirect(url_for("admin.home"))
            else:
                return redirect(url_for("cliente.home"))
        else:
            flash(user) 
    return render_template("auth/login.html")

@auth.route("/registro", methods = ["GET","POST"])
def registro():
    if request.method == "POST":
        dni = request.form["dni"]
        nombres = request.form["nombres"]
        apellidos = request.form["apellido"]
        correo = request.form["correo"]
        fechaNacimiento = request.form["fecha_nacimiento"]
        contraseña = request.form["contraseña"]

        error = Autenticacion.registro(dni, nombres, apellidos, correo, fechaNacimiento, contraseña)

        if error is None:
            redirect(url_for("auth.login"))
        else:
            flash(error)
    return render_template("auth/registro.html")


@auth.before_app_request
def load_logged_in_user():
    user_id =session.get("user_id")

    # if user_id is None:
    #     g.user = None
    # else:
    #     g.user = 