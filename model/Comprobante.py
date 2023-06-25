from bd import obtener_conexion
from model.Pedido import Pedido
from model.DetalleOrden import DetalleOrden
from model.Usuario import Usuario
import datetime

class Comprobante:
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

    def __init__(self,p_idPedido,p_idUsuario,p_dniNoRegistrado,p_fechaComprobante,p_horaComprobante,p_subTotal,p_montoTotal,p_igv,p_numComprobante):
        self.idPedido=p_idPedido
        self.idUsuario=p_idUsuario
        self.dniNoRegistrado=p_dniNoRegistrado
        self.fechaComprobante=p_fechaComprobante
        self.horaComprobante=p_horaComprobante
        self.subTotal=p_subTotal
        self.montoTotal=p_montoTotal
        self.igv=p_igv
        self.numeroComprobante=p_numComprobante
        self.midic["idPedido"]=p_idPedido
        self.midic["idUsuario"]=p_idUsuario
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
        idUsuario = Pedido.obtener_dni_pedido(idPedido)[0]
        dniNoRegistrado = Pedido.obtener_dni_pedido(idPedido)[1]
        subTotal = DetalleOrden.obtener_subTotal(idPedido)
        igv = 0.18
        montoTotal = subTotal + (subTotal*igv)
        igv = subTotal*igv
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = "insert into comprobante(idPedido,idUsuario,dniNoRegistrado,fechaComprobante,horaComprobante, subTotal,igv,montoTotal,numeroComprobante) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (idPedido,idUsuario,dniNoRegistrado,fecha_actual,hora_actual, subTotal,igv,montoTotal,numComprobante)
            cursor.execute(query, values)
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
