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

#Cambio 
facultad_blueprint = Blueprint('facultad_blueprint', __name__)
#CAMBIAR(2)
@facultad_blueprint.route('/create_facultad',methods=['POST'])
def create_facultad():
    print(request.json)

    params={
        'idfacultad':request.json['idfacultad'],
        'nombre': request.json['nombre'],
        'escuela_idescuela':request.json['escuela_idescuela'],
    }
    #cambiar para cada tabla
    query="""insert into facultad (idfacultad, nombre,escuela_idescuela) 
            values (%(idfacultad)s, %(nombre)s,%(escuela_idescuela)s)""" 
    cursor.execute(query,params)
    conn.commit()

    content={'idfacultad':params['idfacultad'],
             'nombre':params['nombre'],
             'escuela_idescuela':params['escuela_idescuela']}
    return jsonify(content)