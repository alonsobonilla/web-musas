from flask import Flask, render_template
from controllers.admin import *
from controllers.cliente import *
from controllers.autenticacion import *
from controllers.admin_productos import *
from controllers.admin_categoria_producto import *
app = Flask(__name__)

admin.register_blueprint(productos)
admin.register_blueprint(categoria_producto)

admin.register_blueprint(auth)
cliente.register_blueprint(auth)

app.register_blueprint(admin)
app.register_blueprint(cliente)


app.secret_key = "mysecretkey"

# Iniciar el servidor

if __name__ == "__main__":
    app.run(debug=True)

# print(app.url_map)

