from bd import obtener_conexion
from werkzeug.security import check_password_hash, generate_password_hash

class Autenticacion:
    @staticmethod
    def login(usuario, contraseña):
        conexion = obtener_conexion()
        error = None

        user = "SELECT * FROM usuario WHERE username = ?", (usuario).fetchone()

        if user is None :
            error = "Usuario incorrecto"
        elif not check_password_hash(user["contraseña"], contraseña):
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
                query = "INSERT INTO usuario (*) values (?, ?)"
                conexion.execute(query, (dni, nombres, apellidos,correo, fechaNacimiento, generate_password_hash(contraseña)))
                conexion.commit()
            except conexion.IntegrityError:
                error = f"Dni: {dni} ya registrado"
        return error


