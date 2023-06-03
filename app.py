from flask import Flask
from flask_jwt import JWT
from Token.usuario import authenticate, identity
from controllers.admin import *
from controllers.cliente import *
from controllers.autenticacion import *
from controllers.admin_productos import *
from controllers.admin_categoria_producto import *
from controllers.admin_usuarios import *

#Importando apis
from APIS.productos import *
from APIS.usuarios import *
from APIS.usuarioAdmin import api_admin
from APIS.registro_pedidos import api_registro_pedidos
from APIS.detalleOrden import api_detalleOrden
from APIS.categoriaProducto import api_categoriaProducto

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key"
jwt = JWT(app, authenticate, identity)

admin.register_blueprint(productos)
admin.register_blueprint(categoria_producto)
admin.register_blueprint(usuarios)
admin.register_blueprint(auth)
cliente.register_blueprint(auth)

app.register_blueprint(admin)
app.register_blueprint(cliente)

#Registrando apis
app.register_blueprint(api_productos)
app.register_blueprint(api_usuariosCliente)
app.register_blueprint(api_admin)
app.register_blueprint(api_registro_pedidos)
app.register_blueprint(api_detalleOrden)
app.register_blueprint(api_categoriaProducto)


app.secret_key = "mysecretkey"
# Iniciar el servidor

if __name__ == "__main__":
    app.run(debug=True)

# print(app.url_map)