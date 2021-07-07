#Importamos
from flask import Flask
from flask import render_template
from flask import request

#Instanciamos Flask /Aplicacion
app =Flask(__name__,)

#Creamos nuestro primer roue '/login'
@app.route('/login2',methods=['POST'])
def template():
    #Renderizamos la plantilla de html
    #templates/login.html
    return render_template("login2.html")

#Definimos el route con el metodo post
@app.route('/usuario',methods=['POST'])
def usuario():
    #Obtenemos la informacion del parametro nobreUsuario
    nombreUsuario=request.form ['nombreUsuario']
#Retorna Respuesta
    return"<h1>Bienvenido  "+  nombreUsuario  +  "</h1>"

if __name__=='__main__':
#Iniciamos la aplicacion c
   app.run(debug=True) 