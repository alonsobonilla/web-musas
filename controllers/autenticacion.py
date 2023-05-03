from flask import (
    Flask, 
    request, 
    render_template, 
    redirect, 
    Blueprint, 
    session, 
    url_for, 
    flash, g, 
    current_app
)
from model.Autenticacion import Autenticacion

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET","POST"])
def login():

    blueprint_name = request.blueprint

    if request.method == "POST":
        usuario = request.form["usuario"]
        contraseña = request.form["contraseña"]

        user = Autenticacion.login(usuario, contraseña, blueprint_name)

        if not isinstance(user, str):
            session.pop(blueprint_name, None)

            if blueprint_name == "cliente.auth":
                session[blueprint_name] = user[0]
                return redirect(url_for("cliente.home"))
            elif blueprint_name == "admin.auth":
                session[blueprint_name] = user[1]
                return redirect(url_for("admin.home"))
        else:
            flash(user)
    
    if blueprint_name == "cliente.auth":
        if g.cliente == None:
            return render_template("client/login.html")
        else:
            return render_template("client/index.html", cliente = g.cliente[0])
    elif blueprint_name == "admin.auth":
        if g.admin == None:
            return render_template("admin/login.html")
        else:
            return redirect(url_for("admin.home"))
        
    

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
            redirect(url_for("client.login"))
        else:
            flash(error) 

    blueprint_name = request.blueprint
    if blueprint_name == "cliente.auth":
        if g.cliente == None:
            return render_template("client/registro.html")
        else:
            return render_template("client/index.html", cliente = g.cliente[0])
    else:
        return redirect(url_for("admin.home"))

@auth.route("/logout")
def logout():
    blueprint_name = request.blueprint
    session.pop(blueprint_name, None)
    
    if blueprint_name == "cliente.auth":
        return redirect(url_for("cliente.home"))
    else:
        return redirect(url_for("admin.home"))
    

@auth.before_app_request
def load_logged_in_user():
    blueprint_name = request.blueprint
    user_id = session.get(blueprint_name)

    if blueprint_name == "cliente.auth":
        if user_id is None:
            g.cliente = None
        else:
            g.cliente = Autenticacion.sesionRegistrada(blueprint_name, user_id)   
    else:
        if user_id is None:
            g.admin = None
        else:
            g.admin = Autenticacion.sesionRegistrada(blueprint_name, user_id)       