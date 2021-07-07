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
alumno_blueprint = Blueprint('alumno_blueprint', __name__)
#CAMBIAR(2)
@alumno_blueprint.route('/create_alumno',methods=['POST'])
def create_alumno():
    print(request.json)

    params={
        'cui':request.json['cui'],
        'nombre': request.json['nombre'],
        'paterno':request.json['paterno'],
        'materno':request.json['materno'],
        'telefono':request.json['telefono'],
        'carrera_idcarrera':request.json['carrera_idcarrera'],
        'email':request.json['email'],
    }
    #cambiar para cada tabla
    query="""insert into alumno (cui, nombre,paterno,materno,telefono,carrera_idcarrera,email) 
            values (%(cui)s, %(nombre)s,%(paterno)s,%(materno)s,%(telefono)s,%(carrera_idcarrera)s,%(email)s)""" 
    cursor.execute(query,params)
    conn.commit()

    content={'cui':params['cui'],
             'nombre':params['nombre'],
             'paterno':params['paterno'],
             'materno':params['materno'],
             'telefono':params['telefono'],
             'carrera_idcarrera':params['carrera_idcarrera'],
             'email':params['email']}
    return jsonify(content)