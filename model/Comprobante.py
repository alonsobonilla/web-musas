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
    def insertar_comprobante()