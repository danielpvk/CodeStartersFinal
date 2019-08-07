import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# The database URI
#************************
# ***********************DATABASE LOCAL
#************************
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@localhost:3306/cartera_vigente"

#************************
# ***********************DATABASE HEROKU
#************************
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@localhost:3306/vida_empresas"

db = SQLAlchemy(app)


# Create our database model

class cartera_vigente(db.Model):
    __tablename__ = 'cartera_vigente'

    Index = db.Column(db.Integer, primary_key=True)
    Estado = db.Column(db.String)
    Sector = db.Column(db.String)
    Cartera = db.Column(db.Integer)
    Fecha = db.Column(db.Date)


    def __repr__(self):
        return '<vida %r>' % (self.name)



def resultadoCartera (EstadoQuery,SectorQuery):
    results = db.session.query(cartera_vigente.Cartera, cartera_vigente.Fecha).filter(cartera_vigente.Estado == EstadoQuery,cartera_vigente.Sector == SectorQuery)
    print(results)
    # Create a dictionary from the row data and append to a list
    lista_resultado = []
    for cartera, fecha in results:
        lista_dict = {}
        lista_dict["Cartera"] = cartera
        lista_dict["Fecha"] = fecha
        lista_resultado.append(lista_dict)

    return lista_resultado



# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()


@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

# AGUASCALIENTESW
@app.route("/Aguascalientes/Bancario/")
def AgsProbabilidadSupervivenciaServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoCartera("Aguascalientes","Bancario"))




if __name__ == '__main__':
    app.run(debug=True)
