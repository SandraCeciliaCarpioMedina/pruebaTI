from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from flaskext.mysql import MySQL
from flask_cors import CORS, cross_origin

app= Flask(__name__)
mysql=MySQL()
app.config['MYSQL_DATABASE_USER'] ='root'
app.config['MYSQL_DATABASE_PASSWORD'] ='admi'
app.config['MYSQL_DATABASE_DB'] ='proyecto'
app.config['MYSQL_DATABASE_HOST'] ='127.0.0.1'
mysql.init_app(app)

conn =mysql.connect()
cursor=conn.cursor()

#CAMBIAR TABLA
curso_blueprint = Blueprint('curso_blueprint', __name__)
#CAMBIAR(2)
@curso_blueprint.route('/create_curso',methods=['POST'])
def create_curso():
    print(request.json)

    params={
        'idcurso':request.json['idcurso'],
        'nombre': request.json['nombre'],
        'creditos':request.json['creditos'],
        'alumno_cui':request.json['alumno_cui'],
        'profesor_idprofesor':request.json['profesor_idprofesor'],
        'asistencia_idasistencia':request.json['asistencia_idasistencia'],
    }
    #cambiar para cada tabla
    query="""insert into curso (idcurso, nombre,creditos,alumno_cui,profesor_idprofesor,asistencia_idasistencia) 
            values (%(idcurso)s, %(nombre)s,%(creditos)s,%(alumno_cui)s,%(profesor_idprofesor)s,%(asistencia_idasistencia)s)""" 
    cursor.execute(query,params)
    conn.commit()

    content={'idcurso':params['idcurso'],
             'nombre':params['nombre'],
             'creditos':params['creditos'],
             'alumno_cui':params['alumno_cui'],
             'profesor_idprofesor':params['profesor_idprofesor'],
             'asistencia_idasistencia':params['asistencia_idasistencia']}
    return jsonify(content)