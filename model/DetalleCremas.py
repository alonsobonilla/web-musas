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
          
    # def insertar_detalleCremas(idPedido,idCrema,idDetalleOrden):
    #     conexion = obtener_conexion()
    #     with conexion.cursor() as cursor:
    #         query = "insert into detalleCremas values (%s,%s,%s)"
    #         values = (idPedido,idCrema,idDetalleOrden)
    #         cursor.execute(query,values)
    #     conexion.commit()
    #     conexion.close()
       
    def obtener_detalleCremas_idPedido(idPedido):
        conexion = obtener_conexion()
        juego = None
        with conexion.cursor() as cursor:
            cursor.execute("select * from detalleCremas where idPedido = %s ", (idPedido))
            juego = cursor.fetchone()
        conexion.close()
        return juego
