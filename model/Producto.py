from bd import obtener_conexion

class Producto:   
    @staticmethod
    def getProductosTipo(id):
        conexion = obtener_conexion()
        productos = []
        query = "select nombre, descripcion, precio from producto where id_categoria = " + id
        with conexion.cursor() as cursor:
            cursor.execute(query)  
            productos = cursor.fetchall()
        conexion.close()
        return productos
    
    @staticmethod
    def insertar_producto( nombre, descripcion, precio, existencias):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO producto( nombre, descripcion, precio, existencias) VALUES (%s, %s, %s, %s)",
                        ( nombre, descripcion, precio, existencias))
        conexion.commit()
        conexion.close()

    @staticmethod
    def obtener_productos():
        conexion = obtener_conexion()
        productos = []
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idProducto, nombre, descripcion, precio, existencias FROM producto")
            productos = cursor.fetchall()
        conexion.close()
        return productos
        
    @staticmethod
    def eliminar_producto(id):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM producto WHERE idProducto = %s", (id))
        conexion.commit()
        conexion.close()

    @staticmethod
    def obtener_producto_por_id(id):
        conexion = obtener_conexion()
        seleccion = None
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT idProducto, nombre, descripcion, precio, existencias FROM producto WHERE idProducto = %s", (id))
            seleccion = cursor.fetchone()
        conexion.close()
        return seleccion

    @staticmethod
    def actualizar_producto(nombre, descripcion, precio, existencias, id):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE producto SET nombre = %s, descripcion = %s, precio = %s, existencias = %s WHERE idProducto = %s", (nombre, descripcion, precio, existencias, id))
        conexion.commit()
        conexion.close()