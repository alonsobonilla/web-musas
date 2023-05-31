from flask import (
    Flask, 
    request, 
    render_template, 
    redirect, 
    Blueprint, 
    session, 
    url_for, 
    flash,
    current_app,
    g
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
                session[blueprint_name] = user[0][1]
                return redirect(url_for("admin.home"))
        else:
            flash(user)
    
    if blueprint_name == "cliente.auth":
        return render_template("client/index.html", cliente = g.cliente[0])
    elif blueprint_name == "admin.auth":
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
