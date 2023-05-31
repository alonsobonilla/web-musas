from bd import obtener_conexion
from werkzeug.security import check_password_hash, generate_password_hash

class Usuario:
    idAdmin = 0
    usuario = ""
    contraseña = ""
    diccionario = dict()

    def __init__(self, idAdmin, usuario, contraseña):
        self.idAdmin = idAdmin
        self.usuario = usuario
        self.contraseña = contraseña
        self.diccionario["usuario"] = usuario
        self.diccionario["contraseña"] = contraseña
        self.diccionario["idAdmin"] = idAdmin

    @staticmethod
    def get_usuarios():
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM usuarioAdmin")
            usuarios = cursor.fetchall()
        conexion.close()
        return usuarios
    
    @staticmethod
    def insert_usuario(usuario, contraseña):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO usuarioAdmin (usuario, contraseña) VALUES (%s, %s)", (usuario, generate_password_hash(contraseña)))
        conexion.commit()
        conexion.close()

    @staticmethod
    def delete_usuario(id):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM usuarioAdmin WHERE idAdmin = %s", (id))
        conexion.commit()
        conexion.close()

    @staticmethod
    def get_usuario(id):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idAdmin, usuario, contraseña FROM usuarioAdmin WHERE idAdmin = %s", (id))
            usuario = cursor.fetchone()
        conexion.close()
        return usuario
    
    @staticmethod
    def get_username(nombre):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idAdmin,usuario, contraseña FROM usuarioAdmin WHERE usuario = %s", (nombre))
            usuario = cursor.fetchone()
        conexion.close()
        return usuario

    @staticmethod
    def update_usuario(usuario, contraseña):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE usuarioAdmin SET contraseña = %s WHERE usuario = %s", ( generate_password_hash(contraseña), usuario))
        conexion.commit()
        conexion.close()