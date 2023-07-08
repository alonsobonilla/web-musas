from flask import Flask, request
from flask_jwt import JWT
from flask_swagger_ui import get_swaggerui_blueprint
from Token.usuario import authenticate, identity
from controllers.admin import *
from controllers.cliente import *
from controllers.autenticacion import *
from controllers.admin_productos import *
from controllers.admin_categoria_producto import *
from controllers.admin_usuarios import *
from controllers.admin_pedidos import *
from controllers.admin_ventas import *
# Importando apis
from APIS.productos import *
from APIS.usuarios import api_usuarios
from APIS.registro_pedidos import api_registro_pedidos
from APIS.detalleOrden import api_detalleOrden
from APIS.categoriaProducto import api_categoriaProducto
from APIS.detalleComprobante import api_detalleComprobante
from APIS.detalleCremas import api_detalleCremas
from APIS.comprobante import api_comprobante
from APIS.transacciones import transaccion
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key"
jwt = JWT(app, authenticate, identity)

# swagger
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
# Our API url (can of course be a local resource)
API_URL = '/static/documentacion.yaml'

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    SWAGGER_URL,
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

admin.register_blueprint(productos)
admin.register_blueprint(categoria_producto)
admin.register_blueprint(usuarios)
admin.register_blueprint(pedidos)
admin.register_blueprint(ventas)
admin.register_blueprint(auth)
cliente.register_blueprint(auth)

app.register_blueprint(admin)
app.register_blueprint(cliente)
# Registro de swagger
app.register_blueprint(swaggerui_blueprint)
# Registrando apis
app.register_blueprint(api_productos)
app.register_blueprint(api_usuarios)
app.register_blueprint(api_registro_pedidos)
app.register_blueprint(api_detalleOrden)
app.register_blueprint(api_categoriaProducto)
app.register_blueprint(api_detalleComprobante)
app.register_blueprint(api_detalleCremas)
app.register_blueprint(api_comprobante)
app.register_blueprint(transaccion)

app.secret_key = "mysecretkey"
# Iniciar el servidor

if __name__ == "__main__":
    app.run(debug=True)

# print(app.url_map)
