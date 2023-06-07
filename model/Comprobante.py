from bd import obtener_conexion

class comprobante:
    idComprobante = 0
    idPedido = 0 
    dniUsuario = 0
    dniNoRegistrado = 0
    fechaComprobante = 0
    horaComprobante = 0
    subTotal = 0  
    montoTotal = 0 
    igv = 0       
    numeroComprobante = 0
    @staticmethod
   
        

    def validar_idComprobante_existente(idComprobante):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            consulta = "SELECT COUNT(*) FROM comprobante WHERE idComprobante = %s"
            cursor.execute(consulta, (idComprobante,))
            resultado = cursor.fetchone()
        if resultado[0] > 0:
            return True
        else:
            return False
