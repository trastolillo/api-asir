import MySQLdb
from flask import request, jsonify
from src import app, mysql


@app.get('/unidades')
def listar_unidades():
    cursor = mysql.connection.cursor()
    try:
        sql = "select * from unidades"
        cursor.execute(sql)
        datos = cursor.fetchall()
        unidades = []
        if datos != None:
            for fila in datos:
                unidad = {
                    'id_modulo': fila[0],
                    'unidad': fila[1],
                    'titulo': fila[2],
                    'url': fila[3]
                }
                unidades.append(unidad)
        return jsonify(unidades)
    except (MySQLdb.Error, MySQLdb.Warning) as ex:
        print(f"********** Error: {ex}")
        return jsonify({'Error': str(ex)})
    except Exception as ex:
        return jsonify({'Error': ex.with_traceback})


@app.get('/unidad/<id_modulo>/<unidad>')
def listar_unidad(id_modulo: str, unidad: int):
    try:
        cursor = mysql.connection.cursor()
        sql = 'select * from unidades where id_modulo = "{0}" and unidad={1}'.format(
            id_modulo, unidad)
        cursor.execute(sql)
        datos = cursor.fetchone()
        unidad = {
            'id_modulo': datos[0],
            'unidad': datos[1],
            'titulo': datos[2],
            'url': datos[3]
        }
        return jsonify(unidad)
    except (MySQLdb.Error, MySQLdb.Warning) as ex:
        print(f"********** Error: {ex}")
        return jsonify({'Error': str(ex)})
    except Exception as ex:
        return jsonify({'Error': ex.with_traceback})


@app.post('/unidad')
def agregar_unidad():
    try:
        cursor = mysql.connection.cursor()
        sql = 'insert into unidades values ("{0}", {1}, "{2}", "{3}")'.format(
            request.json['id_modulo'],
            request.json['unidad'],
            request.json['titulo'],
            request.json['url']
        )
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({"resultado": "Unidad registrada"})
    except (MySQLdb.Error, MySQLdb.Warning) as ex:
        print(f"********** Error: {ex}")
        return jsonify({'Error': str(ex)})
    except Exception as ex:
        return jsonify({'Error': ex.with_traceback})


@app.put('/unidadurl/<id_modulo>/<unidad>')
def actualizar_url_unidad(id_modulo: str, unidad: int):
    try:
        cursor = mysql.connection.cursor()
        url = request.json['url']
        sql = f'update unidades set url="{url}" where id_modulo="{id_modulo}" and unidad={unidad}'
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({"resultado": "Curso actualizado"})
    except (MySQLdb.Error, MySQLdb.Warning) as ex:
        print(f"********** Error: {ex}")
        return jsonify({'Error': str(ex)})
    except Exception as ex:
        return jsonify({'Error': ex.with_traceback})


@app.delete('/unidad/<id_modulo>/<unidad>')
def eliminar_unidad(id_modulo: str, unidad: int):
    try:
        cursor = mysql.connection.cursor()
        sql = f'delete from unidades where id_modulo="{id_modulo}" and unidad={unidad}'
        cursor.execute(sql)
        mysql.connection.commit()
        # TODO: Cuando borras registro que no existe, retorna éxito
        return ({"resultado": "Curso eliminado"})
    except (MySQLdb.Error, MySQLdb.Warning) as ex:
        print(f"********** Error: {ex}")
        return jsonify({'Error': str(ex)})
    except Exception as ex:
        return jsonify({'Error': ex.with_traceback})
