from bd import obtener_conexion

class Usuario:
    DNI = ""
    nombres = ""
    apellidos = ""
    correo = ""
    numTel = ""
    contraseña = ""
    tipoUsuario = ""
    midic   = dict()

    def __init__(self,p_DNI,p_nombres,p_apellidos,p_correo,p_numTel,p_contraseña, p_tipoUsuario):
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

        self.midic["tipoUsuario"]=self.tipoUsuario

    def insertar_usuario(DNI, nombres, apellidos, correo, numTel,contra, tipoUsuario):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO usuario(DNI, nombres, apellidos, correo, numTel,contraseña, tipoUsuario) VALUES (%s, %s, %s, %s, %s, %s, %s)", (DNI, nombres, apellidos, correo, numTel,contra, tipoUsuario))
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


    def obtener_usuario_dni_tipo(dni, tipoUsuario):
        conexion = obtener_conexion()
        modo = None
        with conexion.cursor() as cursor: 
            cursor.execute("SELECT DNI,nombres,apellidos,correo, numTel, contraseña, tipoUsuario FROM usuario WHERE DNI= %s and tipoUsuario = %s",(dni,tipoUsuario))
            modo = cursor.fetchone()
        conexion.close()
        return modo

    def actualizar_usuario(correo, numTel,contra,dni, tipo):
        if correo is "":
            correo = Usuario.obtener_usuario(dni)[3]
        elif numTel is "":
            numTel = Usuario.obtener_usuario(dni)[4]
        elif contra is "":
            contra = Usuario.obtener_usuario(dni)[5]
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE usuario SET correo = %s, numTel= %s, contraseña= %s WHERE DNI=%s and tipoUsuario = %s",(correo, numTel,contra,dni, tipo))
        conexion.commit()
        conexion.close()
    
    def eliminar_usuario(dni, tipoUsuario):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM usuario WHERE DNI = %s and tipoUsuario = %s", (dni,tipoUsuario))
        conexion.commit()
        conexion.close() 
