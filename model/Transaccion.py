from bd import obtener_conexion
from model.Pedido import Pedido
from model.DetalleOrden import DetalleOrden
from model.Comprobante import Comprobante
from model.Pedido import Pedido
from datetime import time, datetime, date


class Transaccion:
    conteo = 0

    @classmethod
    def insertarCompra(cls, datosPedido, productos):

        idUsuario = datosPedido["idUsuario"]
        dniNoRegistrado = datosPedido["dniNoRegistrado"]
        numeroTelefono = datosPedido["telefono"]
        nombres = datosPedido["nombres"]
        horaRecojo = datetime.strptime(
            datosPedido["horaRecojo"], "%H:%M").time()
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
                    cursor.execute(queryPedido, (idPedido, dniNoRegistrado, nombres,
                                   numeroTelefono, horaRecojo, estadoBoleta, billeteraDigital, keyPedido))
                else:
                    cursor.execute(queryPedido, (idPedido, idUsuario, dniNoRegistrado, nombres,
                                   numeroTelefono, horaRecojo, estadoBoleta, billeteraDigital, keyPedido))
            with conexion.cursor() as cursor:
                for producto in productos:
                    idProducto = producto["idProducto"]
                    nombreProducto = producto["nombre"]
                    precioUnidad = producto["precio"]
                    cantidad = producto["cantidad"]
                    precioTotal = producto["precioTotal"]
                    cremas = producto["cremas"]

                    cursor.execute(queryDetalleOrden, (idDetalleOrden, idPedido,
                                   idProducto, nombreProducto, precioUnidad, cantidad, precioTotal))
                    for crema in cremas:
                        idCrema = crema
                        cursor.execute(queryDetalleCremas,
                                       (idPedido, idCrema, idDetalleOrden))
                    idDetalleOrden += 1

            conexion.commit()
            return True
        except Exception as e:
            conexion.rollback()
            raise e
        finally:
            conexion.close()

    def insertarComprobante(idPedido, keyPedido):
        datosPedido = Pedido.obtener_dni_pedido(idPedido)
        idUsuario = datosPedido[0]
        dniNoRegistrado = datosPedido[1]
        idComprobante = Comprobante.obtener_id_comprobante_registro()
        fechaComprobante = date.today()
        horaComprobante = datetime.now().time()
        subTotal = DetalleOrden.obtener_subTotal(idPedido)
        base = subTotal/1.18
        igv = subTotal-base
        montoTotal = subTotal
        numComprobante = Comprobante.obtener_numero_comprobante()
        ordenes = DetalleOrden.obtener_detalle_orden_id_pedido(idPedido)

        queryComprobante = "INSERT INTO comprobante(idComprobante, idPedido, idUsuario, dniNoRegistrado, fechaComprobante, horaComprobante, subTotal, montoTotal, igv, numeroComprobante) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        queryDetalleComprobante = "INSERT INTO detalleComprobante(idComprobante, idProducto, nombreProducto, precioUnidad, cantidad, precioTotal) VALUES (%s, %s, %s, %s, %s, %s)"

        validateKey = Pedido.validate_key_pedido(idPedido, keyPedido)
        if not validateKey:
            return False
        try:
            conexion = obtener_conexion()
            with conexion.cursor() as cursor:
                cursor.execute(queryComprobante, (idComprobante, idPedido, idUsuario, dniNoRegistrado,
                               fechaComprobante, horaComprobante, subTotal, montoTotal, igv, numComprobante))

            with conexion.cursor() as cursor:
                for orden in ordenes:
                    idProducto = orden[2]
                    nombreProducto = orden[3]
                    precioUnidad = orden[4]
                    cantidad = orden[5]
                    precioTotal = orden[6]
                    try:
                        cursor.execute(queryDetalleComprobante, (idComprobante, idProducto,
                                       nombreProducto, precioUnidad, cantidad, precioTotal))
                    except:
                        cursor.execute(
                            "select cantidad,precioTotal from detalleComprobante where idComprobante = %s and idProducto = %s", (idComprobante, idProducto))
                        data = cursor.fetchone()
                        cantidad += data[0]
                        precioTotal += data[1]
                        cursor.execute("update detalleComprobante set cantidad = %s, precioTotal = %s where idComprobante = %s and idProducto = %s", (
                            cantidad, precioTotal, idComprobante, idProducto))
            with conexion.cursor() as cursor:
                cursor.execute(
                    "UPDATE registroPedido SET estadoRecojo = %s WHERE idPedido = %s", (True, idPedido))
            conexion.commit()
            return True
        except Exception as e:
            conexion.rollback()
            raise e
        finally:
            conexion.close()
