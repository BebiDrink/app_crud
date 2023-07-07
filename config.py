# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# VARIABLES DE ENTORNO
USER = os.environ['DB_USER']
PASSWORD = os.environ['DB_PASS']
HOST = os.environ['DB_HOST']
DATABASE = os.environ['DB_DATABASE']
S_KEY = os.environ['SECRET_KEY']

# URI PARA LA CONEXIÓN
CONNECTION_URI = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"

# CONFIGURACIÓN PARA LA INSTANCIA DE APP CON SQL ALCHEMY
class Config:
    SQLALCHEMY_DATABASE_URI = CONNECTION_URI # DEV
    SECRET_KEY = f'{S_KEY}' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False




