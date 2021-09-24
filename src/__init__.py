from flask import Flask
from flask_mysqldb import MySQL
from src import config


app = Flask(__name__)
app.config.from_object(config.configuracion['development'])
mysql = MySQL(app)


def pagina_no_encontrada(error):
    return error


from src import modulos
