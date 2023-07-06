from utils.db import db, ma

""" from flask_login import UserMixin """


# MODELO DE TABLA USUARIOS
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __init__(self, usuario, password):
        """
        Constructor de la clase Usuario.

        Args:
            Usuario (str): Nombre de usuario.
            Password (str): Password del usuario.
        """

        self.usuario = usuario
        self.password = password


# MODELO DE TABLA PRODUCTOS
class Producto(db.Model):
    """
    Definición de la tabla Producto en la base de datos.
    La clase Producto hereda de db.Model.
    Esta clase representa la tabla "Producto" en la base de datos.
    """

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    imagen = db.Column(db.String(400))

    def __init__(self, nombre, precio, stock, imagen):
        """
        Constructor de la clase Producto.

        Args:
            nombre (str): Nombre del producto.
            precio (int): Precio del producto.
            stock (int): Cantidad en stock del producto.
            imagen (str): URL o ruta de la imagen del producto.
        """
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.imagen = imagen


# Esquema de Usuario
class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ("id", "usuario", "password")


# Esquema de Producto
class ProductoSchema(ma.Schema):
    class Meta:
        fields = ("id", "nombre", "precio", "stock", "imagen")


# Crear instancias de los esquemas
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)
