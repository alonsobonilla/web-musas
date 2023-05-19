import pymysql, configparser
from config import*

def obtener_conexion():
    if port == '' :
        return pymysql.connect(host=host, user=username, password=password, db=db)
    else:
        return pymysql.connect(host=host, port= port, user=username, password=password, db=db)


