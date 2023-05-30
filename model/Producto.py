from bd import obtener_conexion

class Producto:
    nombre = None
    descripcion = None
    precio = 0.0    
    existencias = 0
    idCategoria = None
    diccionario = dict()

    def __init__(self, nombre, descripcion, precio, existencias, idCategoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.existencias = existencias
        self.idCategoria = idCategoria
        self.diccionario["idProducto"] = idProducto
        self.diccionario["nombre"] = nombre
        self.diccionario["descripcion"] = descripcion
        self.diccionario["precio"] = precio
        self.diccionario["existencias"] = existencias
        self.diccionario["idCategoria"] = idCategoria

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
    def insertar_producto( nombre, descripcion, precio, existencias, idCategoria):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO producto( idCategoria, nombre, descripcion, precio, existencias) VALUES (%s, %s, %s, %s, %s)",
                        ( idCategoria, nombre, descripcion, precio, existencias))
        conexion.commit()
        conexion.close()

    @staticmethod
    def obtener_productos():
        conexion = obtener_conexion()
        productos = []
        query = "SELECT p.*, cp.nombreCategoria  FROM producto p INNER JOIN categoriaProducto cp ON p.idCategoria = cp.idCategoria"
        with conexion.cursor() as cursor:
            cursor.execute(query)
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
                "SELECT p.idProducto, p.nombre, p.descripcion, p.precio, p.existencias, cp.nombreCategoria FROM producto p INNER JOIN categoriaProducto cp ON p.idCategoria = cp.idCategoria WHERE idProducto = %s", (id))
            seleccion = cursor.fetchone()
        conexion.close()
        return seleccion

    @staticmethod
    def actualizar_producto(nombre, descripcion, precio, existencias, id, idCategoria):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE producto SET nombre = %s, descripcion = %s, precio = %s, existencias = %s, idCategoria = %s WHERE idProducto = %s", (nombre, descripcion, precio, existencias, idCategoria, id ))
        conexion.commit()
        conexion.close()