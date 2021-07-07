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
carrera_blueprint = Blueprint('carrera_blueprint', __name__)
#CAMBIAR(2)
@carrera_blueprint.route('/create_carrera',methods=['POST'])
def create_carrera():
    print(request.json)

    params={
        'idcarrera':request.json['idcarrera'],
        'nombre': request.json['nombre'],
        'escuela_idescuela':request.json['escuela_idescuela'],
        'profesor_idprofesor':request.json['profesor_idprofesor'],
        'facultad_idfacultad':request.json['facultad_idfacultad'],
    }
    #cambiar para cada tabla
    query="""insert into carrera (idcarrera, nombre,escuela_idescuela,profesor_idprofesor,facultad_idfacultad) 
            values (%(idcarrera)s, %(nombre)s,%(escuela_idescuela)s,%(profesor_idprofesor)s,%(facultad_idfacultad)s)""" 
    cursor.execute(query,params)
    conn.commit()

    content={'idcarrera':params['idcarrera'],
             'nombre':params['nombre'],
             'escuela_idescuela':params['escuela_idescuela'],
             'profesor_idprofesor':params['profesor_idprofesor'],
             'facultad_idfacultad':params['facultad_idfacultad']}
    return jsonify(content)