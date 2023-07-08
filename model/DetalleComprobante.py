from bd import obtener_conexion
from werkzeug.security import check_password_hash, generate_password_hash
from model.Producto import Producto
from model.Comprobante import Comprobante
from model.DetalleOrden import DetalleOrden
# obtener, insertar, obtener por id


class detalleComprobante:
    idComprobante = 0
    idProducto = 0
    nombreProducto = ""
    precioUnidad = 0.0
    cantidad = 0
    precioTotal = 0.0
    midic = dict()

    def __init__(self, p_idComprobante, p_idProducto, p_nombreProducto, p_precioUnidad, p_cantidad, p_precioTotal):
        self.idComprobante = p_idComprobante
        self.idProducto = p_idProducto
        self.nombreProducto = p_nombreProducto
        self.precioUnidad = p_precioUnidad
        self.cantidad = p_cantidad
        self.precioTotal = p_precioTotal
        self.midic["idComprobante"] = p_idComprobante
        self.midic["idProducto"] = p_idProducto
        self.midic["nombreProducto"] = p_nombreProducto
        self.midic["precioUnidad"] = p_precioUnidad
        self.midic["cantidad"] = p_cantidad
        self.midic["precioTotal"] = p_precioTotal

    def obtener_detalleComprobante_id(idcomprobante):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = "SELECT * FROM detalleComprobante WHERE idComprobante= %s"
            values = (idcomprobante)
            cursor.execute(query, values)
            detalleComprobante = cursor.fetchone()
        conexion.close()
        return detalleComprobante

    def obtener_detalleComprobante():
        conexion = obtener_conexion()
        detalleC = []
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM detalleComprobante")
            detalleC = cursor.fetchall()
        conexion.close()
        return detalleC
