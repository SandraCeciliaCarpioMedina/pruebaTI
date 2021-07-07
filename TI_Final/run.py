from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
#from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

#IMPORTANDO LOS ARCHIVOS
from backend.blueprints.alumno_blueprint import alumno_blueprint
from backend.blueprints.carrera_blueprint import carrera_blueprint
from backend.blueprints.curso_blueprint import curso_blueprint
from backend.blueprints.facultad_blueprint import facultad_blueprint
from backend.blueprints.profesor_blueprint import profesor_blueprint

app = Flask(__name__)
# para que utilice vue compilado ( npm run build ). En la carpeta dist, esta lo compilado de vue
#app = Flask(__name__,
#            static_folder = "./frontend/dist/static",
#            template_folder = "./frontend/dist")

#IMPORTANDO LOS ARCHIVOS II:
app.register_blueprint(alumno_blueprint)
app.register_blueprint(carrera_blueprint)
app.register_blueprint(curso_blueprint)
app.register_blueprint(facultad_blueprint)
app.register_blueprint(profesor_blueprint)



#conectarse a otro servidor 
#cors = CORS(app)
#@app.route('/', defaults={'path': ''})
#@app.route('/<path:path>')
#def dender_vue(path):
#    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
