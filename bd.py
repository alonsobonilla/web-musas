import pymysql, configparser

config = configparser.ConfigParser()
config.read('config.ini')

host = config.get('database', 'host')
port = int(config.get('database', 'port'))
db = config.get('database', 'database_name')
username = config.get('database','username')
password = config.get('database', 'password')

def obtener_conexion():
    return pymysql.connect(host=host, port=port, user=username, password=password, db=db)


