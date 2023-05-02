from flask import Flask, render_template
from controllers.admin import *
from controllers.cliente import *
from controllers.autenticacion import *

app = Flask(__name__)

app.register_blueprint(cliente)
app.register_blueprint(admin)
app.register_blueprint(auth)

# Iniciar el servidor

if __name__ == "__main__":
    app.run(debug=True)

# print(app.url_map)

