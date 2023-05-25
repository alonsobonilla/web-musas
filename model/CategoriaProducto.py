from bd import obtener_conexion
class CategoriaProducto:

    @staticmethod
    def insertar_categoria(nombreCategoria, descripcion):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO categoriaProducto(nombreCategoria, descripción) VALUES (%s, %s)",
            (nombreCategoria, descripcion))
        conexion.commit()
        conexion.close()

    def obtener_categorias():
        conexion = obtener_conexion()
        categoria = []
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idCategoria, nombreCategoria, descripción FROM categoriaProducto")
            categoria = cursor.fetchall()
        conexion.close()
        return categoria

    def eliminar_categoria(idCategoria):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM categoriaProducto WHERE idCategoria = %s", (idCategoria,))
        conexion.commit()
        conexion.close()

    def obtener_categoria_por_id(idCategoria):
        conexion = obtener_conexion()
        juego = None
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT idCategoria, nombreCategoria, descripción FROM categoriaProducto WHERE idCategoria = %s", (idCategoria,))
            juego = cursor.fetchone()
        conexion.close()
        return juego

    def actualizar_categoria(nombreCategoria, descripcion, id):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE categoria SET nombreCategoria = %s, descripcion = %s WHERE idCategoria = %s",
                        ( nombreCategoria, descripcion, id))
        conexion.commit()
        conexion.close()