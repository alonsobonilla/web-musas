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
            diccionario["estadoBoleta"] = "Si" if pedido[8] == 1 else "No"
            diccionario["billeteraDigital"] = "Si" if pedido[9] == 1 else "No"
            diccionario["keyPedido"] = pedido[10]
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
    
    def validate_key_pedido(idPedido, keyPedido):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT keyPedido FROM registroPedido WHERE idPedido = %s and keyPedido = %s", (idPedido, keyPedido))
            key = cursor.fetchone()
        conexion.close()
        if key is None:
            return False
        return True
    def get_pedidos_ordenados_horarios():
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("select * from registroPedido where estadoRecojo = false and fechaPedido = (select current_date()) order by horaRecojo;")
            pedidos = cursor.fetchall()
        conexion.close()
        return Pedido.diccionario_pedidos(pedidos)
    