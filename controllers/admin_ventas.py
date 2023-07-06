from flask import Blueprint, render_template, request, redirect, url_for, g
from model.Comprobante import Comprobante
ventas = Blueprint("ventas", __name__, url_prefix="/ventas")


@ventas.route("/")
def home():
    comprobantes = Comprobante.obtener_comprobante()
    return render_template("admin/ventas/index.html", comprobantes=comprobantes, usuario=g.user)


@ventas.route("detalle_comprobante/<int:idComprobante>")
def show_detalle(idComprobante):
    return render_template("admin/ventas/detalle_comprobante.html")
