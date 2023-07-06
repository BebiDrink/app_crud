from flask import Blueprint, render_template, request
from models.tables import Usuario

auth = Blueprint('auth', __name__)

# LOGIN AUTENTICACIÓN DE EMPLEADOS
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.json.get("username")
        password = request.json.get("password")

        usuario = Usuario.query.filter_by(usuario=username).first()

    return render_template("login.html")