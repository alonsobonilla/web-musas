from flask import Blueprint, render_template, request, redirect, url_for, g
from flask_paginate import Pagination, get_page_parameter
from model.Comprobante import Comprobante
from model.DetalleComprobante import detalleComprobante
from model.Pedido import Pedido
ventas = Blueprint("ventas", __name__, url_prefix="/ventas")


@ventas.route("/")
def home():
    search = False
    q = request.args.get('q')
    if q:
        search = True

    comprobantesTotal = Comprobante.obtener_total()
    per_page = 9
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start_index = (page - 1) * per_page + 1

    pagination = Pagination(page=page, total=comprobantesTotal, per_page=per_page,
                            search=search)

    comprobantes = Comprobante.obtener_comprobantes_paginacion(
        per_page, start_index)
    return render_template("admin/ventas/index.html", comprobantes=comprobantes, usuario=g.user, pagination=pagination)


@ventas.route("detalle_comprobante/<int:idComprobante>")
def show_detalle(idComprobante):
    info_comprobante = Comprobante.obtener_comprobante_id(idComprobante)
    detalles_productos = detalleComprobante.obtener_detalleComprobante_id(
        idComprobante)
    idPedido = info_comprobante[1]
    datos_comprobante = Pedido.get_pedido_por_id_pedido(idPedido)

    forma_pago = datos_comprobante[9]
    nombre_forma = "Efectivo"
    if forma_pago == 1:
        nombre_forma = "Billetera digital"

    return render_template("admin/ventas/detalle_comprobante.html", usuario=g.user, productos=detalles_productos, comprobante=info_comprobante, pedido=datos_comprobante, forma_pago=nombre_forma)
