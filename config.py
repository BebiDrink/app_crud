# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:asd123@localhost/productos" # DEV
    #SQLALCHEMY_DATABASE_URI = 'mysql://usuario:contraseña@localhost/nombre_de_la_base_de_datos # PRODUCTION'
    #SECRET_KEY = 'clave_secreta'  # Cambia esto por una clave secreta más segura
    SQLALCHEMY_TRACK_MODIFICATIONS = False
