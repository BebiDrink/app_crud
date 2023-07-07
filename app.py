from flask import Flask

from routes.views import approutes
from routes.auth import auth
from utils.db import db, ma
from config import Config




# Instancia de flask
app = Flask(__name__)


# Configuración de la aplicación
app.config.from_object(Config)


# Configuración de la base de datos y esquemas
ma.init_app(app)
db.init_app(app)


# Registro de las rutas
app.register_blueprint(auth)
app.register_blueprint(approutes)



# Crea todas las tablas en la base de datos
with app.app_context():
    db.create_all()


# app
if __name__ == "__main__":
    app.run(debug=True)
