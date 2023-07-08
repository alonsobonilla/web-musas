from flask import Blueprint, render_template, g, request
from flask_paginate import Pagination, get_page_parameter
from model.Pedido import Pedido
from model.DetalleOrden import DetalleOrden
from model.DetalleCremas import DetalleCremas
pedidos = Blueprint("pedidos", __name__, url_prefix="/pedidos")


@pedidos.route("/")
def home():
    search = False
    q = request.args.get('q')
    if q:
        search = True

    pedidosT = Pedido.total()
    per_page = 4
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start_index = (page - 1) * per_page + 1

    pagination = Pagination(page=page, total=pedidosT, per_page=per_page,
                            search=search)
    pedidos = Pedido.get_pedidos_ordenados_horarios(per_page, start_index)
    detalleOrdenes = DetalleOrden.obtener_detalle_orden_pedidos_recoger()
    detalleCremas = DetalleCremas.obtner_detalle_cremas_pedidos_recoger()
    listaOrdenes = []
    for do in detalleOrdenes:
        obj = DetalleOrden(do[0], do[2], do[1], do[3], do[4], do[5], do[6])
        listaOrdenes.append(obj.midic.copy())
    return render_template("admin/pedidos/index.html", usuario=g.user, pedidos=pedidos, ordenes=listaOrdenes, cremas=detalleCremas, pagination=pagination)
