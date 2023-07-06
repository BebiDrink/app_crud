from flask import Blueprint, render_template, jsonify, request, url_for, redirect, flash
from utils.db import db
from models.tables import Producto, producto_schema, productos_schema


# Blueprint para registrar en app.py
approutes = Blueprint("approutes", __name__)



# ==================== INDEX ========================
@approutes.route("/", methods=["GET", "POST"])
def home():
    all_productos = Producto.query.all()
    result = productos_schema.dump(all_productos)
    return render_template("productos.html", productos=result)



# ==================== API TODOS LOS PRODUCTOS ========================
@approutes.route("/productos", methods=["GET"])
def get_productos():
    
    # Busca y obtiene todos los productos en la base de datos
    all_productos = Producto.query.all()

    # Serializa los productos
    result = productos_schema.dump(all_productos)

    # Retorna una Json array con los productos
    return jsonify(result)



# ==================== API UN SOLO PRODUCTO ========================
@approutes.route("/productos/<id>", methods=["GET"])
def get_producto(id):
    """
    Endpoint para obtener un producto específico de la base de datos.

    Retorna un JSON con la información del producto correspondiente al ID proporcionado.
    """

    # Obtiene el producto correspondiente al ID recibido
    producto = Producto.query.get(
        id
    )  
    
    # Retorna el JSON del producto
    return producto_schema.jsonify(producto)  



# ==================== API BORRAR PRODUCTO  ========================
@approutes.route("/del/<id>")
def delete_producto(id):
    """
    Endpoint para eliminar un producto de la base de datos.

    Elimina el producto correspondiente al ID proporcionado y retorna un JSON con el registro eliminado.
    """

    # Obtiene el producto correspondiente al ID recibido
    producto = Producto.query.get(id) 

    # Elimina el producto de la sesión de la base de datos
    db.session.delete(producto)

    # Guarda los cambios en la base de datos
    db.session.commit()

    flash('Producto borrado exitosamente', 'error')  

    # Redirige a la página principal y actualiza la lista de productos mostrados
    return redirect(url_for("approutes.home"))



# ==================== API CREAR PRODUCTO ========================
@approutes.route("/add", methods=['POST'])  # Endpoint para crear un producto
def create_producto():
    """
    Endpoint para crear un nuevo producto en la base de datos.
    Lee los datos proporcionados en formato JSON por el cliente y crea un nuevo registro 
    de producto en la base de datos. Retorna un JSON con el nuevo producto creado.
    """
    nombre = request.form['nombre']
    precio = request.form['precio']
    stock = request.form['stock']
    imagen = request.form['imagen']

    nuevo_producto = Producto(nombre=nombre, precio=precio, stock=stock, imagen=imagen)
    db.session.add(nuevo_producto)
    db.session.commit()

    flash('Producto guardado exitosamente', 'success')

    return redirect(url_for("approutes.home"))

"""     # Obtiene el nombre del producto del JSON proporcionado
    nombre = request.json["nombre"] 

    # Obtiene el precio del producto del JSON proporcionado 
    precio = request.json["precio"] 

    # Obtiene el stock del producto del JSON proporcionado 
    stock = request.json["stock"]

    # Obtiene la imagen del producto del JSON proporcionado
    imagen = request.json["imagen"]  

    # Crea un nuevo objeto Producto con los datos proporcionados
    new_producto = Producto(nombre, precio, stock, imagen)  

    # Agrega el nuevo producto a la sesión de la base de datos
    db.session.add(new_producto)  

    # Guarda los cambios en la base de datos
    db.session.commit()  

    # Retorna el JSON del nuevo producto creado
    return producto_schema.jsonify(new_producto)   """



# ==================== API ATUALIZAR PRODUCTO ========================
# Endpoint para actualizar un producto
@approutes.route("/productos/<id>", methods=["PUT"])
def update_producto(id):
    """
    Endpoint para actualizar un producto existente en la base de datos.

    Lee los datos proporcionados en formato JSON por el cliente y actualiza el registro del producto con el ID especificado.
    Retorna un JSON con el producto actualizado.
    """

    # Obtiene el producto existente con el ID especificado
    producto = Producto.query.get(id)  

    # Actualiza los atributos del producto con los datos proporcionados en el JSON
    producto.nombre = request.json["nombre"]
    producto.precio = request.json["precio"]
    producto.stock = request.json["stock"]
    producto.imagen = request.json["imagen"]

    # Guarda los cambios en la base de datos
    db.session.commit() 

    # Retorna el JSON del producto actualizado
    return producto_schema.jsonify(producto)
