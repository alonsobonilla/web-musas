from bd import obtener_conexion
from model.Pedido import Pedido
from model.Producto import Producto

class DetalleCremas:
    idPedido = 0
    idProducto = 0
    idCrema = 0
    midic = dict()
   
    def __init__(self, p_idPedido, p_idProducto, p_idCrema):
        self.idPedido = p_idPedido
        self.idProducto = p_idProducto
        self.idCrema = p_idCrema
        self.midic["idPedido"] = p_idPedido
        self.midic["idProducto"] = p_idProducto
        self.midic["idCrema"] = p_idCrema
       
    def insertar_detalleCremas(idPedido,idProducto,idCrema):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = "insert into detalleCremas values (%s,%s,%s)"
            values = (idPedido,idProducto,idCrema)
        conexion.commit()
        conexion.close()
       
    def obtener_detalleCremas_idPedido(idPedido,idProducto):
        conexion = obtener_conexion()
        juego = None
        with conexion.cursor() as cursor:
            cursor.execute("select * from detalleCremas where idPedido = %s and idProducto =%s", (idPedido,idProducto))
            juego = cursor.fetchone()
        conexion.close()
        return juego
