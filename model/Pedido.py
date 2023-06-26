from bd import obtener_conexion
from datetime import datetime, timedelta, date

class Pedido:

    cont = 0

    @staticmethod
    def get_pedidos():
        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM registroPedido")
                pedidos = cursor.fetchall()

        if pedidos is None:
            return pedidos
        return Pedido.diccionario_pedidos(pedidos)
        
    
    @staticmethod
    def get_pedidos_por_dni(dni):
        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM registroPedido WHERE dniNoRegistrado = %s", (dni))
                pedidos = cursor.fetchall()
        if pedidos is None:
            return pedidos
        return Pedido.diccionario_pedidos(pedidos)
    
    @staticmethod
    def get_pedidos_por_id(id):
        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM registroPedido WHERE idUsuario = %s", (id))
                pedidos = cursor.fetchall()
        if pedidos is None:
            return pedidos
        return Pedido.diccionario_pedidos(pedidos)
    
    @classmethod
    def insertar_pedido_usuario_no_registrado( cls, dniNoRegistrado, numeroTelefono, horaRecojo, estadoBoleta, billeteraDigital):

        # with open("keyPedidos.txt", "r") as archivo:
        #     ultimalinea = archivo.readlines()[-1].strip()
        
        # if ultimalinea != "":
        #     digito = ultimalinea[4:]
        #     cls.cont = int(digito)

        cls.cont += 1
        cont = str(cls.cont)
        keyPedido = "2023" + cont

        # with open("~/web-musas/keyPedidos.txt", "w") as archivo:
        #     archivo.write(keyPedido + "\n")

        if dniNoRegistrado == "":
                return False

        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("INSERT INTO registroPedido( dniNoRegistrado, numeroTelefono, horaRecojo, fechaPedido, estadoBoleta, billeteraDigital, estadoRecojo, keyPedido) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (dniNoRegistrado, numeroTelefono, horaRecojo, date.today(), estadoBoleta, billeteraDigital, False, keyPedido))
                conexion.commit()

    @classmethod
    #mal escrito
    def insertar_peidido_usuario_registrado(cls, idUsuario,dni, numeroTelefono, horaRecojo, estadoBoleta, billeteraDigital):
        cls.cont += 1
        cont = str(cls.cont)
        keyPedido = "2023" + cont

        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("INSERT INTO registroPedido( idUsuario, dniNoRegistrado, numeroTelefono, horaRecojo, fechaPedido, estadoBoleta, billeteraDigital, estadoRecojo, keyPedido) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (idUsuario, dni, numeroTelefono, horaRecojo, datetime.now(), estadoBoleta, billeteraDigital, False, keyPedido))
                conexion.commit()

    @staticmethod
    def actualizar_estado_recojo(keyPedido):
        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT estadoRecojo FROM registroPedido WHERE keyPedido = %s and estadoRecojo = 0", (keyPedido))
                seleccion = cursor.fetchone()
            if seleccion is not None: 
                with conexion.cursor() as cursor:
                    cursor.execute("UPDATE registroPedido SET estadoRecojo = %s WHERE keyPedido = %s and estadoRecojo = 0", (True, keyPedido))
                    conexion.commit()
                    return True
            else:
                return False
    @staticmethod
    def diccionario_pedidos(pedidos):
        list = []
        for pedido in pedidos:
            diccionario = dict()
            horaRecojo = str(timedelta(seconds=pedido[6].seconds))
            fechaPedido = str(date(year=pedido[7].year, month=pedido[7].month, day=pedido[7].day))

            diccionario['idPedido'] = pedido[0]
            diccionario["idUsuario"] = pedido[1]
            diccionario["dniNoRegistrado"] = pedido[2]
            diccionario["nombres"] = pedido[3]
            diccionario["numeroTelefono"] = pedido[4]
            diccionario["estadoRecojo"] = "Recogido" if pedido[5] == 1 else "En proceso"
            diccionario["horaRecojo"] = horaRecojo
            diccionario["fechaPedido"] = fechaPedido
            diccionario["estadoBoleta"] = "Si" if pedido[9] == 1 else "No"
            diccionario["billeteraDigital"] = "Si" if pedido[10] == 1 else "No"
            diccionario["keyPedido"] = pedido[11]
            list.append(diccionario)
        return list
    

    def validar_idPedido_existente(idPedido):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            consulta = "SELECT COUNT(*) FROM registroPedido WHERE idPedido = %s"
            cursor.execute(consulta, (idPedido,))
            resultado = cursor.fetchone()
        if resultado[0] > 0:
            return True
        else:
            return False
        
    def obtener_dni_pedido(idPedido):
        conexion = obtener_conexion()
        juego = None
        with conexion.cursor() as cursor:
            cursor.execute("select idUsuario, dniNoRegistrado from registroPedido where idPedido = %s" ,(idPedido))
            juego = cursor.fetchone()
        conexion.close()
        return juego

    def obtener_id_pedido_registro():
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT coalesce(max(idPedido),0)+1 as idpedido FROM registroPedido")
            idPedido = cursor.fetchone()
        conexion.close()
        return idPedido[0]
    