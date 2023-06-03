from bd import obtener_conexion

class Producto:
    @staticmethod
    def getProductosCategoria(id):
        conexion = obtener_conexion()
        productos = []
        with conexion.cursor() as cursor:
            cursor.execute("select * from producto where idCategoria = %s", id)  
            productos = cursor.fetchall()
        conexion.close()

        if productos is None:
            return productos
        
        lista_diccionarios = []
        for producto in productos:
            diccionario = dict()
            diccionario["idProducto"] = producto[0]
            diccionario["nombre"] = producto[2]
            diccionario["descripcion"] = producto[3]
            diccionario["precio"] = producto[4]
            diccionario["existencias"] = producto[5]
            lista_diccionarios.append(diccionario)
        return lista_diccionarios
    
    @staticmethod
    def insertar_producto( nombre, descripcion, precio, existencias, idCategoria):
        
        if nombre == "" or descripcion == "" or precio == "" or existencias == "" or idCategoria == "":
            return False
        
        nombre = nombre.strip()
        descripcion = descripcion.strip()
        precio = float(precio.strip()) if type(precio) == str else precio
        existencias = int(existencias.strip()) if type(existencias) == str else existencias
        idCategoria = int(idCategoria.strip()) if type(idCategoria) == str else idCategoria

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

        lista_diccionarios = []
        for producto in productos:
            diccionario = dict()
            diccionario["idProducto"] = producto[0]
            diccionario["idCategoria"] = producto[1]
            diccionario["nombre"] = producto[2]    
            diccionario["descripcion"] = producto[3]
            diccionario["precio"] = producto[4]
            diccionario["existencias"] = producto[5]
            diccionario["nombreCategoria"] = producto[6]
            lista_diccionarios.append(diccionario)
        return lista_diccionarios
        
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
                "SELECT p.idProducto, p.nombre, p.descripcion, p.precio, p.existencias, cp.nombreCategoria, p.idCategoria FROM producto p INNER JOIN categoriaProducto cp ON p.idCategoria = cp.idCategoria WHERE idProducto = %s", (id))
            seleccion = cursor.fetchone()
        conexion.close()

        if seleccion is None:
            return seleccion
        
        diccionario = dict()
        diccionario["idProducto"] = seleccion[0]
        diccionario["nombre"] = seleccion[1]
        diccionario["descripcion"] = seleccion[2]
        diccionario["precio"] = seleccion[3]
        diccionario["existencias"] = seleccion[4]   
        diccionario["nombreCategoria"] = seleccion[5]
        diccionario["idCategoria"] = seleccion[6]
        return diccionario

    @staticmethod
    def actualizar_producto(nombre, descripcion, precio, existencias, id, idCategoria):
        
        id = int(id)
        nombre = nombre.strip()
        descripcion = descripcion.strip()
        precio = float(precio.strip()) if type(precio) == str else precio
        existencias = int(existencias.strip()) if type(existencias) == str else existencias
        idCategoria = int(idCategoria.strip()) if type(idCategoria) == str else idCategoria

        if nombre == "" or descripcion == "" or precio == "" or existencias == "" or idCategoria == "":
            producto = Producto.obtener_producto_por_id(id)
            if nombre == "":
                nombre = producto["nombre"]
            if descripcion == "":
                descripcion = producto["descripcion"]
            if precio == "":
                precio = producto["precio"]
            if existencias == "":
                existencias = producto["existencias"]
            if idCategoria == "":
                idCategoria = producto["idCategoria"]
        
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE producto SET nombre = %s, descripcion = %s, precio = %s, existencias = %s, idCategoria = %s WHERE idProducto = %s", (nombre, descripcion, precio, existencias, idCategoria, id ))
        conexion.commit()
        conexion.close()


   