#Importamos
from flask import Flask
from flask import render_template
from flask import request

#Instanciamos Flask /Aplicacion
app =Flask(__name__,)

#Creamos nuestro primer roue '/login'
@app.route('/login')
def template():
    #templates/form.html
    return render_template("login.html")

#Definimos el route con el metodo GET
@app.route('/usuario',methods=['GET'])
def usuario():
    nombreUsuario=request.args.get('nombreUsuario')
#Retorna Respuesta
    return"<h1>Bienvenido  "+  nombreUsuario  +  "</h1>"

if __name__=='__main__':
#Iniciamos la aplicacion c
   app.run(debug=True) 