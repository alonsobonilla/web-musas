from bd import obtener_conexion
from model.Pedido import Pedido
from model.Usuario import Usuario
import datetime

class comprobante:
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

    def insertar_comprobante(idComprobante,idPedido,dniNoRegistrado,subTotal,montoTotal,igv,numComprobante):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = "insert into comprobante values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            fecha_actual = datetime.date.today()
            hora_actual = datetime.datetime.now().time()
            values = (idComprobante,idPedido,dniNoRegistrado,)

