from flask import request, jsonify
from src import app, mysql


@app.get('/modulos')
def listar_modulos():
    try:
        cursor = mysql.connection.cursor()
        sql = "select * from modulos"
        cursor.execute(sql)
        datos = cursor.fetchall()
        modulos = []
        if datos != None:
            for fila in datos:
                modulo = {'id_modulo': fila[0],
                          'modulo': fila[1], 'url': fila[2]}
                modulos.append(modulo)
        return jsonify(modulos)
    except Exception as ex:
        return jsonify({'Error': ex.with_traceback})


@app.get('/modulo/<id>')
def listar_modulo(id):
    try:
        cursor = mysql.connection.cursor()
        sql = 'select * from modulos where id_modulo = "{0}"'.format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        modulo = {'id_modulo': datos[0],
                  'modulo': datos[1], 'url': datos[2]}
        return jsonify(modulo)
    except Exception as ex:
        return jsonify({'Error': 'Modulo no existe'})


@app.post('/modulo')
def agregar_modulo():
    try:
        cursor = mysql.connection.cursor()
        sql = 'insert into modulos values ("{0}", "{1}", "{2}")'.format(
            request.json['id_modulo'],
            request.json['modulo'],
            request.json['url']
        )
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({"resultado": "Módulo registrado"})
    except Exception as ex:
        return jsonify({'Error': 'Error agregando el módulo'})


@app.delete('/modulo/<id>')
def eliminar_modulo(id):
    try:
        cursor = mysql.connection.cursor()
        sql = 'delete from modulos where id_modulo="{0}"'.format(id)
        cursor.execute(sql)
        mysql.connection.commit()
        # TODO: Cuando borras registro que no existe, retorna éxito
        return ({"resultado": "Curso eliminado"})
    except Exception as ex:
        return jsonify({'Error': 'Error eliminando'})


@app.put('/modulo/<id>')
def actualizar_modulo(id):
    try:
        cursor = mysql.connection.cursor()
        sql = 'update modulos set modulo="{0}", url="{1}" where id_modulo="{2}"'.format(
            request.json['modulo'],
            request.json['url'],
            id
        )
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({"resultado": "Curso actualizado"})
    except Exception as ex:
        return jsonify({'Error': ex})
