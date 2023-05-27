import pymysql
from cfg import*

def obtener_conexion():
    return pymysql.connect(host=host, port= port, user=username, password=password, db=db, ssl={'ssl': {'sslmode': 'require', 'ssl_ca': 'DigiCertGlobalRootCA.crt.pem'}})


