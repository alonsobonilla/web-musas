from bd import obtener_conexion
from werkzeug.security import check_password_hash, generate_password_hash


class Usuario:
    DNI = ""
    nombres = ""
    apellidos = ""
    correo = ""
    numTel = ""
    contraseña = ""
    tipoUsuario = ""
    midic = dict()

    def __init__(self, p_DNI, p_nombres, p_apellidos, p_correo, p_numTel, p_contraseña, p_tipoUsuario):
        self.DNI = p_DNI
        self.nombres = p_nombres
        self.apellidos = p_apellidos
        self.correo = p_correo
        self.numTel = p_numTel
        self.midic["DNI"] = p_DNI
        self.midic["nombres"] = p_nombres
        self.midic["apellidos"] = p_apellidos
        self.midic["correo"] = p_correo
        self.midic["numTel"] = p_numTel
        self.midic["contraseña"] = p_contraseña
        if p_tipoUsuario:
            self.tipoUsuario = "Cliente"
        else:
            self.tipoUsuario = "Admin"

        self.midic["tipoUsuario"] = self.tipoUsuario

    def insertar_usuario(DNI, nombres, apellidos, correo, numTel, contra, tipoUsuario):
        user = Usuario.obtener_usuario_dni_tipo(DNI, tipoUsuario)
        error = None
        if user is None:
            conexion = obtener_conexion()
            with conexion.cursor() as cursor:
                cursor.execute("INSERT INTO usuario(DNI, nombres, apellidos, correo, numTelf,contraseña, tipoUsuario) VALUES (%s, %s, %s, %s, %s, %s, %s)", (
                    DNI, nombres, apellidos, correo, numTel, contra, tipoUsuario))
            conexion.commit()
            conexion.close()
        else:
            error = "Usuario ya registrado"
        return error

    def obtener_usuarios():
        conexion = obtener_conexion()
        usuarios = []
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM usuario where tipoUsuario = %s", (False))
            usuarios = cursor.fetchall()
        conexion.close()
        return usuarios

    def obtener_usuario_id(id):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM usuario WHERE idUsuario = %s", (id))
            usuario = cursor.fetchone()
        return usuario

    def obtener_usuario_id_tipo(id, tipoUsuario):
        conexion = obtener_conexion()
        modo = None
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT DNI,nombres,apellidos,correo, numTelf, contraseña, tipoUsuario FROM usuario WHERE idUsuario= %s and tipoUsuario = %s", (id, tipoUsuario))
            modo = cursor.fetchone()
        conexion.close()
        return modo

    def actualizar_usuario(correo, numTel, contra, id, tipo):
        if correo is "":
            correo = Usuario.obtener_usuario_id_tipo(id, tipo)[3]
        elif numTel is "":
            numTel = Usuario.obtener_usuario_id_tipo(id, tipo)[4]
        elif contra is "":
            contra = Usuario.obtener_usuario_id_tipo(id, tipo)[5]
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE usuario SET correo = %s, numTelf= %s, contraseña= %s WHERE idUsuario=%s and tipoUsuario = %s",
                           (correo, numTel, contra, id, tipo))
        conexion.commit()
        conexion.close()

    def eliminar_usuario(dni, tipoUsuario):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute(
                "DELETE FROM usuario WHERE DNI = %s and tipoUsuario = %s", (dni, tipoUsuario))
        conexion.commit()
        conexion.close()

    def eliminar_usuario_id(id):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM usuario WHERE idUsuario = %s", (id))
        conexion.commit()
        conexion.close()

    def obtener_usuario_dni_tipo(dni, tipo):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM usuario WHERE DNI = %s and tipoUsuario = %s", (dni, tipo))
            usuario = cursor.fetchone()
        return usuario

    def validar_usuario_id(id):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM usuario WHERE idUsuario = %s", (id,))
            resultado = cursor.fetchone()
        conexion.close()
        if resultado[0] > 0:
            return True
        
    def obtener_usuarios_jwt():
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idUsuario, dni, contraseña FROM usuario")
            usuarios = cursor.fetchall()
        conexion.close()
        return usuarios
