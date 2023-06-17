from bd import obtener_conexion
from model.Pedido import Pedido
from model.DetalleOrden import DetalleOrden
from model.Usuario import Usuario
import datetime

class Comprobante:
    idComprobante = 0
    idPedido = 0
    dniUsuario = ""
    dniNoRegistrado = 0
    fechaComprobante = ""
    horaComprobante = ""
    subTotal = 0  
    montoTotal = 0
    igv = 0      
    numeroComprobante = ""
    midic = dict()


    def __init__(self,p_idComprobante,p_idPedido,p_dniUsuario,p_dniNoRegistrado,p_fechaComprobante,p_horaComprobante,p_subTotal,p_montoTotal,p_igv,p_numComprobante):
        self.idComprobante=p_idComprobante
        self.idPedido=p_idPedido
        self.dniUsuario=p_dniUsuario
        self.dniNoRegistrado=p_dniNoRegistrado
        self.fechaComprobante=p_fechaComprobante
        self.horaComprobante=p_horaComprobante
        self.subTotal=p_subTotal
        self.montoTotal=p_montoTotal
        self.igv=p_igv
        self.numeroComprobante=p_numComprobante
        self.midic["idComprobante"]=p_idComprobante
        self.midic["idPedido"]=p_idPedido
        self.midic["dniUsuario"]=p_dniUsuario
        self.midic["dniNoRegistrado"]=p_dniNoRegistrado
        self.midic["fechaComprobante"]=p_fechaComprobante
        self.midic["horaComprobante"]=p_horaComprobante
        self.midic["subTotal"]=p_subTotal
        self.midic["montoTotal"]=p_montoTotal
        self.midic["igv"]=p_igv
        self.midic["numComprobante"]=p_numComprobante


    def insertar_comprobante(idPedido,numComprobante):
        fecha_actual = datetime.date.today()
        hora_actual = datetime.datetime.now().time()
        dniUsuario = Pedido.obtener_dni_pedido(idPedido)[0]
        dniNoRegistrado = Pedido.obtener_dni_pedido(idPedido)[1]
        subTotal = DetalleOrden.obtener_subTotal(idPedido)
        igv = 0.18
        montoTotal = subTotal + (subTotal*igv)
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = "insert into comprobante(idPedido,dniUsuario,dniNoRegistrado,fechaComprobante,horaComprobante, subTotal,igv,montoTotal,numeroComprobante) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(query, (idPedido,dniUsuario,dniNoRegistrado,fecha_actual,hora_actual, subTotal,igv,montoTotal,numComprobante))
        conexion.commit()
        conexion.close()
 
    def obtener_comprobante():
        conexion = obtener_conexion()
        comprobantes = []
        with conexion.cursor() as cursor:
            cursor.execute("select * from comprobante")
            comprobantes = cursor.fetchall()
        conexion.close()
        return comprobantes
   
    def obtener_comprobante_dni(idUsuario):
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
