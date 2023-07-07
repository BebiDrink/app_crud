# APP CRUD (PRODUCTOS) CON FLASK

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0-green)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4-yellow)
![HTML](https://img.shields.io/badge/HTML-5-red)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4-purple)

Este repositorio contiene una aplicación CRUD desarrollada en el marco del curso Full Stack Python de CAC. El objetivo principal de esta aplicación es establecer una comunicación efectiva entre el backend y el frontend, permitiendo la gestión de productos.

## Tecnologías utilizadas

- Python
- Flask
- MySQL
- SQLAlchemy
- HTML
- Bootstrap

## Descripción

La aplicación CRUD (Create, Read, Update, Delete) con Flask es una solución integral que permite la gestión de productos. Fue desarrollada como parte del curso Full Stack Python de CAC, brindando a los participantes la oportunidad de aplicar sus conocimientos en un proyecto real.

### Características principales

- **Backend con Flask**: La aplicación utiliza Flask, un framework web de Python, para proporcionar un backend robusto y flexible. Flask permite el enrutamiento de URL, la gestión de solicitudes y respuestas, y la integración con bases de datos.

- **Persistencia de datos con MySQL**: Se emplea MySQL como base de datos para almacenar y recuperar la información de los productos. Esto garantiza la integridad y la disponibilidad de los datos en todo momento.

- **ORM SQLAlchemy**: Se utiliza SQLAlchemy como ORM (Object-Relational Mapping) para interactuar con la base de datos de manera intuitiva y eficiente. SQLAlchemy simplifica las operaciones de consulta y manipulación de datos, permitiendo una mayor productividad en el desarrollo.

- **Interfaz de usuario intuitiva**: La aplicación cuenta con una interfaz de usuario desarrollada en HTML, que proporciona una experiencia amigable y fácil de usar. Se ha aplicado el framework Bootstrap para estilizar la aplicación, lo que la hace atractiva visualmente y adaptable a diferentes dispositivos.

### Funcionalidades principales

- **Autenticación de usuarios**: Se ha implementado un sistema de autenticación que valida las credenciales de los usuarios autorizados, en este caso, empleados. Esto garantiza la seguridad y el acceso controlado a la aplicación.

- **Gestión de productos**: La página de productos muestra una lista de los productos existentes y permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar). Los usuarios pueden agregar nuevos productos, editar los existentes y eliminarlos según sea necesario.

- **API para consumo externo**: La aplicación cuenta con una API general habilitada mediante el módulo Flask-CORS. Esto permite que la página Bebidrink, u otras aplicaciones externas, puedan consumir la API y mostrar los productos a los clientes de forma dinámica.

## Configuración y ejecución

Para ejecutar la aplicación en tu entorno local, sigue los siguientes pasos:

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias especificadas en el archivo `requirements.txt`.
3. Configura los parámetros de conexión a la base de datos en el archivo `config.py`.
4. Ejecuta la aplicación utilizando el comando `python app.py`.
5. Accede a la aplicación en tu navegador web mediante la URL `http://localhost:5000`.

¡Disfruta de la gestión de productos con la aplicación CRUD desarrollada con Flask! Si tienes alguna pregunta o sugerencia, no dudes en contactarnos.