from bd import obtener_conexion
from werkzeug.security import check_password_hash, generate_password_hash

class Autenticacion:

    diccionario_tipo = {
        "cliente.auth": {
            "tipoUsuario": True
        },
        "admin.auth": {
            "tipoUsuario": False
        }
    }

    @staticmethod
    def login(dni, contraseña, tipo_blueprint):
        conexion = obtener_conexion()
        error = None
        cursor = conexion.cursor()

        tipo = Autenticacion.diccionario_tipo[tipo_blueprint]
        tipoUsuario = tipo["tipoUsuario"]
        
        with conexion.cursor() as cursor:
            query = f"SELECT * FROM usuario WHERE dni = %s and tipoUsuario = %s"
            cursor.execute(query, (dni, tipoUsuario))
            user = cursor.fetchall()

        if user is None or user.__len__() == 0:
            error = "Usuario incorrecto"
        elif (check_password_hash(user[0][6], contraseña) ) or user[0][6] != contraseña:
            error = "Contraseña incorrecta"
        else:
            error = user

        return error

    @staticmethod
    def registro(dni, nombres, apellidos, correo, numTelf, contraseña):
        conexion = obtener_conexion()
        error = None

        if not dni or not nombres or not apellidos or not correo or not numTelf or not contraseña:
            error = "Campos obligatorios"
        else:
            try:
                query = "INSERT INTO usuario (dni,nombres,apellidos,correo,numTelf,contraseña,tipoUsuario) values (%s, %s, %s, %s, %s, %s,%s)"
                cursor = conexion.cursor()
                cursor.execute(query, (dni, nombres, apellidos,correo, numTelf, generate_password_hash(contraseña), True))
                conexion.commit()
            except conexion.IntegrityError:
                error = f"Dni: {dni} ya registrado"            
        return error

    @staticmethod
    def sesionRegistrada(blueprint_name, dni):

        conexion = obtener_conexion()

        tipoUsuario = Autenticacion.diccionario_tipo[blueprint_name]["tipoUsuario"]

        with conexion.cursor() as cursor:
            query = f"SELECT * FROM usuario WHERE dni = %s and tipoUsuario = %s"
            cursor = conexion.cursor()
            cursor.execute(query, (dni, tipoUsuario))
            user = cursor.fetchall()

        return user[0]