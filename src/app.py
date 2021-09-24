from flask import Flask, jsonify
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)
mysql = MySQL(app)


def pagina_no_encontrada(error):
    return error


import modulos

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
