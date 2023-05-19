from bd import obtener_conexion
from werkzeug.security import check_password_hash, generate_password_hash

class Autenticacion:

    diccionario_tipo = {
        "cliente.auth": {
            "tabla": "usuario",
            "columna": "dni"
        },
        "admin.auth": {
            "tabla": "usuarioAdmin",
            "columna": "usuario"
        }
    }

    @staticmethod
    def login(usuario, contraseña, tipo_blueprint):
        conexion = obtener_conexion()
        error = None
        cursor = conexion.cursor()

        tipo = Autenticacion.diccionario_tipo[tipo_blueprint]
        tabla = tipo["tabla"]
        columna = tipo["columna"]
        
        query = f"SELECT * FROM {tabla} WHERE {columna} = %s"
        cursor.execute(query, (usuario))
        user = cursor.fetchall()
        cursor.close()

        if user is None or user.__len__() == 0:
            error = "Usuario incorrecto"
        elif ( tabla == "usuario" and not check_password_hash(user[0][2], contraseña) ) or user[0][2] != contraseña:
            error = "Contraseña incorrecta"
        else:
            error = user

        return error

    @staticmethod
    def registro(dni, nombres, apellidos, correo, fechaNacimiento, contraseña):
        conexion = obtener_conexion()
        error = None

        if not dni or not nombres or not apellidos or not correo or not fechaNacimiento or not contraseña:
            error = "Campos obligatorios"
        else:
            try:
                query = "INSERT INTO usuario (*) values (%s, %s, %s, %s, %s, %s)"
                cursor = conexion.cursor()
                cursor.execute(query, (dni, nombres, apellidos,correo, fechaNacimiento, generate_password_hash(contraseña)))
                conexion.commit()
            except conexion.IntegrityError:
                error = f"Dni: {dni} ya registrado"            
        return error

    @staticmethod
    def sesionRegistrada(blueprint_name, id_sesion):

        conexion = obtener_conexion()

        tabla = Autenticacion.diccionario_tipo[blueprint_name]["tabla"]
        columna = Autenticacion.diccionario_tipo[blueprint_name]["columna"]

        query = f"SELECT * FROM {tabla} WHERE {columna} = %s"
        cursor = conexion.cursor()
        cursor.execute(query, (id_sesion))
        user = cursor.fetchall()
        cursor.close()

        return user[0]