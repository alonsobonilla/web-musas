from bd import obtener_conexion
from werkzeug.security import check_password_hash, generate_password_hash
from model.Producto import Producto
from model.Pedido import Pedido
#obtener, insertar, obtener por id
class DetalleOrden:
    idDetalleOrden = 0
    idProducto = 0
    idPedido = 0
    nombreProducto = ""
    precioUnidad = 0.0
    cantidad = 0
    precioTotal = 0.0
    midic = dict()

    def __init__(self,p_idDetalleOrden,p_idProducto,p_idPedido,p_nombreProducto,p_precioUnidad,p_cantidad,p_precioTotal):
        self.idDetalleOrden = p_idDetalleOrden
        self.idProducto= p_idProducto
        self.idPedido = p_idPedido
        self.nombreProducto = p_nombreProducto
        self.precioUnidad = p_precioUnidad
        self.cantidad = p_cantidad
        self.precioTotal = p_precioTotal
        self.midic["idDetalleOrden"] = p_idDetalleOrden
        self.midic["idProducto"] = p_idProducto
        self.midic["idPedido"] = p_idPedido
        self.midic["nombreProducto"] = p_nombreProducto
        self.midic["precioUnidad"] = p_precioUnidad
        self.midic["cantidad"] = p_cantidad
        self.midic["precioTotal"] = p_precioTotal

    def obtener_detalleOrden():
        conexion = obtener_conexion()
        detalleOrden = []
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM detalleOrden")
            detalleOrden = cursor.fetchall()
        conexion.close()
        return detalleOrden


    def obtener_detalleOrden_id(idDetalleOrden,idpedido):
        conexion = obtener_conexion()
        modo=None
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idProducto,idPedido,nombreProducto,precioUnidad,cantidad,precioTotal FROM detalleOrden WHERE idPedido = %s AND idDetalleOrden=%s",(idpedido,idDetalleOrden))
            modo = cursor.fetchone()
        conexion.close()
        return modo

    def obtener_subTotal(idPedido):
        conexion = obtener_conexion()
        juego = None
        with conexion.cursor() as cursor:
            cursor.execute("select precioTotal from detalleOrden where idPedido = %s", (idPedido))
            juego = cursor.fetchall()
        conexion.close()
        subTotal = 0
        for j in juego:
            subTotal += j[0]
        return subTotal
    
    def obtener_id_detalle_orden_registro():
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("select coalesce(max(idDetalleOrden),0)+1 as iddetalleorden from detalleOrden")  
            fila = cursor.fetchone()
        conexion.close()
        return fila[0]
    
    def obtener_detalle_orden_id_pedido(idPedido):
        conexion = obtener_conexion()
        detalleOrden = []
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM detalleOrden WHERE idPedido = %s",(idPedido))
            detalleOrden = cursor.fetchall()
        conexion.close()
        return detalleOrden

    def obtener_detalle_orden_pedidos_recoger():
        conexion = obtener_conexion()
        detalleOrden = []
        with conexion.cursor() as cursor:
            cursor.execute("select * from detalleOrden dor where dor.idPedido = (select idPedido from registroPedido where estadoRecojo = false and fechaPedido = (select current_date()) and idPedido = dor.idPedido  order by horaRecojo);")
            detalleOrden = cursor.fetchall()
        conexion.close()
        return detalleOrden