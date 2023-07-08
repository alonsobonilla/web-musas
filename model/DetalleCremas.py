from bd import obtener_conexion
from model.Pedido import Pedido
from model.Producto import Producto


class DetalleCremas:
    idPedido = 0
    idCrema = 0
    idDetalleOrden = 0
    midic = dict()

    def __init__(self, p_idPedido, p_idCrema, p_idDetalleOrden):
        self.idPedido = p_idPedido
        self.idCrema = p_idCrema
        self.idDetalleOrden = p_idDetalleOrden
        self.midic["idPedido"] = p_idPedido
        self.midic["idCrema"] = p_idCrema
        self.midic["idDetalleOrden"] = p_idDetalleOrden

    def obtener_detalleCremas_idPedido(idPedido, idDetalleOrden):
        conexion = obtener_conexion()
        juego = None
        with conexion.cursor() as cursor:
            cursor.execute(
                "select * from detalleCremas where idPedido = %s and idDetalleOrden = %s", (idPedido, idDetalleOrden))
            juego = cursor.fetchall()
        conexion.close()
        return juego

    def obtner_detalle_cremas_pedidos_recoger():
        conexion = obtener_conexion()
        detalleCremas = []
        with conexion.cursor() as cursor:
            cursor.execute("select dc.*, pr.nombre from detalleCremas dc inner join producto pr on dc.idCrema = pr.idProducto where dc.idDetalleOrden = (select dor.idDetalleOrden from detalleOrden dor where dor.idPedido = (select rp.idPedido from registroPedido rp where rp.estadoRecojo = false and rp.fechaPedido = (select current_date()) and rp.idPedido = dor.idPedido order by rp.horaRecojo) and dor.idDetalleOrden = dc.idDetalleOrden);")
            detalleCremas = cursor.fetchall()
        conexion.close()
        return detalleCremas
