from bd import obtener_conexion

class CategoriaProducto:
    idCategoria = 0
    nombreCategoria = ""
    descripcion = ""
    midic = dict()

    def __init__(self,p_idCategoria,p_nombreCategoria,p_descripcion):
        self.idCategoria = p_idCategoria
        self.nombreCategoria = p_nombreCategoria
        self.descripcion = p_descripcion
        self.midic["idCategoria"] = p_idCategoria
        self.midic["nombreCategoria"] = p_nombreCategoria
        self.midic["descripcion"] = p_descripcion


    @staticmethod
    def insertar_categoria(nombreCategoria, descripcion):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO categoriaProducto(nombreCategoria, descripcion) VALUES (%s, %s)",
            (nombreCategoria, descripcion))
        conexion.commit()
        conexion.close()

    def obtener_categorias():
        conexion = obtener_conexion()
        categoria = []
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM categoriaProducto")
            categoria = cursor.fetchall()
        conexion.close()
        return categoria

    def eliminar_categoria(idCategoria):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM categoriaProducto WHERE idCategoria = %s", (idCategoria,))
                conexion.commit()
                conexion.close()
                return True
            except:
                return False


    def obtener_categoria_por_id(idCategoria):
        conexion = obtener_conexion()
        juego = None
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT idCategoria, nombreCategoria, descripcion FROM categoriaProducto WHERE idCategoria = %s", (idCategoria))
            juego = cursor.fetchone()
        conexion.close()
        return juego
    
    def actualizar_categoria(nombreCategoria, descripcion, id):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE categoriaProducto SET nombreCategoria = %s, descripcion = %s WHERE idCategoria = %s",
                        ( nombreCategoria, descripcion, id))
        conexion.commit()
        conexion.close()


    # def obtener_idcategoria_por_nombre(nombreCategoria):
    #     conexion = obtener_conexion()   
    #     Cat = None
    #     with conexion.cursor() as cursor:
    #         cursor.execute("Select idCategoria FROM categoriaProducto WHERE nombreCategoria=%s",(nombreCategoria))
    #         Cat = cursor.fetchone()
    #     conexion.close()
    #     return Cat