import MySQLdb
from flask import request, jsonify
from src import app, mysql


@app.get('/tareas')
def listar_tareas():
    cursor = mysql.connection.cursor()
    try:
        sql = "select * from view_tareas"
        cursor.execute(sql)
        datos = cursor.fetchall()
        tareas = []
        if datos != None:
            for fila in datos:
                tarea = {
                    'id_modulo': fila[0],
                    'modulo': fila[1],
                    'unidad': fila[2],
                    'titulo': fila[3],
                    'tipo': fila[4],
                    'fecha_limite': fila[5],
                    'fecha_terminado': fila[6],
                    'url': fila[7]
                }
                tareas.append(tarea)
        return jsonify(tareas)
    except (MySQLdb.Error, MySQLdb.Warning) as ex:
        print(f"********** Error: {ex}")
        return jsonify({'Error': str(ex)})
    except Exception as ex:
        return jsonify({'Error': ex.with_traceback})


@app.get('/tarea/<id_modulo>/<unidad>/<tipo>')
def listar_tarea(id_modulo: str, unidad: int, tipo: str):
    try:
        cursor = mysql.connection.cursor()
        sql = 'select * from view_tareas where id_modulo = "{0}" and unidad={1} and tipo ="{2}"'.format(
            id_modulo, unidad, tipo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        tarea = {
            'id_modulo': datos[0],
            'modulo': datos[1],
            'unidad': datos[2],
            'titulo': datos[3],
            'tipo': datos[4],
            'fecha_limite': datos[5],
            'fecha_terminado': datos[6],
            'url': datos[7]
        }
        return jsonify(tarea)
    except (MySQLdb.Error, MySQLdb.Warning) as ex:
        print(f"********** Error: {ex}")
        return jsonify({'Error': str(ex)})
    except Exception as ex:
        return jsonify({'Error': ex.with_traceback})


@app.post('/tarea')
def agregar_tarea():
    cursor = mysql.connection.cursor()
    try:
        sql = 'insert into tareas (id_modulo, unidad, tipo, fecha_limite) values ("{0}", {1}, "{2}", "{3}")'.format(
            request.json['id_modulo'],
            request.json['unidad'],
            request.json['tipo'],
            request.json['fecha_limite']
        )
        cursor.execute(sql)
        mysql.connection.commit()

        return jsonify({"resultado": "Tarea registrada"})
    except (MySQLdb.Error, MySQLdb.Warning) as ex:
        print(f"********** Error: {ex}")
        return jsonify({'Error': str(ex)})
    except Exception as ex:
        return jsonify({'Error': ex.with_traceback})


@app.put('/fin/<id_modulo>/<unidad>/<tipo>')
def finalizar_tarea(id_modulo: str, unidad: int, tipo: str):
    try:
        cursor = mysql.connection.cursor()
        fecha_terminado = request.json['fecha_terminado']
        sql = f'update tareas set fecha_terminado="{fecha_terminado}" where id_modulo="{id_modulo}" and unidad={unidad} and tipo="{tipo}"'
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({"resultado": "Curso actualizado"})
    except (MySQLdb.Error, MySQLdb.Warning) as ex:
        print(f"********** Error: {ex}")
        return jsonify({'Error': str(ex)})
    except Exception as ex:
        return jsonify({'Error': ex.with_traceback})


@app.delete('/tarea/<id_modulo>/<unidad>/<tipo>')
def eliminar_tarea(id_modulo: str, unidad: int, tipo: str):
    try:
        cursor = mysql.connection.cursor()
        sql = f'delete from tareas where id_modulo="{id_modulo}" and unidad={unidad} and tipo="{tipo}"'
        cursor.execute(sql)
        mysql.connection.commit()
        # TODO: Cuando borras registro que no existe, retorna ??xito
        return ({"resultado": "Curso eliminado"})
    except (MySQLdb.Error, MySQLdb.Warning) as ex:
        print(f"********** Error: {ex}")
        return jsonify({'Error': str(ex)})
    except Exception as ex:
        return jsonify({'Error': ex.with_traceback})
