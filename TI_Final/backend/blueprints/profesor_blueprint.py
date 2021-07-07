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

profesor_blueprint = Blueprint('profesor_blueprint', __name__)
#CAMBIAR(2)
@profesor_blueprint.route('/create_profesor',methods=['POST'])
def create_profesor():
    print(request.json)

    params={
        'idprofesor':request.json['idprofesor'],
        'Nombre': request.json['Nombre'],
        'ApellidoPaterno':request.json['ApellidoPaterno'],
        'ApellidoMaterno':request.json['ApellidoMaterno'],
        'DNI':request.json['DNI'],
        'telefono':request.json['telefono'],
    }
    #cambiar para cada tabla
    query="""insert into profesor (idprofesor, Nombre, ApellidoPaterno, ApellidoMaterno, DNI, telefono) 
            values (%(idprofesor)s, %(Nombre)s,%(ApellidoPaterno)s,%(ApellidoMaterno)s,%(DNI)s,%(telefono)s)"""
    cursor.execute(query,params)
    conn.commit()

    content={'idprofesor':params['idprofesor'],
             'Nombre':params['Nombre'],
             'ApellidoPaterno':params['ApellidoPaterno'],
             'ApellidoMaterno':params['ApellidoMaterno'],
             'DNI':params['DNI'],
             'telefono':params['telefono'],
            }
    return jsonify(content)