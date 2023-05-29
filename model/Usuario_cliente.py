from bd import obtener_conexion

class Usuario_cliente:
    DNI = ""
    nombres = ""
    apellidos = ""
    correo = ""
    numTel = ""
    fechaNac =  ""
    midic   = dict()


    def __init__(self,p_DNI,p_nombres,p_apellidos,p_correo,p_numTel,p_fechaNac):
        self.DNI = p_DNI
        self.nombres = p_nombres
        self.apellidos = p_apellidos
        self.correo = p_correo
        self.numTel = p_numTel
        self.fechaNac = p_fechaNac
        self.midic["DNI"] = p_DNI
        self.midic["nombres"] = p_nombres
        self.midic["apellidos"] = p_apellidos
        self.midic["correo"] = p_correo
        self.midic["numTel"] = p_numTel
        self.midic["fechaNac"] = p_fechaNac

    def insertar_usuario(DNI, nombres, apellidos, correo, numTel, fechaNac):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO usuario(DNI, nombres, apellidos, correo, numTel, fechNacimiento) VALUES (%s, %s, %s, %s, %s,%s)", (DNI, nombres, apellidos, correo, numTel, fechaNac))
        conexion.commit()
        conexion.close()

    def obtener_usuario():
        conexion = obtener_conexion()
        usuarios = []
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM usuario")
            usuarios = cursor.fetchall()
        conexion.close()
        return usuarios


    def obtener_usuario_dni(dni):
        conexion = obtener_conexion()
        modo = None
        with conexion.cursor() as cursor: 
            cursor.execute("SELECT DNI, correo, numTel FROM usuario WHERE DNI= %s",(dni,))
            modo = cursor.fetchone()
        conexion.close()
        return modo


    def actualizar_usuario(correo, numTel, dni):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE usuario SET correo = %s, numTel= %s WHERE DNI=%s",(correo, numTel,dni))
        conexion.commit()
        conexion.close()


    def eliminar_usuario(dni):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM usuario WHERE DNI = %s", (dni,))
        conexion.commit()
        conexion.close()   