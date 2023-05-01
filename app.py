from flask import Flask, render_template
from controllers.admin import *
from controllers.cliente import *


app = Flask(__name__)

app.register_blueprint(cliente)
app.register_blueprint(admin, url_prefix='/admin')

# Iniciar el servidor
if __name__ == "__main__":
    app.run(debug=True)

# print(app.url_map)

