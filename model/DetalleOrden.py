from bd import obtener_conexion
from werkzeug.security import check_password_hash, generate_password_hash
from model.Producto import Producto
from model.Pedido import Pedido
#obtener, insertar, obtener por id
class DetalleOrden:
    idProducto = 0
    idPedido = 0
    nombreProducto = ""
    precioUnidad = 0.0
    cantidad = 0
    precioTotal = 0.0
    midic = dict()

    def __init__(self,p_idProducto,p_idPedido,p_nombreProducto,p_precioUnidad,p_cantidad,p_precioTotal):
        self.idProducto= p_idProducto
        self.idPedido = p_idPedido
        self.nombreProducto = p_nombreProducto
        self.precioUnidad = p_precioUnidad
        self.cantidad = p_cantidad
        self.precioTotal = p_precioTotal
        self.midic["idProducto"] = p_idProducto
        self.midic["idPedido"] = p_idPedido
        self.midic["nombreProducto"] = p_nombreProducto
        self.midic["precioUnidad"] = p_precioUnidad
        self.midic["cantidad"] = p_cantidad
        self.midic["precioTotal"] = p_precioTotal

    def insertar_detalleOrden(idproducto,idpedido,cantidad):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = "INSERT INTO detalleOrden VALUES (%s, %s, %s, %s, %s, %s)"
            nomP =Producto.obtener_producto_por_id(idproducto)["nombre"]
            precioU = Producto.obtener_producto_por_id(idproducto)["precio"]
            precioT = cantidad * precioU
            values = (idproducto,idpedido,nomP,precioU,cantidad,precioT)
            cursor.execute(query, values)
        conexion.commit()
        conexion.close()


    def obtener_detalleOrden():
        conexion = obtener_conexion()
        detalleOrden = []
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM detalleOrden")
            detalleOrden = cursor.fetchall()
        conexion.close()
        return detalleOrden


    def obtener_detalleOrden_id(idproducto,idpedido):
        conexion = obtener_conexion()
        modo=None
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idProducto,idPedido,nombreProducto,precioUnidad,cantidad,precioTotal FROM detalleOrden WHERE idproducto=%s AND idpedido=%s",(idpedido,idproducto,))
            modo = cursor.fetchone()
        conexion.close()
        return modo

    def obtener_subTotal(idPedido):
        conexion = obtener_conexion()
        juego = None
        with conexion.cursor() as cursor:
            cursor.execute("select precioTotal from detalleOrden where idPedido = %s", (idPedido))
            juego = cursor.fetchone()
        conexion.close()
        subTotal = 0
        for j in juego:
            subTotal += j[0]
        return subTotal
    
    