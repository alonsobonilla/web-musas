from bd import obtener_conexion
from model.Pedido import Pedido
from model.DetalleOrden import DetalleOrden
from datetime import time, datetime
class Transaccion:
    conteo = 0
    @classmethod
    def insertarCompra(cls, datosPedido, productos):

        idUsuario = datosPedido["idUsuario"]
        dniNoRegistrado = datosPedido["dniNoRegistrado"]
        numeroTelefono = datosPedido["telefono"]
        nombres = datosPedido["nombres"]
        horaRecojo = datetime.strptime(datosPedido["horaRecojo"], "%H:%M").time() 
        estadoBoleta = datosPedido["estadoBoleta"]
        billeteraDigital = datosPedido["billeteraDigital"]
    
        if idUsuario == "":
            queryPedido = "INSERT INTO registroPedido(idPedido,dniNoRegistrado, nombres, numeroTelefono, horaRecojo, estadoBoleta, billeteraDigital, keyPedido) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        else:
            queryPedido = "INSERT INTO registroPedido(idPedido, idUsuario, dniNoRegistrado, nombres, numeroTelefono, horaRecojo,estadoBoleta, billeteraDigital, keyPedido) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)"
        
        queryDetalleOrden = "INSERT INTO detalleOrden(idDetalleOrden, idPedido, idProducto, nombreProducto, precioUnidad, cantidad, preciototal) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        queryDetalleCremas = "INSERT INTO detalleCremas(idPedido, idCrema, idDetalleOrden) VALUES (%s, %s, %s)"

        cls.conteo += 1
        cont = str(cls.conteo)
        keyPedido = "2023" + cont

        idPedido = Pedido.obtener_id_pedido_registro()
        idDetalleOrden = DetalleOrden.obtener_id_detalle_orden_registro()
        try:

            conexion = obtener_conexion()
            with conexion.cursor() as cursor:
                if idUsuario == "":
                    cursor.execute(queryPedido, (idPedido, dniNoRegistrado, nombres, numeroTelefono, horaRecojo, estadoBoleta, billeteraDigital, keyPedido))
                else:
                    cursor.execute(queryPedido, (idPedido, idUsuario, dniNoRegistrado, nombres, numeroTelefono, horaRecojo, estadoBoleta, billeteraDigital, keyPedido))
            with conexion.cursor() as cursor:
                for producto in productos:
                    idProducto = producto["idProducto"]
                    nombreProducto = producto["nombre"]
                    precioUnidad = producto["precio"]
                    cantidad = producto["cantidad"]
                    precioTotal = producto["precioTotal"]
                    cremas = producto["cremas"]
    
                    cursor.execute(queryDetalleOrden, (idDetalleOrden, idPedido, idProducto, nombreProducto, precioUnidad, cantidad, precioTotal))
                with conexion.cursor() as cursor:
                    for crema in cremas:
                        idCrema = crema
                        cursor.execute(queryDetalleCremas,(idPedido, idCrema, idDetalleOrden))
            conexion.commit()
            return True   
        except Exception as e:
            conexion.rollback()
            raise e
        finally:
            conexion.close()