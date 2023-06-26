from bd import obtener_conexion
from model.Pedido import Pedido
from model.DetalleOrden import DetalleOrden
from datetime import date, datetime, timedelta

class Comprobante:
    idComprobante = 0
    idPedido = 0
    idUsuario = ""
    dniNoRegistrado = 0
    fechaComprobante = ""
    horaComprobante = ""
    subTotal = 0  
    montoTotal = 0
    igv = 0      
    numeroComprobante = ""
    midic = dict()

    def __init__(self,p_idComprobate, p_idPedido,p_idUsuario,p_dniNoRegistrado,p_fechaComprobante,p_horaComprobante,p_subTotal,p_montoTotal,p_igv,p_numComprobante):
        self.idComprobante= p_idComprobate
        self.idPedido=p_idPedido
        self.idUsuario=p_idUsuario
        self.dniNoRegistrado=p_dniNoRegistrado
        self.fechaComprobante=p_fechaComprobante
        self.horaComprobante=p_horaComprobante
        self.subTotal=p_subTotal
        self.montoTotal=p_montoTotal
        self.igv=p_igv
        self.numeroComprobante=p_numComprobante
        self.midic["idComprobante"] = p_idComprobate
        self.midic["idPedido"]=p_idPedido
        self.midic["idUsuario"]=p_idUsuario
        self.midic["dniNoRegistrado"]=p_dniNoRegistrado
        self.midic["fechaComprobante"]=str(date(year=p_fechaComprobante.year, month=p_fechaComprobante.month, day=p_fechaComprobante.day))
        self.midic["horaComprobante"]=str(timedelta(seconds=p_horaComprobante.seconds))
        self.midic["subTotal"]=p_subTotal
        self.midic["montoTotal"]=p_montoTotal
        self.midic["igv"]=p_igv
        self.midic["numComprobante"]=p_numComprobante
 
    def obtener_comprobante():
        conexion = obtener_conexion()
        comprobantes = []
        with conexion.cursor() as cursor:
            cursor.execute("select * from comprobante")
            comprobantes = cursor.fetchall()
        conexion.close()
        return comprobantes
   
    def obtener_comprobante_idUsuario(idUsuario):
        conexion = obtener_conexion()
        juego = None
        with conexion.cursor() as cursor:
            cursor.execute("select * from comprobante where idUsuario = %s" ,(idUsuario))
            juego = cursor.fetchone()
        conexion.close()
        return juego

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

    def obtener_id_comprobante_registro():
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT coalesce(MAX(idComprobante),0)+1 as idComprobante FROM comprobante")
            idComprobante = cursor.fetchone()
        conexion.close()
        return idComprobante[0]
    
    def obtener_numero_comprobante():
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT coalesce(MAX(numeroComprobante),0)+1 as numeroComprobante FROM comprobante")
            numeroComprobante = cursor.fetchone()
        conexion.close()
        return numeroComprobante[0]