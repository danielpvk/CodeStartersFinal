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
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:007007Jr@localhost:3306/cartera_vigente"

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
    Cartera = db.Column(db.Float)
    Vencida = db.Column(db.Float)
    Vigente = db.Column(db.Float)
    Imor = db.Column(db.Float)
    Fecha = db.Column(db.String)


    def __repr__(self):
        return '<cartera_vigente %r>' % (self.name)



def resultadoCartera (EstadoQuery,SectorQuery):
    results = db.session.query(cartera_vigente.Cartera, cartera_vigente.Fecha,cartera_vigente.Vencida,cartera_vigente.Imor,cartera_vigente.Vigente).filter(cartera_vigente.Estado == EstadoQuery,cartera_vigente.Sector == SectorQuery)
    print(results)
    # Create a dictionary from the row data and append to a list
    lista_resultado = []
    for cartera, fecha, vencida,vigente, imor in results:
        lista_dict = {}
        lista_dict["Cartera"] = cartera
        lista_dict["Fecha"] = fecha
        lista_dict["Vencida"] = vencida
        lista_dict["Vigente"] = vigente
        lista_dict["Imor"] = imor

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
def A1():	
    return jsonify(resultadoCartera("Aguascalientes","Bancario"))
@app.route('/Aguascalientes/ServiciosFinancieros(NoBancarios)/')	
def A2():	
    return jsonify(resultadoCartera('Aguascalientes','ServiciosFinancieros(NoBancarios)'))
@app.route('/Aguascalientes/ServiciosProfesionalesyTecnicos/')	
def A3():	
    return jsonify(resultadoCartera('Aguascalientes','ServiciosProfesionalesyTecnicos'))
@app.route('/Aguascalientes/Transporte/')	
def A4():	
    return jsonify(resultadoCartera('Aguascalientes','Transporte'))
@app.route('/Aguascalientes/Bancario/')	
def A5():	
    return jsonify(resultadoCartera('Aguascalientes','Bancario'))
@app.route('/Aguascalientes/AgriculturaSilviculturaGanaderiayPesca/')	
def A6():	
    return jsonify(resultadoCartera('Aguascalientes','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Aguascalientes/AlimentosBebidasyTabaco/')	
def A7():	
    return jsonify(resultadoCartera('Aguascalientes','AlimentosBebidasyTabaco'))
@app.route('/Aguascalientes/Comercio/')	
def A8():	
    return jsonify(resultadoCartera('Aguascalientes','Comercio'))
@app.route('/Aguascalientes/ComunicacionesyTelecomunicaciones/')	
def A9():	
    return jsonify(resultadoCartera('Aguascalientes','ComunicacionesyTelecomunicaciones'))
@app.route('/Aguascalientes/Construccion/')	
def A10():	
    return jsonify(resultadoCartera('Aguascalientes','Construccion'))
@app.route('/Aguascalientes/Educativo/')	
def A11():	
    return jsonify(resultadoCartera('Aguascalientes','Educativo'))
@app.route('/Aguascalientes/GobiernoFederal/')	
def A12():	
    return jsonify(resultadoCartera('Aguascalientes','GobiernoFederal'))
@app.route('/Aguascalientes/HotelesyRestaurantes/')	
def A13():	
    return jsonify(resultadoCartera('Aguascalientes','HotelesyRestaurantes'))
@app.route('/Aguascalientes/IndustriaAutomotriz/')	
def A14():	
    return jsonify(resultadoCartera('Aguascalientes','IndustriaAutomotriz'))

@app.route('/Aguascalientes/IndustriaMaterialesdeConstruccion/')	
def A15():	
    return jsonify(resultadoCartera('Aguascalientes','IndustriaMaterialesdeConstruccion'))
@app.route('/Aguascalientes/IndustriaQuimicayFarmaceutica/')	
def A16():	
    return jsonify(resultadoCartera('Aguascalientes','IndustriaQuimicayFarmaceutica'))
@app.route('/Aguascalientes/IndustriaTextilydeCalzado/')	
def A17():	
    return jsonify(resultadoCartera('Aguascalientes','IndustriaTextilydeCalzado'))
@app.route('/Aguascalientes/OrganismosInternacionales/')	
def A18():	
    return jsonify(resultadoCartera('Aguascalientes','OrganismosInternacionales'))
@app.route('/Aguascalientes/PetroleoMineriaGasyEnergia/')	
def A19():	
    return jsonify(resultadoCartera('Aguascalientes','PetroleoMineriaGasyEnergia'))
@app.route('/Aguascalientes/RestoIndustria/')	
def A20():	
    return jsonify(resultadoCartera('Aguascalientes','RestoIndustria'))
@app.route('/Aguascalientes/Salud/')	
def A21():	
    return jsonify(resultadoCartera('Aguascalientes','Salud'))
@app.route('/Aguascalientes/ServiciosComunalesySociales/')	
def A22():	
    return jsonify(resultadoCartera('Aguascalientes','ServiciosComunalesySociales'))
@app.route('/Aguascalientes/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A23():	
    return jsonify(resultadoCartera('Aguascalientes','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Aguascalientes/ServiciosFinancieros(NoBancarios)/')	
def A24():	
    return jsonify(resultadoCartera('Aguascalientes','ServiciosFinancieros(NoBancarios)'))
@app.route('/Aguascalientes/ServiciosProfesionalesyTecnicos/')	
def A25():	
    return jsonify(resultadoCartera('Aguascalientes','ServiciosProfesionalesyTecnicos'))
@app.route('/Aguascalientes/Transporte/')	
def A26():	
    return jsonify(resultadoCartera('Aguascalientes','Transporte'))
@app.route('/Aguascalientes/Bancario/')	
def A27():	
    return jsonify(resultadoCartera('Aguascalientes','Bancario'))
@app.route('/Aguascalientes/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A28():	
    return jsonify(resultadoCartera('Aguascalientes','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Aguascalientes/ServiciosFinancieros(NoBancarios)/')	
def A29():	
    return jsonify(resultadoCartera('Aguascalientes','ServiciosFinancieros(NoBancarios)'))
@app.route('/Aguascalientes/ServiciosProfesionalesyTecnicos/')	
def A30():	
    return jsonify(resultadoCartera('Aguascalientes','ServiciosProfesionalesyTecnicos'))
@app.route('/Aguascalientes/Transporte/')	
def A31():	
    return jsonify(resultadoCartera('Aguascalientes','Transporte'))
@app.route('/Aguascalientes/Bancario/')	
def A32():	
    return jsonify(resultadoCartera('Aguascalientes','Bancario'))
@app.route('/BajaCaliforniaNorte/AgriculturaSilviculturaGanaderiayPesca/')	
def A33():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/BajaCaliforniaNorte/AlimentosBebidasyTabaco/')	
def A34():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','AlimentosBebidasyTabaco'))
@app.route('/BajaCaliforniaNorte/Comercio/')	
def A35():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','Comercio'))
@app.route('/BajaCaliforniaNorte/ComunicacionesyTelecomunicaciones/')	
def A36():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','ComunicacionesyTelecomunicaciones'))
@app.route('/BajaCaliforniaNorte/Construccion/')	
def A37():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','Construccion'))
@app.route('/BajaCaliforniaNorte/Educativo/')	
def A38():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','Educativo'))
@app.route('/BajaCaliforniaNorte/GobiernoFederal/')	
def A39():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','GobiernoFederal'))
@app.route('/BajaCaliforniaNorte/HotelesyRestaurantes/')	
def A40():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','HotelesyRestaurantes'))
@app.route('/BajaCaliforniaNorte/IndustriaAutomotriz/')	
def A41():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','IndustriaAutomotriz'))
@app.route('/BajaCaliforniaNorte/IndustriaMaterialesdeConstruccion/')	
def A42():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','IndustriaMaterialesdeConstruccion'))
@app.route('/BajaCaliforniaNorte/IndustriaQuimicayFarmaceutica/')	
def A43():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','IndustriaQuimicayFarmaceutica'))
@app.route('/BajaCaliforniaNorte/IndustriaTextilydeCalzado/')	
def A44():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','IndustriaTextilydeCalzado'))
@app.route('/BajaCaliforniaNorte/OrganismosInternacionales/')	
def A45():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','OrganismosInternacionales'))
@app.route('/BajaCaliforniaNorte/PetroleoMineriaGasyEnergia/')	
def A46():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','PetroleoMineriaGasyEnergia'))
@app.route('/BajaCaliforniaNorte/RestoIndustria/')	
def A47():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','RestoIndustria'))
@app.route('/BajaCaliforniaNorte/Salud/')	
def A48():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','Salud'))
@app.route('/BajaCaliforniaNorte/ServiciosComunalesySociales/')	
def A49():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','ServiciosComunalesySociales'))
@app.route('/BajaCaliforniaNorte/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A50():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/BajaCaliforniaNorte/ServiciosFinancieros(NoBancarios)/')	
def A51():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','ServiciosFinancieros(NoBancarios)'))
@app.route('/BajaCaliforniaNorte/ServiciosProfesionalesyTecnicos/')	

def A52():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','ServiciosProfesionalesyTecnicos'))
@app.route('/BajaCaliforniaNorte/Transporte/')	
def A53():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','Transporte'))
@app.route('/BajaCaliforniaNorte/Bancario/')	
def A54():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','Bancario'))
@app.route('/BajaCaliforniaNorte/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A55():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/BajaCaliforniaNorte/ServiciosFinancieros(NoBancarios)/')	
def A56():	
    
    return jsonify(resultadoCartera('BajaCaliforniaNorte','ServiciosFinancieros(NoBancarios)'))
@app.route('/BajaCaliforniaNorte/ServiciosProfesionalesyTecnicos/')	
def A57():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','ServiciosProfesionalesyTecnicos'))
@app.route('/BajaCaliforniaNorte/Transporte/')	
def A58():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','Transporte'))
@app.route('/BajaCaliforniaNorte/Bancario/')	
def A59():	
    return jsonify(resultadoCartera('BajaCaliforniaNorte','Bancario'))
@app.route('/BajaCaliforniaSur/AgriculturaSilviculturaGanaderiayPesca/')	
def A60():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/BajaCaliforniaSur/AlimentosBebidasyTabaco/')	
def A61():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','AlimentosBebidasyTabaco'))
@app.route('/BajaCaliforniaSur/Comercio/')	
def A62():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','Comercio'))
@app.route('/BajaCaliforniaSur/ComunicacionesyTelecomunicaciones/')	
def A63():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','ComunicacionesyTelecomunicaciones'))
@app.route('/BajaCaliforniaSur/Construccion/')	
def A64():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','Construccion'))
@app.route('/BajaCaliforniaSur/Educativo/')	
def A65():	
    
    return jsonify(resultadoCartera('BajaCaliforniaSur','Educativo'))
@app.route('/BajaCaliforniaSur/GobiernoFederal/')	
def A66():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','GobiernoFederal'))
@app.route('/BajaCaliforniaSur/HotelesyRestaurantes/')	
def A67():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','HotelesyRestaurantes'))
@app.route('/BajaCaliforniaSur/IndustriaAutomotriz/')	
def A68():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','IndustriaAutomotriz'))
@app.route('/BajaCaliforniaSur/IndustriaMaterialesdeConstruccion/')	

def A69():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','IndustriaMaterialesdeConstruccion'))
@app.route('/BajaCaliforniaSur/IndustriaQuimicayFarmaceutica/')	
def A70():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','IndustriaQuimicayFarmaceutica'))
@app.route('/BajaCaliforniaSur/IndustriaTextilydeCalzado/')	
def A71():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','IndustriaTextilydeCalzado'))
@app.route('/BajaCaliforniaSur/OrganismosInternacionales/')	
def A72():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','OrganismosInternacionales'))
@app.route('/BajaCaliforniaSur/PetroleoMineriaGasyEnergia/')	
def A73():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','PetroleoMineriaGasyEnergia'))
@app.route('/BajaCaliforniaSur/RestoIndustria/')	
def A74():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','RestoIndustria'))
@app.route('/BajaCaliforniaSur/Salud/')	
def A75():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','Salud'))
@app.route('/BajaCaliforniaSur/ServiciosComunalesySociales/')	
def A76():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','ServiciosComunalesySociales'))
@app.route('/BajaCaliforniaSur/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A77():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/BajaCaliforniaSur/ServiciosFinancieros(NoBancarios)/')	
def A78():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','ServiciosFinancieros(NoBancarios)'))
@app.route('/BajaCaliforniaSur/ServiciosProfesionalesyTecnicos/')	
def A79():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','ServiciosProfesionalesyTecnicos'))
@app.route('/BajaCaliforniaSur/Transporte/')	
def A80():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','Transporte'))
@app.route('/BajaCaliforniaSur/Bancario/')	
def A81():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','Bancario'))
@app.route('/BajaCaliforniaSur/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A82():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/BajaCaliforniaSur/ServiciosFinancieros(NoBancarios)/')	
def A83():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','ServiciosFinancieros(NoBancarios)'))
@app.route('/BajaCaliforniaSur/ServiciosProfesionalesyTecnicos/')	
def A84():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','ServiciosProfesionalesyTecnicos'))
@app.route('/BajaCaliforniaSur/Transporte/')	
def A85():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','Transporte'))
@app.route('/BajaCaliforniaSur/Bancario/')	
def A86():	
    return jsonify(resultadoCartera('BajaCaliforniaSur','Bancario'))
@app.route('/Campeche/AgriculturaSilviculturaGanaderiayPesca/')	
def A87():	
    return jsonify(resultadoCartera('Campeche','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Campeche/AlimentosBebidasyTabaco/')	
def A88():	
    
    return jsonify(resultadoCartera('Campeche','AlimentosBebidasyTabaco'))
@app.route('/Campeche/Comercio/')	
def A89():	
    return jsonify(resultadoCartera('Campeche','Comercio'))
@app.route('/Campeche/ComunicacionesyTelecomunicaciones/')	
def A90():	
    return jsonify(resultadoCartera('Campeche','ComunicacionesyTelecomunicaciones'))
@app.route('/Campeche/Construccion/')	
def A91():	
    return jsonify(resultadoCartera('Campeche','Construccion'))
@app.route('/Campeche/Educativo/')	
def A92():	
    return jsonify(resultadoCartera('Campeche','Educativo'))
@app.route('/Campeche/GobiernoFederal/')	
def A93():	
    return jsonify(resultadoCartera('Campeche','GobiernoFederal'))
@app.route('/Campeche/HotelesyRestaurantes/')	
def A94():	
    return jsonify(resultadoCartera('Campeche','HotelesyRestaurantes'))
@app.route('/Campeche/IndustriaAutomotriz/')	
def A95():	
    return jsonify(resultadoCartera('Campeche','IndustriaAutomotriz'))
@app.route('/Campeche/IndustriaMaterialesdeConstruccion/')	
def A96():	
    return jsonify(resultadoCartera('Campeche','IndustriaMaterialesdeConstruccion'))
@app.route('/Campeche/IndustriaQuimicayFarmaceutica/')	
def A97():	
    return jsonify(resultadoCartera('Campeche','IndustriaQuimicayFarmaceutica'))
@app.route('/Campeche/IndustriaTextilydeCalzado/')	
def A98():	
    return jsonify(resultadoCartera('Campeche','IndustriaTextilydeCalzado'))
@app.route('/Campeche/OrganismosInternacionales/')	
def A99():	
    return jsonify(resultadoCartera('Campeche','OrganismosInternacionales'))
@app.route('/Campeche/PetroleoMineriaGasyEnergia/')	
def A100():	
    return jsonify(resultadoCartera('Campeche','PetroleoMineriaGasyEnergia'))
@app.route('/Campeche/RestoIndustria/')	
def A101():	
    return jsonify(resultadoCartera('Campeche','RestoIndustria'))
@app.route('/Campeche/Salud/')	
def A102():	
    return jsonify(resultadoCartera('Campeche','Salud'))
@app.route('/Campeche/ServiciosComunalesySociales/')	
def A103():	
    return jsonify(resultadoCartera('Campeche','ServiciosComunalesySociales'))
@app.route('/Campeche/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A104():	
    return jsonify(resultadoCartera('Campeche','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Campeche/ServiciosFinancieros(NoBancarios)/')	
def A105():	
    return jsonify(resultadoCartera('Campeche','ServiciosFinancieros(NoBancarios)'))
@app.route('/Campeche/ServiciosProfesionalesyTecnicos/')	
def A106():	
    return jsonify(resultadoCartera('Campeche','ServiciosProfesionalesyTecnicos'))
@app.route('/Campeche/Transporte/')	
def A107():	
    
    return jsonify(resultadoCartera('Campeche','Transporte'))
@app.route('/Campeche/Bancario/')	
def A108():	
    
    return jsonify(resultadoCartera('Campeche','Bancario'))
@app.route('/Campeche/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A109():	
    return jsonify(resultadoCartera('Campeche','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Campeche/ServiciosFinancieros(NoBancarios)/')	
def A110():	
    return jsonify(resultadoCartera('Campeche','ServiciosFinancieros(NoBancarios)'))
@app.route('/Campeche/ServiciosProfesionalesyTecnicos/')	
def A111():	
    return jsonify(resultadoCartera('Campeche','ServiciosProfesionalesyTecnicos'))
@app.route('/Campeche/Transporte/')	
def A112():	
    return jsonify(resultadoCartera('Campeche','Transporte'))
@app.route('/Campeche/Bancario/')	

def A113():	
    return jsonify(resultadoCartera('Campeche','Bancario'))
@app.route('/Chiapas/AgriculturaSilviculturaGanaderiayPesca/')	
def A114():	
    return jsonify(resultadoCartera('Chiapas','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Chiapas/AlimentosBebidasyTabaco/')	
def A115():	
    return jsonify(resultadoCartera('Chiapas','AlimentosBebidasyTabaco'))
@app.route('/Chiapas/Comercio/')	
def A116():	
    return jsonify(resultadoCartera('Chiapas','Comercio'))
@app.route('/Chiapas/ComunicacionesyTelecomunicaciones/')	
def A117():	
    return jsonify(resultadoCartera('Chiapas','ComunicacionesyTelecomunicaciones'))
@app.route('/Chiapas/Construccion/')	
def A118():	
    return jsonify(resultadoCartera('Chiapas','Construccion'))
@app.route('/Chiapas/Educativo/')	
def A119():	
    return jsonify(resultadoCartera('Chiapas','Educativo'))
@app.route('/Chiapas/GobiernoFederal/')	
def A120():	
    return jsonify(resultadoCartera('Chiapas','GobiernoFederal'))
@app.route('/Chiapas/HotelesyRestaurantes/')	
def A121():	
    return jsonify(resultadoCartera('Chiapas','HotelesyRestaurantes'))
@app.route('/Chiapas/IndustriaAutomotriz/')	
def A122():	
    return jsonify(resultadoCartera('Chiapas','IndustriaAutomotriz'))
@app.route('/Chiapas/IndustriaMaterialesdeConstruccion/')	
def A123():	
    return jsonify(resultadoCartera('Chiapas','IndustriaMaterialesdeConstruccion'))
@app.route('/Chiapas/IndustriaQuimicayFarmaceutica/')	
def A124():	
    return jsonify(resultadoCartera('Chiapas','IndustriaQuimicayFarmaceutica'))
@app.route('/Chiapas/IndustriaTextilydeCalzado/')	
def A125():	
    return jsonify(resultadoCartera('Chiapas','IndustriaTextilydeCalzado'))
@app.route('/Chiapas/OrganismosInternacionales/')	
def A126():	
    return jsonify(resultadoCartera('Chiapas','OrganismosInternacionales'))
@app.route('/Chiapas/PetroleoMineriaGasyEnergia/')	
def A127():	
    return jsonify(resultadoCartera('Chiapas','PetroleoMineriaGasyEnergia'))
@app.route('/Chiapas/RestoIndustria/')	
def A128():	
    return jsonify(resultadoCartera('Chiapas','RestoIndustria'))
@app.route('/Chiapas/Salud/')	
def A129():	
    return jsonify(resultadoCartera('Chiapas','Salud'))
@app.route('/Chiapas/ServiciosComunalesySociales/')	
def A130():	
    return jsonify(resultadoCartera('Chiapas','ServiciosComunalesySociales'))
@app.route('/Chiapas/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A131():	
    return jsonify(resultadoCartera('Chiapas','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Chiapas/ServiciosFinancieros(NoBancarios)/')	
def A132():	
    return jsonify(resultadoCartera('Chiapas','ServiciosFinancieros(NoBancarios)'))
@app.route('/Chiapas/ServiciosProfesionalesyTecnicos/')	
def A133():	
    return jsonify(resultadoCartera('Chiapas','ServiciosProfesionalesyTecnicos'))
@app.route('/Chiapas/Transporte/')	
def A134():	
    return jsonify(resultadoCartera('Chiapas','Transporte'))
@app.route('/Chiapas/Bancario/')	
def A135():	
    return jsonify(resultadoCartera('Chiapas','Bancario'))
@app.route('/Chiapas/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A136():	
    return jsonify(resultadoCartera('Chiapas','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Chiapas/ServiciosFinancieros(NoBancarios)/')	
def A137():	
    return jsonify(resultadoCartera('Chiapas','ServiciosFinancieros(NoBancarios)'))
@app.route('/Chiapas/ServiciosProfesionalesyTecnicos/')	
def A138():	
    return jsonify(resultadoCartera('Chiapas','ServiciosProfesionalesyTecnicos'))
@app.route('/Chiapas/Transporte/')	
def A139():	
    return jsonify(resultadoCartera('Chiapas','Transporte'))
@app.route('/Chiapas/Bancario/')	
def A140():	
    return jsonify(resultadoCartera('Chiapas','Bancario'))
@app.route('/Chihuahua/AgriculturaSilviculturaGanaderiayPesca/')	
def A141():	
    return jsonify(resultadoCartera('Chihuahua','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Chihuahua/AlimentosBebidasyTabaco/')	
def A142():	
    return jsonify(resultadoCartera('Chihuahua','AlimentosBebidasyTabaco'))
@app.route('/Chihuahua/Comercio/')	
def A143():	
    
    return jsonify(resultadoCartera('Chihuahua','Comercio'))
@app.route('/Chihuahua/ComunicacionesyTelecomunicaciones/')	
def A144():	
    return jsonify(resultadoCartera('Chihuahua','ComunicacionesyTelecomunicaciones'))
@app.route('/Chihuahua/Construccion/')	
def A145():	
    return jsonify(resultadoCartera('Chihuahua','Construccion'))
@app.route('/Chihuahua/Educativo/')	
def A146():	
    return jsonify(resultadoCartera('Chihuahua','Educativo'))
@app.route('/Chihuahua/GobiernoFederal/')	
def A147():	
    return jsonify(resultadoCartera('Chihuahua','GobiernoFederal'))
@app.route('/Chihuahua/HotelesyRestaurantes/')	
def A148():	
    return jsonify(resultadoCartera('Chihuahua','HotelesyRestaurantes'))
@app.route('/Chihuahua/IndustriaAutomotriz/')	
def A149():	
    return jsonify(resultadoCartera('Chihuahua','IndustriaAutomotriz'))
@app.route('/Chihuahua/IndustriaMaterialesdeConstruccion/')	
def A150():	
    return jsonify(resultadoCartera('Chihuahua','IndustriaMaterialesdeConstruccion'))
@app.route('/Chihuahua/IndustriaQuimicayFarmaceutica/')	
def A151():	
    return jsonify(resultadoCartera('Chihuahua','IndustriaQuimicayFarmaceutica'))
@app.route('/Chihuahua/IndustriaTextilydeCalzado/')	
def A152():	
    return jsonify(resultadoCartera('Chihuahua','IndustriaTextilydeCalzado'))
@app.route('/Chihuahua/OrganismosInternacionales/')	
def A153():	
    return jsonify(resultadoCartera('Chihuahua','OrganismosInternacionales'))
@app.route('/Chihuahua/PetroleoMineriaGasyEnergia/')	
def A154():	
    return jsonify(resultadoCartera('Chihuahua','PetroleoMineriaGasyEnergia'))
@app.route('/Chihuahua/RestoIndustria/')	
def A155():	
    return jsonify(resultadoCartera('Chihuahua','RestoIndustria'))
@app.route('/Chihuahua/Salud/')	
def A156():	
    return jsonify(resultadoCartera('Chihuahua','Salud'))
@app.route('/Chihuahua/ServiciosComunalesySociales/')	
def A157():	
    return jsonify(resultadoCartera('Chihuahua','ServiciosComunalesySociales'))
@app.route('/Chihuahua/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A158():	
    return jsonify(resultadoCartera('Chihuahua','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Chihuahua/ServiciosFinancieros(NoBancarios)/')	
def A159():	
    return jsonify(resultadoCartera('Chihuahua','ServiciosFinancieros(NoBancarios)'))
@app.route('/Chihuahua/ServiciosProfesionalesyTecnicos/')	
def A160():	
    return jsonify(resultadoCartera('Chihuahua','ServiciosProfesionalesyTecnicos'))
@app.route('/Chihuahua/Transporte/')	
def A161():	
    return jsonify(resultadoCartera('Chihuahua','Transporte'))
@app.route('/Chihuahua/Bancario/')	
def A162():	
    return jsonify(resultadoCartera('Chihuahua','Bancario'))
@app.route('/CiudaddeMexico/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A163():	
    return jsonify(resultadoCartera('CiudaddeMexico','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/CiudaddeMexico/ServiciosFinancieros(NoBancarios)/')	
def A164():	
    return jsonify(resultadoCartera('CiudaddeMexico','ServiciosFinancieros(NoBancarios)'))
@app.route('/CiudaddeMexico/ServiciosProfesionalesyTecnicos/')	
def A165():	
    return jsonify(resultadoCartera('CiudaddeMexico','ServiciosProfesionalesyTecnicos'))
@app.route('/CiudaddeMexico/Transporte/')	

def A166():	
    return jsonify(resultadoCartera('CiudaddeMexico','Transporte'))
@app.route('/CiudaddeMexico/Bancario/')	
def A167():	
    return jsonify(resultadoCartera('CiudaddeMexico','Bancario'))
@app.route('/CiudaddeMexico/AgriculturaSilviculturaGanaderiayPesca/')	
def A168():	
    
    return jsonify(resultadoCartera('CiudaddeMexico','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/CiudaddeMexico/AlimentosBebidasyTabaco/')	
def A169():	
    return jsonify(resultadoCartera('CiudaddeMexico','AlimentosBebidasyTabaco'))
@app.route('/CiudaddeMexico/Comercio/')	
def A170():	
    return jsonify(resultadoCartera('CiudaddeMexico','Comercio'))
@app.route('/CiudaddeMexico/ComunicacionesyTelecomunicaciones/')	
def A171():	
    return jsonify(resultadoCartera('CiudaddeMexico','ComunicacionesyTelecomunicaciones'))
@app.route('/CiudaddeMexico/Construccion/')	
def A172():	
    return jsonify(resultadoCartera('CiudaddeMexico','Construccion'))
@app.route('/CiudaddeMexico/Educativo/')	
def A173():	
    return jsonify(resultadoCartera('CiudaddeMexico','Educativo'))
@app.route('/CiudaddeMexico/GobiernoFederal/')	
def A174():	
    return jsonify(resultadoCartera('CiudaddeMexico','GobiernoFederal'))
@app.route('/CiudaddeMexico/HotelesyRestaurantes/')	
def A175():	
    return jsonify(resultadoCartera('CiudaddeMexico','HotelesyRestaurantes'))
@app.route('/CiudaddeMexico/IndustriaAutomotriz/')	
def A176():	
    return jsonify(resultadoCartera('CiudaddeMexico','IndustriaAutomotriz'))
@app.route('/CiudaddeMexico/IndustriaMaterialesdeConstruccion/')	
def A177():	
    return jsonify(resultadoCartera('CiudaddeMexico','IndustriaMaterialesdeConstruccion'))
@app.route('/CiudaddeMexico/IndustriaQuimicayFarmaceutica/')	
def A178():	
    return jsonify(resultadoCartera('CiudaddeMexico','IndustriaQuimicayFarmaceutica'))
@app.route('/CiudaddeMexico/IndustriaTextilydeCalzado/')	
def A179():	
    return jsonify(resultadoCartera('CiudaddeMexico','IndustriaTextilydeCalzado'))
@app.route('/CiudaddeMexico/OrganismosInternacionales/')	
def A180():	
    return jsonify(resultadoCartera('CiudaddeMexico','OrganismosInternacionales'))
@app.route('/CiudaddeMexico/PetroleoMineriaGasyEnergia/')	
def A181():	
    return jsonify(resultadoCartera('CiudaddeMexico','PetroleoMineriaGasyEnergia'))
@app.route('/CiudaddeMexico/RestoIndustria/')	
def A182():	
    return jsonify(resultadoCartera('CiudaddeMexico','RestoIndustria'))
@app.route('/CiudaddeMexico/Salud/')	
def A183():	
    return jsonify(resultadoCartera('CiudaddeMexico','Salud'))
@app.route('/CiudaddeMexico/ServiciosComunalesySociales/')	
def A184():	
    return jsonify(resultadoCartera('CiudaddeMexico','ServiciosComunalesySociales'))
@app.route('/CiudaddeMexico/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A185():	
    return jsonify(resultadoCartera('CiudaddeMexico','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/CiudaddeMexico/ServiciosFinancieros(NoBancarios)/')	
def A186():	
    return jsonify(resultadoCartera('CiudaddeMexico','ServiciosFinancieros(NoBancarios)'))
@app.route('/CiudaddeMexico/ServiciosProfesionalesyTecnicos/')	
def A187():	
    return jsonify(resultadoCartera('CiudaddeMexico','ServiciosProfesionalesyTecnicos'))
@app.route('/CiudaddeMexico/Transporte/')	
def A188():	
    return jsonify(resultadoCartera('CiudaddeMexico','Transporte'))
@app.route('/CiudaddeMexico/Bancario/')	
def A189():	
    
    return jsonify(resultadoCartera('CiudaddeMexico','Bancario'))
@app.route('/Coahuila/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A190():	
    return jsonify(resultadoCartera('Coahuila','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Coahuila/ServiciosFinancieros(NoBancarios)/')	
def A191():	
    return jsonify(resultadoCartera('Coahuila','ServiciosFinancieros(NoBancarios)'))
@app.route('/Coahuila/ServiciosProfesionalesyTecnicos/')	
def A192():	
    return jsonify(resultadoCartera('Coahuila','ServiciosProfesionalesyTecnicos'))
@app.route('/Coahuila/Transporte/')	
def A193():	
    return jsonify(resultadoCartera('Coahuila','Transporte'))
@app.route('/Coahuila/Bancario/')	
def A194():	
    return jsonify(resultadoCartera('Coahuila','Bancario'))
@app.route('/Coahuila/AgriculturaSilviculturaGanaderiayPesca/')	
def A195():	
    return jsonify(resultadoCartera('Coahuila','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Coahuila/AlimentosBebidasyTabaco/')	
def A196():	
    return jsonify(resultadoCartera('Coahuila','AlimentosBebidasyTabaco'))
@app.route('/Coahuila/Comercio/')	
def A197():	
    return jsonify(resultadoCartera('Coahuila','Comercio'))
@app.route('/Coahuila/ComunicacionesyTelecomunicaciones/')	
def A198():	
    return jsonify(resultadoCartera('Coahuila','ComunicacionesyTelecomunicaciones'))
@app.route('/Coahuila/Construccion/')	
def A199():	
    return jsonify(resultadoCartera('Coahuila','Construccion'))
@app.route('/Coahuila/Educativo/')	
def A200():	
    return jsonify(resultadoCartera('Coahuila','Educativo'))
@app.route('/Coahuila/GobiernoFederal/')	
def A201():	
    return jsonify(resultadoCartera('Coahuila','GobiernoFederal'))
@app.route('/Coahuila/HotelesyRestaurantes/')	
def A202():	
    return jsonify(resultadoCartera('Coahuila','HotelesyRestaurantes'))
@app.route('/Coahuila/IndustriaAutomotriz/')	
def A203():	
    return jsonify(resultadoCartera('Coahuila','IndustriaAutomotriz'))
@app.route('/Coahuila/IndustriaMaterialesdeConstruccion/')	
def A204():	
    return jsonify(resultadoCartera('Coahuila','IndustriaMaterialesdeConstruccion'))
@app.route('/Coahuila/IndustriaQuimicayFarmaceutica/')	
def A205():	
    return jsonify(resultadoCartera('Coahuila','IndustriaQuimicayFarmaceutica'))
@app.route('/Coahuila/IndustriaTextilydeCalzado/')	
def A206():	
    return jsonify(resultadoCartera('Coahuila','IndustriaTextilydeCalzado'))
@app.route('/Coahuila/OrganismosInternacionales/')	
def A207():	
    return jsonify(resultadoCartera('Coahuila','OrganismosInternacionales'))
@app.route('/Coahuila/PetroleoMineriaGasyEnergia/')	
def A208():	
    return jsonify(resultadoCartera('Coahuila','PetroleoMineriaGasyEnergia'))
@app.route('/Coahuila/RestoIndustria/')	
def A209():	
    return jsonify(resultadoCartera('Coahuila','RestoIndustria'))
@app.route('/Coahuila/Salud/')	
def A210():	
    return jsonify(resultadoCartera('Coahuila','Salud'))
@app.route('/Coahuila/ServiciosComunalesySociales/')	
def A211():	
    return jsonify(resultadoCartera('Coahuila','ServiciosComunalesySociales'))
@app.route('/Coahuila/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A212():	
    return jsonify(resultadoCartera('Coahuila','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Coahuila/ServiciosFinancieros(NoBancarios)/')	
def A213():	
    return jsonify(resultadoCartera('Coahuila','ServiciosFinancieros(NoBancarios)'))
@app.route('/Coahuila/ServiciosProfesionalesyTecnicos/')	
def A214():	
    return jsonify(resultadoCartera('Coahuila','ServiciosProfesionalesyTecnicos'))
@app.route('/Coahuila/Transporte/')	
def A215():	
    return jsonify(resultadoCartera('Coahuila','Transporte'))
@app.route('/Coahuila/Bancario/')	
def A216():	
    return jsonify(resultadoCartera('Coahuila','Bancario'))
@app.route('/Colima/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A217():	
    return jsonify(resultadoCartera('Colima','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Colima/ServiciosFinancieros(NoBancarios)/')	
def A218():	
    return jsonify(resultadoCartera('Colima','ServiciosFinancieros(NoBancarios)'))
@app.route('/Colima/ServiciosProfesionalesyTecnicos/')	
def A219():	
    return jsonify(resultadoCartera('Colima','ServiciosProfesionalesyTecnicos'))
@app.route('/Colima/Transporte/')	
def A220():	
    return jsonify(resultadoCartera('Colima','Transporte'))
@app.route('/Colima/Bancario/')	
def A221():	
    return jsonify(resultadoCartera('Colima','Bancario'))
@app.route('/Colima/AgriculturaSilviculturaGanaderiayPesca/')	
def A222():	
    return jsonify(resultadoCartera('Colima','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Colima/AlimentosBebidasyTabaco/')	
def A223():	
    return jsonify(resultadoCartera('Colima','AlimentosBebidasyTabaco'))
@app.route('/Colima/Comercio/')	
def A224():	
    return jsonify(resultadoCartera('Colima','Comercio'))
@app.route('/Colima/ComunicacionesyTelecomunicaciones/')	
def A225():	
    return jsonify(resultadoCartera('Colima','ComunicacionesyTelecomunicaciones'))
@app.route('/Colima/Construccion/')	
def A226():	
    return jsonify(resultadoCartera('Colima','Construccion'))
@app.route('/Colima/Educativo/')	
def A227():	
    return jsonify(resultadoCartera('Colima','Educativo'))
@app.route('/Colima/GobiernoFederal/')	
def A228():	
    return jsonify(resultadoCartera('Colima','GobiernoFederal'))
@app.route('/Colima/HotelesyRestaurantes/')	
def A229():	
    return jsonify(resultadoCartera('Colima','HotelesyRestaurantes'))
@app.route('/Colima/IndustriaAutomotriz/')	
def A230():	
    return jsonify(resultadoCartera('Colima','IndustriaAutomotriz'))
@app.route('/Colima/IndustriaMaterialesdeConstruccion/')	
def A231():	
    return jsonify(resultadoCartera('Colima','IndustriaMaterialesdeConstruccion'))
@app.route('/Colima/IndustriaQuimicayFarmaceutica/')	
def A232():	
    return jsonify(resultadoCartera('Colima','IndustriaQuimicayFarmaceutica'))
@app.route('/Colima/IndustriaTextilydeCalzado/')	
def A233():	
    return jsonify(resultadoCartera('Colima','IndustriaTextilydeCalzado'))
@app.route('/Colima/OrganismosInternacionales/')	
def A234():	
    return jsonify(resultadoCartera('Colima','OrganismosInternacionales'))
@app.route('/Colima/PetroleoMineriaGasyEnergia/')	
def A235():	
    return jsonify(resultadoCartera('Colima','PetroleoMineriaGasyEnergia'))
@app.route('/Colima/RestoIndustria/')	
def A236():	
    return jsonify(resultadoCartera('Colima','RestoIndustria'))
@app.route('/Colima/Salud/')	
def A237():	
    
    return jsonify(resultadoCartera('Colima','Salud'))
@app.route('/Colima/ServiciosComunalesySociales/')	
def A238():	
    return jsonify(resultadoCartera('Colima','ServiciosComunalesySociales'))
@app.route('/Colima/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A239():	
    return jsonify(resultadoCartera('Colima','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Colima/ServiciosFinancieros(NoBancarios)/')	
def A240():	
    return jsonify(resultadoCartera('Colima','ServiciosFinancieros(NoBancarios)'))
@app.route('/Colima/ServiciosProfesionalesyTecnicos/')	
def A241():	
    return jsonify(resultadoCartera('Colima','ServiciosProfesionalesyTecnicos'))
@app.route('/Colima/Transporte/')	
def A242():	
    return jsonify(resultadoCartera('Colima','Transporte'))
@app.route('/Colima/Bancario/')	
def A243():	
    return jsonify(resultadoCartera('Colima','Bancario'))
@app.route('/Durango/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A244():	
    return jsonify(resultadoCartera('Durango','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Durango/ServiciosFinancieros(NoBancarios)/')	
def A245():	
    return jsonify(resultadoCartera('Durango','ServiciosFinancieros(NoBancarios)'))
@app.route('/Durango/ServiciosProfesionalesyTecnicos/')	
def A246():	
    return jsonify(resultadoCartera('Durango','ServiciosProfesionalesyTecnicos'))
@app.route('/Durango/Transporte/')	
def A247():	
    return jsonify(resultadoCartera('Durango','Transporte'))
@app.route('/Durango/Bancario/')	
def A248():	
    return jsonify(resultadoCartera('Durango','Bancario'))
@app.route('/Durango/AgriculturaSilviculturaGanaderiayPesca/')	
def A249():	
    return jsonify(resultadoCartera('Durango','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Durango/AlimentosBebidasyTabaco/')	
def A250():	
    return jsonify(resultadoCartera('Durango','AlimentosBebidasyTabaco'))
@app.route('/Durango/Comercio/')	
def A251():	
    
    return jsonify(resultadoCartera('Durango','Comercio'))
@app.route('/Durango/ComunicacionesyTelecomunicaciones/')	
def A252():	
    return jsonify(resultadoCartera('Durango','ComunicacionesyTelecomunicaciones'))
@app.route('/Durango/Construccion/')	
def A253():	
    return jsonify(resultadoCartera('Durango','Construccion'))
@app.route('/Durango/Educativo/')	
def A254():	
    return jsonify(resultadoCartera('Durango','Educativo'))
@app.route('/Durango/GobiernoFederal/')	

def A255():	
    return jsonify(resultadoCartera('Durango','GobiernoFederal'))
@app.route('/Durango/HotelesyRestaurantes/')	
def A256():	
    return jsonify(resultadoCartera('Durango','HotelesyRestaurantes'))
@app.route('/Durango/IndustriaAutomotriz/')	
def A257():	
    return jsonify(resultadoCartera('Durango','IndustriaAutomotriz'))
@app.route('/Durango/IndustriaMaterialesdeConstruccion/')	
def A258():	
    return jsonify(resultadoCartera('Durango','IndustriaMaterialesdeConstruccion'))
@app.route('/Durango/IndustriaQuimicayFarmaceutica/')	
def A259():	
    return jsonify(resultadoCartera('Durango','IndustriaQuimicayFarmaceutica'))
@app.route('/Durango/IndustriaTextilydeCalzado/')	
def A260():	
    return jsonify(resultadoCartera('Durango','IndustriaTextilydeCalzado'))
@app.route('/Durango/OrganismosInternacionales/')	
def A261():	
    return jsonify(resultadoCartera('Durango','OrganismosInternacionales'))
@app.route('/Durango/PetroleoMineriaGasyEnergia/')	
def A262():	
    return jsonify(resultadoCartera('Durango','PetroleoMineriaGasyEnergia'))
@app.route('/Durango/RestoIndustria/')	
def A263():	
    return jsonify(resultadoCartera('Durango','RestoIndustria'))
@app.route('/Durango/Salud/')	
def A264():	
    return jsonify(resultadoCartera('Durango','Salud'))
@app.route('/Durango/ServiciosComunalesySociales/')	
def A265():	
    return jsonify(resultadoCartera('Durango','ServiciosComunalesySociales'))
@app.route('/Durango/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A266():	
    return jsonify(resultadoCartera('Durango','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Durango/ServiciosFinancieros(NoBancarios)/')	
def A267():	
    return jsonify(resultadoCartera('Durango','ServiciosFinancieros(NoBancarios)'))
@app.route('/Durango/ServiciosProfesionalesyTecnicos/')	
def A268():	
    return jsonify(resultadoCartera('Durango','ServiciosProfesionalesyTecnicos'))
@app.route('/Durango/Transporte/')	
def A269():	
    return jsonify(resultadoCartera('Durango','Transporte'))
@app.route('/Durango/Bancario/')	
def A270():	
    return jsonify(resultadoCartera('Durango','Bancario'))
@app.route('/EstadodeMexico/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A271():	
    return jsonify(resultadoCartera('EstadodeMexico','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/EstadodeMexico/ServiciosFinancieros(NoBancarios)/')	
def A272():	
    return jsonify(resultadoCartera('EstadodeMexico','ServiciosFinancieros(NoBancarios)'))
@app.route('/EstadodeMexico/ServiciosProfesionalesyTecnicos/')	
def A273():	
    return jsonify(resultadoCartera('EstadodeMexico','ServiciosProfesionalesyTecnicos'))
@app.route('/EstadodeMexico/Transporte/')	
def A274():	
    return jsonify(resultadoCartera('EstadodeMexico','Transporte'))
@app.route('/EstadodeMexico/Bancario/')	
def A275():	
    return jsonify(resultadoCartera('EstadodeMexico','Bancario'))
@app.route('/EstadodeMexico/AgriculturaSilviculturaGanaderiayPesca/')	
def A276():	
    return jsonify(resultadoCartera('EstadodeMexico','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/EstadodeMexico/AlimentosBebidasyTabaco/')	
def A277():	
    return jsonify(resultadoCartera('EstadodeMexico','AlimentosBebidasyTabaco'))
@app.route('/EstadodeMexico/Comercio/')	
def A278():	
    return jsonify(resultadoCartera('EstadodeMexico','Comercio'))
@app.route('/EstadodeMexico/ComunicacionesyTelecomunicaciones/')	
def A279():	
    return jsonify(resultadoCartera('EstadodeMexico','ComunicacionesyTelecomunicaciones'))
@app.route('/EstadodeMexico/Construccion/')	
def A280():	
    return jsonify(resultadoCartera('EstadodeMexico','Construccion'))
@app.route('/EstadodeMexico/Educativo/')	
def A281():	
    return jsonify(resultadoCartera('EstadodeMexico','Educativo'))
@app.route('/EstadodeMexico/GobiernoFederal/')	
def A282():	
    return jsonify(resultadoCartera('EstadodeMexico','GobiernoFederal'))
@app.route('/EstadodeMexico/HotelesyRestaurantes/')	
def A283():	
    return jsonify(resultadoCartera('EstadodeMexico','HotelesyRestaurantes'))
@app.route('/EstadodeMexico/IndustriaAutomotriz/')	
def A284():	
    return jsonify(resultadoCartera('EstadodeMexico','IndustriaAutomotriz'))
@app.route('/EstadodeMexico/IndustriaMaterialesdeConstruccion/')	
def A285():	
    return jsonify(resultadoCartera('EstadodeMexico','IndustriaMaterialesdeConstruccion'))
@app.route('/EstadodeMexico/IndustriaQuimicayFarmaceutica/')	
def A286():	
    return jsonify(resultadoCartera('EstadodeMexico','IndustriaQuimicayFarmaceutica'))
@app.route('/EstadodeMexico/IndustriaTextilydeCalzado/')	

def A287():	return jsonify(resultadoCartera('EstadodeMexico','IndustriaTextilydeCalzado'))
@app.route('/EstadodeMexico/OrganismosInternacionales/')	
def A288():	
    return jsonify(resultadoCartera('EstadodeMexico','OrganismosInternacionales'))
@app.route('/EstadodeMexico/PetroleoMineriaGasyEnergia/')	
def A289():	
    return jsonify(resultadoCartera('EstadodeMexico','PetroleoMineriaGasyEnergia'))
@app.route('/EstadodeMexico/RestoIndustria/')	
def A290():	
    return jsonify(resultadoCartera('EstadodeMexico','RestoIndustria'))
@app.route('/EstadodeMexico/Salud/')	
def A291():	
    return jsonify(resultadoCartera('EstadodeMexico','Salud'))
@app.route('/EstadodeMexico/ServiciosComunalesySociales/')	
def A292():	
    return jsonify(resultadoCartera('EstadodeMexico','ServiciosComunalesySociales'))
@app.route('/EstadodeMexico/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A293():	
    return jsonify(resultadoCartera('EstadodeMexico','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/EstadodeMexico/ServiciosFinancieros(NoBancarios)/')	
def A294():	
    return jsonify(resultadoCartera('EstadodeMexico','ServiciosFinancieros(NoBancarios)'))
@app.route('/EstadodeMexico/ServiciosProfesionalesyTecnicos/')	
def A295():	
    return jsonify(resultadoCartera('EstadodeMexico','ServiciosProfesionalesyTecnicos'))
@app.route('/EstadodeMexico/Transporte/')	
def A296():	
    return jsonify(resultadoCartera('EstadodeMexico','Transporte'))
@app.route('/EstadodeMexico/Bancario/')	
def A297():	
    return jsonify(resultadoCartera('EstadodeMexico','Bancario'))
@app.route('/Guanajuato/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A298():	
    return jsonify(resultadoCartera('Guanajuato','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Guanajuato/ServiciosFinancieros(NoBancarios)/')	
def A299():	
    return jsonify(resultadoCartera('Guanajuato','ServiciosFinancieros(NoBancarios)'))
@app.route('/Guanajuato/ServiciosProfesionalesyTecnicos/')	
def A300():	
    return jsonify(resultadoCartera('Guanajuato','ServiciosProfesionalesyTecnicos'))
@app.route('/Guanajuato/Transporte/')	
def A301():	
    return jsonify(resultadoCartera('Guanajuato','Transporte'))
@app.route('/Guanajuato/Bancario/')	
def A302():	
    return jsonify(resultadoCartera('Guanajuato','Bancario'))
@app.route('/Guanajuato/AgriculturaSilviculturaGanaderiayPesca/')	
def A303():	
    return jsonify(resultadoCartera('Guanajuato','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Guanajuato/AlimentosBebidasyTabaco/')	
def A304():	
    return jsonify(resultadoCartera('Guanajuato','AlimentosBebidasyTabaco'))
@app.route('/Guanajuato/Comercio/')	
def A305():	
    return jsonify(resultadoCartera('Guanajuato','Comercio'))
@app.route('/Guanajuato/ComunicacionesyTelecomunicaciones/')	
def A306():	
    return jsonify(resultadoCartera('Guanajuato','ComunicacionesyTelecomunicaciones'))
@app.route('/Guanajuato/Construccion/')	
def A307():	
    return jsonify(resultadoCartera('Guanajuato','Construccion'))
@app.route('/Guanajuato/Educativo/')	
def A308():	
    return jsonify(resultadoCartera('Guanajuato','Educativo'))
@app.route('/Guanajuato/GobiernoFederal/')	
def A309():	
    return jsonify(resultadoCartera('Guanajuato','GobiernoFederal'))
@app.route('/Guanajuato/HotelesyRestaurantes/')	
def A310():	
    return jsonify(resultadoCartera('Guanajuato','HotelesyRestaurantes'))
@app.route('/Guanajuato/IndustriaAutomotriz/')	
def A311():	
    return jsonify(resultadoCartera('Guanajuato','IndustriaAutomotriz'))
@app.route('/Guanajuato/IndustriaMaterialesdeConstruccion/')	
def A312():	
    return jsonify(resultadoCartera('Guanajuato','IndustriaMaterialesdeConstruccion'))
@app.route('/Guanajuato/IndustriaQuimicayFarmaceutica/')	
def A313():	
    return jsonify(resultadoCartera('Guanajuato','IndustriaQuimicayFarmaceutica'))
@app.route('/Guanajuato/IndustriaTextilydeCalzado/')	
def A314():	
    return jsonify(resultadoCartera('Guanajuato','IndustriaTextilydeCalzado'))
@app.route('/Guanajuato/OrganismosInternacionales/')	
def A315():	
    return jsonify(resultadoCartera('Guanajuato','OrganismosInternacionales'))
@app.route('/Guanajuato/PetroleoMineriaGasyEnergia/')	

def A316():	
    return jsonify(resultadoCartera('Guanajuato','PetroleoMineriaGasyEnergia'))
@app.route('/Guanajuato/RestoIndustria/')	
def A317():	
    return jsonify(resultadoCartera('Guanajuato','RestoIndustria'))
@app.route('/Guanajuato/Salud/')	
def A318():	
    return jsonify(resultadoCartera('Guanajuato','Salud'))
@app.route('/Guanajuato/ServiciosComunalesySociales/')	
def A319():	
    return jsonify(resultadoCartera('Guanajuato','ServiciosComunalesySociales'))
@app.route('/Guanajuato/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A320():	
    return jsonify(resultadoCartera('Guanajuato','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Guanajuato/ServiciosFinancieros(NoBancarios)/')	
def A321():	
    return jsonify(resultadoCartera('Guanajuato','ServiciosFinancieros(NoBancarios)'))
@app.route('/Guanajuato/ServiciosProfesionalesyTecnicos/')	
def A322():	
    return jsonify(resultadoCartera('Guanajuato','ServiciosProfesionalesyTecnicos'))
@app.route('/Guanajuato/Transporte/')	
def A323():	
    return jsonify(resultadoCartera('Guanajuato','Transporte'))
@app.route('/Guanajuato/Bancario/')	
def A324():	
    return jsonify(resultadoCartera('Guanajuato','Bancario'))
@app.route('/Guerrero/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A325():	
    return jsonify(resultadoCartera('Guerrero','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Guerrero/ServiciosFinancieros(NoBancarios)/')	
def A326():	
    return jsonify(resultadoCartera('Guerrero','ServiciosFinancieros(NoBancarios)'))
@app.route('/Guerrero/ServiciosProfesionalesyTecnicos/')	

def A327():	
    return jsonify(resultadoCartera('Guerrero','ServiciosProfesionalesyTecnicos'))
@app.route('/Guerrero/Transporte/')	
def A328():	
    return jsonify(resultadoCartera('Guerrero','Transporte'))
@app.route('/Guerrero/Bancario/')	
def A329():	
    return jsonify(resultadoCartera('Guerrero','Bancario'))
@app.route('/Guerrero/AgriculturaSilviculturaGanaderiayPesca/')	
def A330():	
    return jsonify(resultadoCartera('Guerrero','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Guerrero/AlimentosBebidasyTabaco/')	
def A331():	
    return jsonify(resultadoCartera('Guerrero','AlimentosBebidasyTabaco'))
@app.route('/Guerrero/Comercio/')	
def A332():	
    return jsonify(resultadoCartera('Guerrero','Comercio'))
@app.route('/Guerrero/ComunicacionesyTelecomunicaciones/')	
def A333():	
    return jsonify(resultadoCartera('Guerrero','ComunicacionesyTelecomunicaciones'))
@app.route('/Guerrero/Construccion/')	
def A334():	
    return jsonify(resultadoCartera('Guerrero','Construccion'))
@app.route('/Guerrero/Educativo/')	
def A335():	
    return jsonify(resultadoCartera('Guerrero','Educativo'))
@app.route('/Guerrero/GobiernoFederal/')	
def A336():	
    return jsonify(resultadoCartera('Guerrero','GobiernoFederal'))
@app.route('/Guerrero/HotelesyRestaurantes/')	
def A337():	
    return jsonify(resultadoCartera('Guerrero','HotelesyRestaurantes'))
@app.route('/Guerrero/IndustriaAutomotriz/')	
def A338():	
    return jsonify(resultadoCartera('Guerrero','IndustriaAutomotriz'))
@app.route('/Guerrero/IndustriaMaterialesdeConstruccion/')	
def A339():	
    
    return jsonify(resultadoCartera('Guerrero','IndustriaMaterialesdeConstruccion'))
@app.route('/Guerrero/IndustriaQuimicayFarmaceutica/')	
def A340():	
    return jsonify(resultadoCartera('Guerrero','IndustriaQuimicayFarmaceutica'))
@app.route('/Guerrero/IndustriaTextilydeCalzado/')	

def A341():	
    
    return jsonify(resultadoCartera('Guerrero','IndustriaTextilydeCalzado'))
@app.route('/Guerrero/OrganismosInternacionales/')	
def A342():	
    return jsonify(resultadoCartera('Guerrero','OrganismosInternacionales'))
@app.route('/Guerrero/PetroleoMineriaGasyEnergia/')	
def A343():	
    return jsonify(resultadoCartera('Guerrero','PetroleoMineriaGasyEnergia'))
@app.route('/Guerrero/RestoIndustria/')	
def A344():	
    return jsonify(resultadoCartera('Guerrero','RestoIndustria'))
@app.route('/Guerrero/Salud/')	
def A345():	
    return jsonify(resultadoCartera('Guerrero','Salud'))
@app.route('/Guerrero/ServiciosComunalesySociales/')	

def A346():	
    return jsonify(resultadoCartera('Guerrero','ServiciosComunalesySociales'))
@app.route('/Guerrero/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A347():	
    return jsonify(resultadoCartera('Guerrero','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Guerrero/ServiciosFinancieros(NoBancarios)/')	
def A348():	
    return jsonify(resultadoCartera('Guerrero','ServiciosFinancieros(NoBancarios)'))
@app.route('/Guerrero/ServiciosProfesionalesyTecnicos/')	
def A349():	
    return jsonify(resultadoCartera('Guerrero','ServiciosProfesionalesyTecnicos'))
@app.route('/Guerrero/Transporte/')	
def A350():	
    return jsonify(resultadoCartera('Guerrero','Transporte'))
@app.route('/Guerrero/Bancario/')	
def A351():	
    return jsonify(resultadoCartera('Guerrero','Bancario'))
@app.route('/Hidalgo/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A352():	
    return jsonify(resultadoCartera('Hidalgo','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Hidalgo/ServiciosFinancieros(NoBancarios)/')	
def A353():	
    return jsonify(resultadoCartera('Hidalgo','ServiciosFinancieros(NoBancarios)'))
@app.route('/Hidalgo/ServiciosProfesionalesyTecnicos/')	
def A354():	
    return jsonify(resultadoCartera('Hidalgo','ServiciosProfesionalesyTecnicos'))
@app.route('/Hidalgo/Transporte/')	
def A355():	
    return jsonify(resultadoCartera('Hidalgo','Transporte'))
@app.route('/Hidalgo/Bancario/')	
def A356():	
    return jsonify(resultadoCartera('Hidalgo','Bancario'))
@app.route('/Hidalgo/AgriculturaSilviculturaGanaderiayPesca/')	
def A357():	
    return jsonify(resultadoCartera('Hidalgo','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Hidalgo/AlimentosBebidasyTabaco/')	
def A358():	
    return jsonify(resultadoCartera('Hidalgo','AlimentosBebidasyTabaco'))
@app.route('/Hidalgo/Comercio/')	
def A359():	
    return jsonify(resultadoCartera('Hidalgo','Comercio'))
@app.route('/Hidalgo/ComunicacionesyTelecomunicaciones/')	
def A360():	
    return jsonify(resultadoCartera('Hidalgo','ComunicacionesyTelecomunicaciones'))
@app.route('/Hidalgo/Construccion/')	
def A361():	
    return jsonify(resultadoCartera('Hidalgo','Construccion'))
@app.route('/Hidalgo/Educativo/')	
def A362():	
    return jsonify(resultadoCartera('Hidalgo','Educativo'))
@app.route('/Hidalgo/GobiernoFederal/')	
def A363():	
    return jsonify(resultadoCartera('Hidalgo','GobiernoFederal'))
@app.route('/Hidalgo/HotelesyRestaurantes/')	
def A364():	
    return jsonify(resultadoCartera('Hidalgo','HotelesyRestaurantes'))
@app.route('/Hidalgo/IndustriaAutomotriz/')	
def A365():	
    return jsonify(resultadoCartera('Hidalgo','IndustriaAutomotriz'))
@app.route('/Hidalgo/IndustriaMaterialesdeConstruccion/')	

def A366():	
    return jsonify(resultadoCartera('Hidalgo','IndustriaMaterialesdeConstruccion'))
@app.route('/Hidalgo/IndustriaQuimicayFarmaceutica/')	
def A367():	
    
    return jsonify(resultadoCartera('Hidalgo','IndustriaQuimicayFarmaceutica'))
@app.route('/Hidalgo/IndustriaTextilydeCalzado/')	
def A368():	
    return jsonify(resultadoCartera('Hidalgo','IndustriaTextilydeCalzado'))
@app.route('/Hidalgo/OrganismosInternacionales/')	
def A369():	
    return jsonify(resultadoCartera('Hidalgo','OrganismosInternacionales'))
@app.route('/Hidalgo/PetroleoMineriaGasyEnergia/')	
def A370():	
    return jsonify(resultadoCartera('Hidalgo','PetroleoMineriaGasyEnergia'))
@app.route('/Hidalgo/RestoIndustria/')	
def A371():	
    
    return jsonify(resultadoCartera('Hidalgo','RestoIndustria'))
@app.route('/Hidalgo/Salud/')	
def A372():	
    return jsonify(resultadoCartera('Hidalgo','Salud'))
@app.route('/Hidalgo/ServiciosComunalesySociales/')	
def A373():	
    return jsonify(resultadoCartera('Hidalgo','ServiciosComunalesySociales'))
@app.route('/Hidalgo/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A374():	
    return jsonify(resultadoCartera('Hidalgo','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Hidalgo/ServiciosFinancieros(NoBancarios)/')	
def A375():	
    return jsonify(resultadoCartera('Hidalgo','ServiciosFinancieros(NoBancarios)'))
@app.route('/Hidalgo/ServiciosProfesionalesyTecnicos/')	

def A376():	
    return jsonify(resultadoCartera('Hidalgo','ServiciosProfesionalesyTecnicos'))
@app.route('/Hidalgo/Transporte/')	
def A377():	
    return jsonify(resultadoCartera('Hidalgo','Transporte'))
@app.route('/Hidalgo/Bancario/')	
def A378():	
    return jsonify(resultadoCartera('Hidalgo','Bancario'))
@app.route('/Jalisco/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A379():	
    return jsonify(resultadoCartera('Jalisco','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Jalisco/ServiciosFinancieros(NoBancarios)/')	
def A380():	
    
    return jsonify(resultadoCartera('Jalisco','ServiciosFinancieros(NoBancarios)'))
@app.route('/Jalisco/ServiciosProfesionalesyTecnicos/')	
def A381():	
    return jsonify(resultadoCartera('Jalisco','ServiciosProfesionalesyTecnicos'))
@app.route('/Jalisco/Transporte/')	
def A382():	
    return jsonify(resultadoCartera('Jalisco','Transporte'))
@app.route('/Jalisco/Bancario/')	
def A383():	
    return jsonify(resultadoCartera('Jalisco','Bancario'))
@app.route('/Jalisco/AgriculturaSilviculturaGanaderiayPesca/')	
def A384():	
    return jsonify(resultadoCartera('Jalisco','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Jalisco/AlimentosBebidasyTabaco/')	
def A385():	
    return jsonify(resultadoCartera('Jalisco','AlimentosBebidasyTabaco'))
@app.route('/Jalisco/Comercio/')	
def A386():	
    return jsonify(resultadoCartera('Jalisco','Comercio'))
@app.route('/Jalisco/ComunicacionesyTelecomunicaciones/')	
def A387():	
    return jsonify(resultadoCartera('Jalisco','ComunicacionesyTelecomunicaciones'))
@app.route('/Jalisco/Construccion/')	
def A388():	
    return jsonify(resultadoCartera('Jalisco','Construccion'))
@app.route('/Jalisco/Educativo/')	
def A389():	
    return jsonify(resultadoCartera('Jalisco','Educativo'))
@app.route('/Jalisco/GobiernoFederal/')	
def A390():	
    return jsonify(resultadoCartera('Jalisco','GobiernoFederal'))
@app.route('/Jalisco/HotelesyRestaurantes/')	
def A391():	
    
    return jsonify(resultadoCartera('Jalisco','HotelesyRestaurantes'))
@app.route('/Jalisco/IndustriaAutomotriz/')	
def A392():	
    return jsonify(resultadoCartera('Jalisco','IndustriaAutomotriz'))
@app.route('/Jalisco/IndustriaMaterialesdeConstruccion/')	
def A393():	
    return jsonify(resultadoCartera('Jalisco','IndustriaMaterialesdeConstruccion'))
@app.route('/Jalisco/IndustriaQuimicayFarmaceutica/')	
def A394():	
    return jsonify(resultadoCartera('Jalisco','IndustriaQuimicayFarmaceutica'))
@app.route('/Jalisco/IndustriaTextilydeCalzado/')	
def A395():	
    return jsonify(resultadoCartera('Jalisco','IndustriaTextilydeCalzado'))
@app.route('/Jalisco/OrganismosInternacionales/')	
def A396():	
    return jsonify(resultadoCartera('Jalisco','OrganismosInternacionales'))
@app.route('/Jalisco/PetroleoMineriaGasyEnergia/')	
def A397():	
    return jsonify(resultadoCartera('Jalisco','PetroleoMineriaGasyEnergia'))
@app.route('/Jalisco/RestoIndustria/')	
def A398():	
    
    return jsonify(resultadoCartera('Jalisco','RestoIndustria'))
@app.route('/Jalisco/Salud/')	
def A399():	
    return jsonify(resultadoCartera('Jalisco','Salud'))
@app.route('/Jalisco/ServiciosComunalesySociales/')	
def A400():	
    
    return jsonify(resultadoCartera('Jalisco','ServiciosComunalesySociales'))
@app.route('/Jalisco/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A401():	
    return jsonify(resultadoCartera('Jalisco','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Jalisco/ServiciosFinancieros(NoBancarios)/')	
def A402():	
    return jsonify(resultadoCartera('Jalisco','ServiciosFinancieros(NoBancarios)'))
@app.route('/Jalisco/ServiciosProfesionalesyTecnicos/')	
def A403():	
    return jsonify(resultadoCartera('Jalisco','ServiciosProfesionalesyTecnicos'))
@app.route('/Jalisco/Transporte/')	
def A404():	
    return jsonify(resultadoCartera('Jalisco','Transporte'))
@app.route('/Jalisco/Bancario/')	
def A405():	
    return jsonify(resultadoCartera('Jalisco','Bancario'))
@app.route('/MIchoacan/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')
def A406():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/MIchoacan/ServiciosFinancieros(NoBancarios)/')	
def A407():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosFinancieros(NoBancarios)'))
@app.route('/MIchoacan/ServiciosProfesionalesyTecnicos/')	
def A408():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosProfesionalesyTecnicos'))
@app.route('/MIchoacan/Transporte/')	
def A409():	
    return jsonify(resultadoCartera('MIchoacan','Transporte'))
@app.route('/MIchoacan/Bancario/')	
def A410():	
    return jsonify(resultadoCartera('MIchoacan','Bancario'))
@app.route('/MIchoacan/AgriculturaSilviculturaGanaderiayPesca/')	
def A411():	
    
    return jsonify(resultadoCartera('MIchoacan','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/MIchoacan/AlimentosBebidasyTabaco/')	
def A412():	
    return jsonify(resultadoCartera('MIchoacan','AlimentosBebidasyTabaco'))
@app.route('/MIchoacan/Comercio/')	
def A413():	
    return jsonify(resultadoCartera('MIchoacan','Comercio'))
@app.route('/MIchoacan/ComunicacionesyTelecomunicaciones/')	
def A414():	
    return jsonify(resultadoCartera('MIchoacan','ComunicacionesyTelecomunicaciones'))
@app.route('/MIchoacan/Construccion/')	
def A415():	
    return jsonify(resultadoCartera('MIchoacan','Construccion'))
@app.route('/MIchoacan/Educativo/')	
def A416():	
    return jsonify(resultadoCartera('MIchoacan','Educativo'))
@app.route('/MIchoacan/GobiernoFederal/')	
def A417():	
    return jsonify(resultadoCartera('MIchoacan','GobiernoFederal'))
@app.route('/MIchoacan/HotelesyRestaurantes/')	
def A418():	
    
    
    return jsonify(resultadoCartera('MIchoacan','HotelesyRestaurantes'))
@app.route('/MIchoacan/IndustriaAutomotriz/')	
def A419():	
    return jsonify(resultadoCartera('MIchoacan','IndustriaAutomotriz'))
@app.route('/MIchoacan/IndustriaMaterialesdeConstruccion/')	
def A420():	
    return jsonify(resultadoCartera('MIchoacan','IndustriaMaterialesdeConstruccion'))
@app.route('/MIchoacan/IndustriaQuimicayFarmaceutica/')	
def A421():	
    return jsonify(resultadoCartera('MIchoacan','IndustriaQuimicayFarmaceutica'))
@app.route('/MIchoacan/IndustriaTextilydeCalzado/')	
def A422():	
    return jsonify(resultadoCartera('MIchoacan','IndustriaTextilydeCalzado'))
@app.route('/MIchoacan/OrganismosInternacionales/')	
def A423():	
    return jsonify(resultadoCartera('MIchoacan','OrganismosInternacionales'))
@app.route('/MIchoacan/PetroleoMineriaGasyEnergia/')	
def A424():	
    return jsonify(resultadoCartera('MIchoacan','PetroleoMineriaGasyEnergia'))
@app.route('/MIchoacan/RestoIndustria/')	
def A425():	
    return jsonify(resultadoCartera('MIchoacan','RestoIndustria'))
@app.route('/MIchoacan/Salud/')	
def A426():	
    return jsonify(resultadoCartera('MIchoacan','Salud'))
@app.route('/MIchoacan/ServiciosComunalesySociales/')	
def A427():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosComunalesySociales'))
@app.route('/MIchoacan/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A428():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/MIchoacan/ServiciosFinancieros(NoBancarios)/')	
def A429():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosFinancieros(NoBancarios)'))
@app.route('/MIchoacan/ServiciosProfesionalesyTecnicos/')	
def A430():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosProfesionalesyTecnicos'))
@app.route('/MIchoacan/Transporte/')	
def A431():	
    return jsonify(resultadoCartera('MIchoacan','Transporte'))
@app.route('/MIchoacan/Bancario/')	
def A432():	
    return jsonify(resultadoCartera('MIchoacan','Bancario'))
@app.route('/MIchoacan/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A433():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/MIchoacan/ServiciosFinancieros(NoBancarios)/')	
def A434():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosFinancieros(NoBancarios)'))
@app.route('/MIchoacan/ServiciosProfesionalesyTecnicos/')	
def A435():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosProfesionalesyTecnicos'))
@app.route('/MIchoacan/Transporte/')	
def A436():	
    
    return jsonify(resultadoCartera('MIchoacan','Transporte'))
@app.route('/MIchoacan/Bancario/')	
def A437():	
    return jsonify(resultadoCartera('MIchoacan','Bancario'))
@app.route('/MIchoacan/AgriculturaSilviculturaGanaderiayPesca/')	
def A438():	
    
    return jsonify(resultadoCartera('MIchoacan','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/MIchoacan/AlimentosBebidasyTabaco/')	
def A439():	
    return jsonify(resultadoCartera('MIchoacan','AlimentosBebidasyTabaco'))
@app.route('/MIchoacan/Comercio/')	

def A440():	
    return jsonify(resultadoCartera('MIchoacan','Comercio'))
@app.route('/MIchoacan/ComunicacionesyTelecomunicaciones/')	
def A441():	
    return jsonify(resultadoCartera('MIchoacan','ComunicacionesyTelecomunicaciones'))
@app.route('/MIchoacan/Construccion/')	
def A442():	
    return jsonify(resultadoCartera('MIchoacan','Construccion'))
@app.route('/MIchoacan/Educativo/')	
def A443():	
    return jsonify(resultadoCartera('MIchoacan','Educativo'))
@app.route('/MIchoacan/GobiernoFederal/')	
def A444():	
    return jsonify(resultadoCartera('MIchoacan','GobiernoFederal'))
@app.route('/MIchoacan/HotelesyRestaurantes/')	
def A445():	
    return jsonify(resultadoCartera('MIchoacan','HotelesyRestaurantes'))
@app.route('/MIchoacan/IndustriaAutomotriz/')	
def A446():	
    return jsonify(resultadoCartera('MIchoacan','IndustriaAutomotriz'))
@app.route('/MIchoacan/IndustriaMaterialesdeConstruccion/')	
def A447():	
    return jsonify(resultadoCartera('MIchoacan','IndustriaMaterialesdeConstruccion'))
@app.route('/MIchoacan/IndustriaQuimicayFarmaceutica/')	
def A448():	
    return jsonify(resultadoCartera('MIchoacan','IndustriaQuimicayFarmaceutica'))
@app.route('/MIchoacan/IndustriaTextilydeCalzado/')	
def A449():	
    return jsonify(resultadoCartera('MIchoacan','IndustriaTextilydeCalzado'))
@app.route('/MIchoacan/OrganismosInternacionales/')	
def A450():	
    return jsonify(resultadoCartera('MIchoacan','OrganismosInternacionales'))
@app.route('/MIchoacan/PetroleoMineriaGasyEnergia/')	
def A451():	
    return jsonify(resultadoCartera('MIchoacan','PetroleoMineriaGasyEnergia'))
@app.route('/MIchoacan/RestoIndustria/')	
def A452():	
    return jsonify(resultadoCartera('MIchoacan','RestoIndustria'))
@app.route('/MIchoacan/Salud/')	
def A453():	
    return jsonify(resultadoCartera('MIchoacan','Salud'))
@app.route('/MIchoacan/ServiciosComunalesySociales/')	
def A454():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosComunalesySociales'))
@app.route('/MIchoacan/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A455():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/MIchoacan/ServiciosFinancieros(NoBancarios)/')	
def A456():	
    
    return jsonify(resultadoCartera('MIchoacan','ServiciosFinancieros(NoBancarios)'))
@app.route('/MIchoacan/ServiciosProfesionalesyTecnicos/')	
def A457():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosProfesionalesyTecnicos'))
@app.route('/MIchoacan/Transporte/')	
def A458():	
    return jsonify(resultadoCartera('MIchoacan','Transporte'))
@app.route('/MIchoacan/Bancario/')	
def A459():	
    return jsonify(resultadoCartera('MIchoacan','Bancario'))
@app.route('/MIchoacan/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A460():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/MIchoacan/ServiciosFinancieros(NoBancarios)/')	
def A461():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosFinancieros(NoBancarios)'))
@app.route('/MIchoacan/ServiciosProfesionalesyTecnicos/')	
def A462():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosProfesionalesyTecnicos'))
@app.route('/MIchoacan/Transporte/')	
def A463():	
    return jsonify(resultadoCartera('MIchoacan','Transporte'))
@app.route('/MIchoacan/Bancario/')	
def A464():	
    return jsonify(resultadoCartera('MIchoacan','Bancario'))
@app.route('/MIchoacan/AgriculturaSilviculturaGanaderiayPesca/')	
def A465():	
    return jsonify(resultadoCartera('MIchoacan','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/MIchoacan/AlimentosBebidasyTabaco/')	

def A466():	
    return jsonify(resultadoCartera('MIchoacan','AlimentosBebidasyTabaco'))
@app.route('/MIchoacan/Comercio/')	
def A467():	
    return jsonify(resultadoCartera('MIchoacan','Comercio'))
@app.route('/MIchoacan/ComunicacionesyTelecomunicaciones/')	
def A468():	
    return jsonify(resultadoCartera('MIchoacan','ComunicacionesyTelecomunicaciones'))
@app.route('/MIchoacan/Construccion/')	
def A469():	
    return jsonify(resultadoCartera('MIchoacan','Construccion'))
@app.route('/MIchoacan/Educativo/')	
def A470():	
    return jsonify(resultadoCartera('MIchoacan','Educativo'))
@app.route('/MIchoacan/GobiernoFederal/')	
def A471():	
    return jsonify(resultadoCartera('MIchoacan','GobiernoFederal'))
@app.route('/MIchoacan/HotelesyRestaurantes/')	
def A472():	
    return jsonify(resultadoCartera('MIchoacan','HotelesyRestaurantes'))
@app.route('/MIchoacan/IndustriaAutomotriz/')	
def A473():	
    return jsonify(resultadoCartera('MIchoacan','IndustriaAutomotriz'))
@app.route('/MIchoacan/IndustriaMaterialesdeConstruccion/')	
def A474():	
    return jsonify(resultadoCartera('MIchoacan','IndustriaMaterialesdeConstruccion'))
@app.route('/MIchoacan/IndustriaQuimicayFarmaceutica/')	

def A475():	
    return jsonify(resultadoCartera('MIchoacan','IndustriaQuimicayFarmaceutica'))
@app.route('/MIchoacan/IndustriaTextilydeCalzado/')	
def A476():	
    return jsonify(resultadoCartera('MIchoacan','IndustriaTextilydeCalzado'))
@app.route('/MIchoacan/OrganismosInternacionales/')	
def A477():	
    return jsonify(resultadoCartera('MIchoacan','OrganismosInternacionales'))
@app.route('/MIchoacan/PetroleoMineriaGasyEnergia/')	
def A478():	
    return jsonify(resultadoCartera('MIchoacan','PetroleoMineriaGasyEnergia'))
@app.route('/MIchoacan/RestoIndustria/')	
def A479():	
    return jsonify(resultadoCartera('MIchoacan','RestoIndustria'))
@app.route('/MIchoacan/Salud/')	
def A480():	
    return jsonify(resultadoCartera('MIchoacan','Salud'))
@app.route('/MIchoacan/ServiciosComunalesySociales/')	
def A481():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosComunalesySociales'))
@app.route('/MIchoacan/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A482():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/MIchoacan/ServiciosFinancieros(NoBancarios)/')	
def A483():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosFinancieros(NoBancarios)'))
@app.route('/MIchoacan/ServiciosProfesionalesyTecnicos/')	
def A484():	
    return jsonify(resultadoCartera('MIchoacan','ServiciosProfesionalesyTecnicos'))
@app.route('/MIchoacan/Transporte/')	
def A485():	
    return jsonify(resultadoCartera('MIchoacan','Transporte'))
@app.route('/MIchoacan/Bancario/')	
def A486():	
    return jsonify(resultadoCartera('MIchoacan','Bancario'))
@app.route('/NuevoLeon/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A487():	
    return jsonify(resultadoCartera('NuevoLeon','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/NuevoLeon/ServiciosFinancieros(NoBancarios)/')	
def A488():	
    return jsonify(resultadoCartera('NuevoLeon','ServiciosFinancieros(NoBancarios)'))
@app.route('/NuevoLeon/ServiciosProfesionalesyTecnicos/')	
def A489():	
    return jsonify(resultadoCartera('NuevoLeon','ServiciosProfesionalesyTecnicos'))
@app.route('/NuevoLeon/Transporte/')	
def A490():	
    return jsonify(resultadoCartera('NuevoLeon','Transporte'))
@app.route('/NuevoLeon/Bancario/')	
def A491():	
    return jsonify(resultadoCartera('NuevoLeon','Bancario'))
@app.route('/NuevoLeon/AgriculturaSilviculturaGanaderiayPesca/')	
def A492():	
    return jsonify(resultadoCartera('NuevoLeon','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/NuevoLeon/AlimentosBebidasyTabaco/')	
def A493():	
    return jsonify(resultadoCartera('NuevoLeon','AlimentosBebidasyTabaco'))
@app.route('/NuevoLeon/Comercio/')	
def A494():	
    return jsonify(resultadoCartera('NuevoLeon','Comercio'))
@app.route('/NuevoLeon/ComunicacionesyTelecomunicaciones/')	
def A495():	
    return jsonify(resultadoCartera('NuevoLeon','ComunicacionesyTelecomunicaciones'))
@app.route('/NuevoLeon/Construccion/')	
def A496():	
    return jsonify(resultadoCartera('NuevoLeon','Construccion'))
@app.route('/NuevoLeon/Educativo/')	
def A497():	
    return jsonify(resultadoCartera('NuevoLeon','Educativo'))
@app.route('/NuevoLeon/GobiernoFederal/')	
def A498():	
    return jsonify(resultadoCartera('NuevoLeon','GobiernoFederal'))
@app.route('/NuevoLeon/HotelesyRestaurantes/')	
def A499():	
    return jsonify(resultadoCartera('NuevoLeon','HotelesyRestaurantes'))
@app.route('/NuevoLeon/IndustriaAutomotriz/')	
def A500():	
    return jsonify(resultadoCartera('NuevoLeon','IndustriaAutomotriz'))
@app.route('/NuevoLeon/IndustriaMaterialesdeConstruccion/')	
def A501():	
    return jsonify(resultadoCartera('NuevoLeon','IndustriaMaterialesdeConstruccion'))
@app.route('/NuevoLeon/IndustriaQuimicayFarmaceutica/')	
def A502():	
    return jsonify(resultadoCartera('NuevoLeon','IndustriaQuimicayFarmaceutica'))
@app.route('/NuevoLeon/IndustriaTextilydeCalzado/')	
def A503():	
    return jsonify(resultadoCartera('NuevoLeon','IndustriaTextilydeCalzado'))
@app.route('/NuevoLeon/OrganismosInternacionales/')	
def A504():	
    return jsonify(resultadoCartera('NuevoLeon','OrganismosInternacionales'))
@app.route('/NuevoLeon/PetroleoMineriaGasyEnergia/')	
def A505():	
    return jsonify(resultadoCartera('NuevoLeon','PetroleoMineriaGasyEnergia'))
@app.route('/NuevoLeon/RestoIndustria/')	

def A506():	
    return jsonify(resultadoCartera('NuevoLeon','RestoIndustria'))
@app.route('/NuevoLeon/Salud/')	
def A507():	
    return jsonify(resultadoCartera('NuevoLeon','Salud'))
@app.route('/NuevoLeon/ServiciosComunalesySociales/')	
def A508():	
    return jsonify(resultadoCartera('NuevoLeon','ServiciosComunalesySociales'))
@app.route('/NuevoLeon/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A509():	
    return jsonify(resultadoCartera('NuevoLeon','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/NuevoLeon/ServiciosFinancieros(NoBancarios)/')	
def A510():	
    return jsonify(resultadoCartera('NuevoLeon','ServiciosFinancieros(NoBancarios)'))
@app.route('/NuevoLeon/ServiciosProfesionalesyTecnicos/')	
def A511():	
    return jsonify(resultadoCartera('NuevoLeon','ServiciosProfesionalesyTecnicos'))
@app.route('/NuevoLeon/Transporte/')	

def A512():	
    return jsonify(resultadoCartera('NuevoLeon','Transporte'))
@app.route('/NuevoLeon/Bancario/')	
def A513():	
    return jsonify(resultadoCartera('NuevoLeon','Bancario'))
@app.route('/Oaxaca/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	

def A514():	
    return jsonify(resultadoCartera('Oaxaca','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Oaxaca/ServiciosFinancieros(NoBancarios)/')	
def A515():	
    return jsonify(resultadoCartera('Oaxaca','ServiciosFinancieros(NoBancarios)'))
@app.route('/Oaxaca/ServiciosProfesionalesyTecnicos/')	
def A516():	
    return jsonify(resultadoCartera('Oaxaca','ServiciosProfesionalesyTecnicos'))
@app.route('/Oaxaca/Transporte/')	
def A517():	
    return jsonify(resultadoCartera('Oaxaca','Transporte'))
@app.route('/Oaxaca/Bancario/')	
def A518():	
    return jsonify(resultadoCartera('Oaxaca','Bancario'))
@app.route('/Oaxaca/AgriculturaSilviculturaGanaderiayPesca/')	
def A519():	
    return jsonify(resultadoCartera('Oaxaca','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Oaxaca/AlimentosBebidasyTabaco/')	
def A520():	
    return jsonify(resultadoCartera('Oaxaca','AlimentosBebidasyTabaco'))
@app.route('/Oaxaca/Comercio/')	
def A521():	
    return jsonify(resultadoCartera('Oaxaca','Comercio'))
@app.route('/Oaxaca/ComunicacionesyTelecomunicaciones/')	
def A522():	
    return jsonify(resultadoCartera('Oaxaca','ComunicacionesyTelecomunicaciones'))
@app.route('/Oaxaca/Construccion/')	
def A523():	
    return jsonify(resultadoCartera('Oaxaca','Construccion'))
@app.route('/Oaxaca/Educativo/')	
def A524():	
    return jsonify(resultadoCartera('Oaxaca','Educativo'))
@app.route('/Oaxaca/GobiernoFederal/')	
def A525():	
    return jsonify(resultadoCartera('Oaxaca','GobiernoFederal'))
@app.route('/Oaxaca/HotelesyRestaurantes/')	
def A526():	
    return jsonify(resultadoCartera('Oaxaca','HotelesyRestaurantes'))
@app.route('/Oaxaca/IndustriaAutomotriz/')	
def A527():	
    return jsonify(resultadoCartera('Oaxaca','IndustriaAutomotriz'))
@app.route('/Oaxaca/IndustriaMaterialesdeConstruccion/')	
def A528():	
    return jsonify(resultadoCartera('Oaxaca','IndustriaMaterialesdeConstruccion'))
@app.route('/Oaxaca/IndustriaQuimicayFarmaceutica/')	
def A529():	
    return jsonify(resultadoCartera('Oaxaca','IndustriaQuimicayFarmaceutica'))
@app.route('/Oaxaca/IndustriaTextilydeCalzado/')	
def A530():	
    return jsonify(resultadoCartera('Oaxaca','IndustriaTextilydeCalzado'))
@app.route('/Oaxaca/OrganismosInternacionales/')	
def A531():	
    return jsonify(resultadoCartera('Oaxaca','OrganismosInternacionales'))
@app.route('/Oaxaca/PetroleoMineriaGasyEnergia/')	
def A532():	
    return jsonify(resultadoCartera('Oaxaca','PetroleoMineriaGasyEnergia'))
@app.route('/Oaxaca/RestoIndustria/')	
def A533():	
    return jsonify(resultadoCartera('Oaxaca','RestoIndustria'))
@app.route('/Oaxaca/Salud/')	
def A534():	
    return jsonify(resultadoCartera('Oaxaca','Salud'))
@app.route('/Oaxaca/ServiciosComunalesySociales/')	
def A535():	
    return jsonify(resultadoCartera('Oaxaca','ServiciosComunalesySociales'))
@app.route('/Oaxaca/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A536():	
    return jsonify(resultadoCartera('Oaxaca','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Oaxaca/ServiciosFinancieros(NoBancarios)/')	
def A537():	
    return jsonify(resultadoCartera('Oaxaca','ServiciosFinancieros(NoBancarios)'))
@app.route('/Oaxaca/ServiciosProfesionalesyTecnicos/')	
def A538():	
    return jsonify(resultadoCartera('Oaxaca','ServiciosProfesionalesyTecnicos'))
@app.route('/Oaxaca/Transporte/')	
def A539():	
    return jsonify(resultadoCartera('Oaxaca','Transporte'))
@app.route('/Oaxaca/Bancario/')
def A540():	
    return jsonify(resultadoCartera('Oaxaca','Bancario'))
@app.route('/Puebla/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A541():	
    return jsonify(resultadoCartera('Puebla','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Puebla/ServiciosFinancieros(NoBancarios)/')	
def A542():	
    return jsonify(resultadoCartera('Puebla','ServiciosFinancieros(NoBancarios)'))
@app.route('/Puebla/ServiciosProfesionalesyTecnicos/')	
def A543():	
    return jsonify(resultadoCartera('Puebla','ServiciosProfesionalesyTecnicos'))
@app.route('/Puebla/Transporte/')	
def A544():	
    return jsonify(resultadoCartera('Puebla','Transporte'))
@app.route('/Puebla/Bancario/')	
def A545():	
    return jsonify(resultadoCartera('Puebla','Bancario'))
@app.route('/Puebla/AgriculturaSilviculturaGanaderiayPesca/')	
def A546():	
    return jsonify(resultadoCartera('Puebla','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Puebla/AlimentosBebidasyTabaco/')	
def A547():	
    return jsonify(resultadoCartera('Puebla','AlimentosBebidasyTabaco'))
@app.route('/Puebla/Comercio/')	
def A548():	
    return jsonify(resultadoCartera('Puebla','Comercio'))
@app.route('/Puebla/ComunicacionesyTelecomunicaciones/')	
def A549():	
    return jsonify(resultadoCartera('Puebla','ComunicacionesyTelecomunicaciones'))
@app.route('/Puebla/Construccion/')	
def A550():	
    return jsonify(resultadoCartera('Puebla','Construccion'))
@app.route('/Puebla/Educativo/')	
def A551():	
    return jsonify(resultadoCartera('Puebla','Educativo'))
@app.route('/Puebla/GobiernoFederal/')	
def A552():	
    
    return jsonify(resultadoCartera('Puebla','GobiernoFederal'))
@app.route('/Puebla/HotelesyRestaurantes/')	
def A553():	
    return jsonify(resultadoCartera('Puebla','HotelesyRestaurantes'))
@app.route('/Puebla/IndustriaAutomotriz/')	
def A554():	
    return jsonify(resultadoCartera('Puebla','IndustriaAutomotriz'))
@app.route('/Puebla/IndustriaMaterialesdeConstruccion/')	
def A555():	
    return jsonify(resultadoCartera('Puebla','IndustriaMaterialesdeConstruccion'))
@app.route('/Puebla/IndustriaQuimicayFarmaceutica/')	
def A556():	
    return jsonify(resultadoCartera('Puebla','IndustriaQuimicayFarmaceutica'))
@app.route('/Puebla/IndustriaTextilydeCalzado/')	
def A557():	
    return jsonify(resultadoCartera('Puebla','IndustriaTextilydeCalzado'))
@app.route('/Puebla/OrganismosInternacionales/')	
def A558():	
    return jsonify(resultadoCartera('Puebla','OrganismosInternacionales'))
@app.route('/Puebla/PetroleoMineriaGasyEnergia/')	
def A559():	
    return jsonify(resultadoCartera('Puebla','PetroleoMineriaGasyEnergia'))
@app.route('/Puebla/RestoIndustria/')	
def A560():	
    return jsonify(resultadoCartera('Puebla','RestoIndustria'))
@app.route('/Puebla/Salud/')	
def A561():	
    return jsonify(resultadoCartera('Puebla','Salud'))
@app.route('/Puebla/ServiciosComunalesySociales/')	
def A562():	
    return jsonify(resultadoCartera('Puebla','ServiciosComunalesySociales'))
@app.route('/Puebla/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A563():	
    return jsonify(resultadoCartera('Puebla','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Puebla/ServiciosFinancieros(NoBancarios)/')	
def A564():	
    return jsonify(resultadoCartera('Puebla','ServiciosFinancieros(NoBancarios)'))
@app.route('/Puebla/ServiciosProfesionalesyTecnicos/')	
def A565():	
    return jsonify(resultadoCartera('Puebla','ServiciosProfesionalesyTecnicos'))
@app.route('/Puebla/Transporte/')	
def A566():	
    return jsonify(resultadoCartera('Puebla','Transporte'))
@app.route('/Puebla/Bancario/')	
def A567():	
    return jsonify(resultadoCartera('Puebla','Bancario'))
@app.route('/Puebla/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A568():	
    return jsonify(resultadoCartera('Puebla','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Puebla/ServiciosFinancieros(NoBancarios)/')	
def A569():	
    return jsonify(resultadoCartera('Puebla','ServiciosFinancieros(NoBancarios)'))
@app.route('/Puebla/ServiciosProfesionalesyTecnicos/')	
def A570():	
    return jsonify(resultadoCartera('Puebla','ServiciosProfesionalesyTecnicos'))
@app.route('/Puebla/Transporte/')	
def A571():	
    return jsonify(resultadoCartera('Puebla','Transporte'))
@app.route('/Puebla/Bancario/')	
def A572():	
    return jsonify(resultadoCartera('Puebla','Bancario'))
@app.route('/Queretaro/AgriculturaSilviculturaGanaderiayPesca/')	
def A573():	
    return jsonify(resultadoCartera('Queretaro','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Queretaro/AlimentosBebidasyTabaco/')	
def A574():	
    return jsonify(resultadoCartera('Queretaro','AlimentosBebidasyTabaco'))
@app.route('/Queretaro/Comercio/')	

def A575():	
    return jsonify(resultadoCartera('Queretaro','Comercio'))
@app.route('/Queretaro/ComunicacionesyTelecomunicaciones/')	
def A576():	
    return jsonify(resultadoCartera('Queretaro','ComunicacionesyTelecomunicaciones'))
@app.route('/Queretaro/Construccion/')	
def A577():	
    return jsonify(resultadoCartera('Queretaro','Construccion'))
@app.route('/Queretaro/Educativo/')	
def A578():	
    return jsonify(resultadoCartera('Queretaro','Educativo'))
@app.route('/Queretaro/GobiernoFederal/')	
def A579():	
    return jsonify(resultadoCartera('Queretaro','GobiernoFederal'))
@app.route('/Queretaro/HotelesyRestaurantes/')	
def A580():	
    return jsonify(resultadoCartera('Queretaro','HotelesyRestaurantes'))
@app.route('/Queretaro/IndustriaAutomotriz/')	
def A581():	
    return jsonify(resultadoCartera('Queretaro','IndustriaAutomotriz'))
@app.route('/Queretaro/IndustriaMaterialesdeConstruccion/')	
def A582():	
    return jsonify(resultadoCartera('Queretaro','IndustriaMaterialesdeConstruccion'))
@app.route('/Queretaro/IndustriaQuimicayFarmaceutica/')	
def A583():	
    return jsonify(resultadoCartera('Queretaro','IndustriaQuimicayFarmaceutica'))
@app.route('/Queretaro/IndustriaTextilydeCalzado/')	
def A584():	
    return jsonify(resultadoCartera('Queretaro','IndustriaTextilydeCalzado'))
@app.route('/Queretaro/OrganismosInternacionales/')	
def A585():	
    return jsonify(resultadoCartera('Queretaro','OrganismosInternacionales'))
@app.route('/Queretaro/PetroleoMineriaGasyEnergia/')	
def A586():	
    return jsonify(resultadoCartera('Queretaro','PetroleoMineriaGasyEnergia'))
@app.route('/Queretaro/RestoIndustria/')	
def A587():	
    return jsonify(resultadoCartera('Queretaro','RestoIndustria'))
@app.route('/Queretaro/Salud/')	
def A588():	
    return jsonify(resultadoCartera('Queretaro','Salud'))
@app.route('/Queretaro/ServiciosComunalesySociales/')	
def A589():	
    return jsonify(resultadoCartera('Queretaro','ServiciosComunalesySociales'))
@app.route('/Queretaro/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A590():	
    return jsonify(resultadoCartera('Queretaro','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Queretaro/ServiciosFinancieros(NoBancarios)/')	
def A591():	
    return jsonify(resultadoCartera('Queretaro','ServiciosFinancieros(NoBancarios)'))
@app.route('/Queretaro/ServiciosProfesionalesyTecnicos/')	
def A592():	
    return jsonify(resultadoCartera('Queretaro','ServiciosProfesionalesyTecnicos'))
@app.route('/Queretaro/Transporte/')	
def A593():	
    return jsonify(resultadoCartera('Queretaro','Transporte'))
@app.route('/Queretaro/Bancario/')	
def A594():	
    return jsonify(resultadoCartera('Queretaro','Bancario'))
@app.route('/QuintanaRoo/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A595():	
    return jsonify(resultadoCartera('QuintanaRoo','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/QuintanaRoo/ServiciosFinancieros(NoBancarios)/')	
def A596():	
    return jsonify(resultadoCartera('QuintanaRoo','ServiciosFinancieros(NoBancarios)'))
@app.route('/QuintanaRoo/ServiciosProfesionalesyTecnicos/')	
def A597():	
    return jsonify(resultadoCartera('QuintanaRoo','ServiciosProfesionalesyTecnicos'))
@app.route('/QuintanaRoo/Transporte/')	
def A598():	
    return jsonify(resultadoCartera('QuintanaRoo','Transporte'))
@app.route('/QuintanaRoo/Bancario/')	
def A599():	
    return jsonify(resultadoCartera('QuintanaRoo','Bancario'))
@app.route('/QuintanaRoo/AgriculturaSilviculturaGanaderiayPesca/')	
def A600():	
    return jsonify(resultadoCartera('QuintanaRoo','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/QuintanaRoo/AlimentosBebidasyTabaco/')	
def A601():	
    return jsonify(resultadoCartera('QuintanaRoo','AlimentosBebidasyTabaco'))
@app.route('/QuintanaRoo/Comercio/')	
def A602():	
    return jsonify(resultadoCartera('QuintanaRoo','Comercio'))
@app.route('/QuintanaRoo/ComunicacionesyTelecomunicaciones/')	
def A603():	
    return jsonify(resultadoCartera('QuintanaRoo','ComunicacionesyTelecomunicaciones'))
@app.route('/QuintanaRoo/Construccion/')	
def A604():	
    return jsonify(resultadoCartera('QuintanaRoo','Construccion'))
@app.route('/QuintanaRoo/Educativo/')	
def A605():	
    return jsonify(resultadoCartera('QuintanaRoo','Educativo'))
@app.route('/QuintanaRoo/GobiernoFederal/')	
def A606():	
    return jsonify(resultadoCartera('QuintanaRoo','GobiernoFederal'))
@app.route('/QuintanaRoo/HotelesyRestaurantes/')	
def A607():	
    return jsonify(resultadoCartera('QuintanaRoo','HotelesyRestaurantes'))
@app.route('/QuintanaRoo/IndustriaAutomotriz/')	
def A608():	
    return jsonify(resultadoCartera('QuintanaRoo','IndustriaAutomotriz'))
@app.route('/QuintanaRoo/IndustriaMaterialesdeConstruccion/')	
def A609():	
    return jsonify(resultadoCartera('QuintanaRoo','IndustriaMaterialesdeConstruccion'))
@app.route('/QuintanaRoo/IndustriaQuimicayFarmaceutica/')	
def A610():	
    return jsonify(resultadoCartera('QuintanaRoo','IndustriaQuimicayFarmaceutica'))
@app.route('/QuintanaRoo/IndustriaTextilydeCalzado/')	
def A611():	
    return jsonify(resultadoCartera('QuintanaRoo','IndustriaTextilydeCalzado'))
@app.route('/QuintanaRoo/OrganismosInternacionales/')	
def A612():	
    return jsonify(resultadoCartera('QuintanaRoo','OrganismosInternacionales'))
@app.route('/QuintanaRoo/PetroleoMineriaGasyEnergia/')	

def A613():	return jsonify(resultadoCartera('QuintanaRoo','PetroleoMineriaGasyEnergia'))
@app.route('/QuintanaRoo/RestoIndustria/')	
def A614():	
    
    return jsonify(resultadoCartera('QuintanaRoo','RestoIndustria'))
@app.route('/QuintanaRoo/Salud/')	
def A615():	
    return jsonify(resultadoCartera('QuintanaRoo','Salud'))
@app.route('/QuintanaRoo/ServiciosComunalesySociales/')	
def A616():	
    return jsonify(resultadoCartera('QuintanaRoo','ServiciosComunalesySociales'))
@app.route('/QuintanaRoo/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A617():	
    return jsonify(resultadoCartera('QuintanaRoo','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/QuintanaRoo/ServiciosFinancieros(NoBancarios)/')	
def A618():	
    return jsonify(resultadoCartera('QuintanaRoo','ServiciosFinancieros(NoBancarios)'))
@app.route('/QuintanaRoo/ServiciosProfesionalesyTecnicos/')	
def A619():	
    return jsonify(resultadoCartera('QuintanaRoo','ServiciosProfesionalesyTecnicos'))
@app.route('/QuintanaRoo/Transporte/')	
def A620():	
    return jsonify(resultadoCartera('QuintanaRoo','Transporte'))
@app.route('/QuintanaRoo/Bancario/')	
def A621():	
    return jsonify(resultadoCartera('QuintanaRoo','Bancario'))
@app.route('/SanLuisPotosi/AgriculturaSilviculturaGanaderiayPesca/')	
def A622():	
    return jsonify(resultadoCartera('SanLuisPotosi','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/SanLuisPotosi/AlimentosBebidasyTabaco/')	
def A623():	
    return jsonify(resultadoCartera('SanLuisPotosi','AlimentosBebidasyTabaco'))
@app.route('/SanLuisPotosi/Comercio/')	
def A624():	
    return jsonify(resultadoCartera('SanLuisPotosi','Comercio'))
@app.route('/SanLuisPotosi/ComunicacionesyTelecomunicaciones/')	
def A625():	
    return jsonify(resultadoCartera('SanLuisPotosi','ComunicacionesyTelecomunicaciones'))
@app.route('/SanLuisPotosi/Construccion/')	
def A626():	
    return jsonify(resultadoCartera('SanLuisPotosi','Construccion'))
@app.route('/SanLuisPotosi/Educativo/')	
def A627():	
    return jsonify(resultadoCartera('SanLuisPotosi','Educativo'))
@app.route('/SanLuisPotosi/GobiernoFederal/')	
def A628():	
    return jsonify(resultadoCartera('SanLuisPotosi','GobiernoFederal'))
@app.route('/SanLuisPotosi/HotelesyRestaurantes/')	
def A629():	
    
    return jsonify(resultadoCartera('SanLuisPotosi','HotelesyRestaurantes'))
@app.route('/SanLuisPotosi/IndustriaAutomotriz/')	
def A630():	
    return jsonify(resultadoCartera('SanLuisPotosi','IndustriaAutomotriz'))
@app.route('/SanLuisPotosi/IndustriaMaterialesdeConstruccion/')	
def A631():	
    return jsonify(resultadoCartera('SanLuisPotosi','IndustriaMaterialesdeConstruccion'))
@app.route('/SanLuisPotosi/IndustriaQuimicayFarmaceutica/')	
def A632():	
    return jsonify(resultadoCartera('SanLuisPotosi','IndustriaQuimicayFarmaceutica'))
@app.route('/SanLuisPotosi/IndustriaTextilydeCalzado/')	
def A633():	
    return jsonify(resultadoCartera('SanLuisPotosi','IndustriaTextilydeCalzado'))
@app.route('/SanLuisPotosi/OrganismosInternacionales/')	
def A634():	
    return jsonify(resultadoCartera('SanLuisPotosi','OrganismosInternacionales'))
@app.route('/SanLuisPotosi/PetroleoMineriaGasyEnergia/')	
def A635():	
    return jsonify(resultadoCartera('SanLuisPotosi','PetroleoMineriaGasyEnergia'))
@app.route('/SanLuisPotosi/RestoIndustria/')	
def A636():	
    return jsonify(resultadoCartera('SanLuisPotosi','RestoIndustria'))
@app.route('/SanLuisPotosi/Salud/')	
def A637():	
    return jsonify(resultadoCartera('SanLuisPotosi','Salud'))
@app.route('/SanLuisPotosi/ServiciosComunalesySociales/')	
def A638():	
    return jsonify(resultadoCartera('SanLuisPotosi','ServiciosComunalesySociales'))
@app.route('/SanLuisPotosi/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A639():	
    return jsonify(resultadoCartera('SanLuisPotosi','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/SanLuisPotosi/ServiciosFinancieros(NoBancarios)/')	
def A640():	
    return jsonify(resultadoCartera('SanLuisPotosi','ServiciosFinancieros(NoBancarios)'))
@app.route('/SanLuisPotosi/ServiciosProfesionalesyTecnicos/')	
def A641():	
    return jsonify(resultadoCartera('SanLuisPotosi','ServiciosProfesionalesyTecnicos'))
@app.route('/SanLuisPotosi/Transporte/')	
def A642():	
    return jsonify(resultadoCartera('SanLuisPotosi','Transporte'))
@app.route('/SanLuisPotosi/Bancario/')	

def A643():	
    return jsonify(resultadoCartera('SanLuisPotosi','Bancario'))
@app.route('/Sinaloa/AgriculturaSilviculturaGanaderiayPesca/')	
def A644():	
    return jsonify(resultadoCartera('Sinaloa','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Sinaloa/AlimentosBebidasyTabaco/')	
def A645():	
    return jsonify(resultadoCartera('Sinaloa','AlimentosBebidasyTabaco'))
@app.route('/Sinaloa/Comercio/')	
def A646():	
    return jsonify(resultadoCartera('Sinaloa','Comercio'))
@app.route('/Sinaloa/ComunicacionesyTelecomunicaciones/')	
def A647():	
    return jsonify(resultadoCartera('Sinaloa','ComunicacionesyTelecomunicaciones'))
@app.route('/Sinaloa/Construccion/')	
def A648():	
    return jsonify(resultadoCartera('Sinaloa','Construccion'))
@app.route('/Sinaloa/Educativo/')	
def A649():	
    return jsonify(resultadoCartera('Sinaloa','Educativo'))
@app.route('/Sinaloa/GobiernoFederal/')	
def A650():	
    return jsonify(resultadoCartera('Sinaloa','GobiernoFederal'))
@app.route('/Sinaloa/HotelesyRestaurantes/')	
def A651():	
    return jsonify(resultadoCartera('Sinaloa','HotelesyRestaurantes'))
@app.route('/Sinaloa/IndustriaAutomotriz/')	
def A652():	
    return jsonify(resultadoCartera('Sinaloa','IndustriaAutomotriz'))
@app.route('/Sinaloa/IndustriaMaterialesdeConstruccion/')	
def A653():	
    return jsonify(resultadoCartera('Sinaloa','IndustriaMaterialesdeConstruccion'))
@app.route('/Sinaloa/IndustriaQuimicayFarmaceutica/')	
def A654():	
    return jsonify(resultadoCartera('Sinaloa','IndustriaQuimicayFarmaceutica'))
@app.route('/Sinaloa/IndustriaTextilydeCalzado/')	
def A655():	
    return jsonify(resultadoCartera('Sinaloa','IndustriaTextilydeCalzado'))
@app.route('/Sinaloa/OrganismosInternacionales/')	
def A656():	
    return jsonify(resultadoCartera('Sinaloa','OrganismosInternacionales'))
@app.route('/Sinaloa/PetroleoMineriaGasyEnergia/')	
def A657():	
    return jsonify(resultadoCartera('Sinaloa','PetroleoMineriaGasyEnergia'))
@app.route('/Sinaloa/RestoIndustria/')	
def A658():	
    return jsonify(resultadoCartera('Sinaloa','RestoIndustria'))
@app.route('/Sinaloa/Salud/')	
def A659():	
    return jsonify(resultadoCartera('Sinaloa','Salud'))
@app.route('/Sinaloa/ServiciosComunalesySociales/')	
def A660():	
    return jsonify(resultadoCartera('Sinaloa','ServiciosComunalesySociales'))
@app.route('/Sinaloa/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A661():	
    return jsonify(resultadoCartera('Sinaloa','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Sinaloa/ServiciosFinancieros(NoBancarios)/')	
def A662():	
    return jsonify(resultadoCartera('Sinaloa','ServiciosFinancieros(NoBancarios)'))
@app.route('/Sinaloa/ServiciosProfesionalesyTecnicos/')	
def A663():	
    return jsonify(resultadoCartera('Sinaloa','ServiciosProfesionalesyTecnicos'))
@app.route('/Sinaloa/Transporte/')	
def A664():	
    return jsonify(resultadoCartera('Sinaloa','Transporte'))
@app.route('/Sinaloa/Bancario/')	
def A665():	
    return jsonify(resultadoCartera('Sinaloa','Bancario'))
@app.route('/Sonora/AgriculturaSilviculturaGanaderiayPesca/')	
def A666():	
    return jsonify(resultadoCartera('Sonora','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Sonora/AlimentosBebidasyTabaco/')	
def A667():	
    return jsonify(resultadoCartera('Sonora','AlimentosBebidasyTabaco'))
@app.route('/Sonora/Comercio/')	
def A668():	
    return jsonify(resultadoCartera('Sonora','Comercio'))
@app.route('/Sonora/ComunicacionesyTelecomunicaciones/')	
def A669():	
    return jsonify(resultadoCartera('Sonora','ComunicacionesyTelecomunicaciones'))
@app.route('/Sonora/Construccion/')	
def A670():	
    return jsonify(resultadoCartera('Sonora','Construccion'))
@app.route('/Sonora/Educativo/')	
def A671():	
    return jsonify(resultadoCartera('Sonora','Educativo'))
@app.route('/Sonora/GobiernoFederal/')	
def A672():	
    return jsonify(resultadoCartera('Sonora','GobiernoFederal'))
@app.route('/Sonora/HotelesyRestaurantes/')	
def A673():	
    return jsonify(resultadoCartera('Sonora','HotelesyRestaurantes'))
@app.route('/Sonora/IndustriaAutomotriz/')	
def A674():	
    return jsonify(resultadoCartera('Sonora','IndustriaAutomotriz'))
@app.route('/Sonora/IndustriaMaterialesdeConstruccion/')	
def A675():	
    return jsonify(resultadoCartera('Sonora','IndustriaMaterialesdeConstruccion'))
@app.route('/Sonora/IndustriaQuimicayFarmaceutica/')	
def A676():	
    return jsonify(resultadoCartera('Sonora','IndustriaQuimicayFarmaceutica'))
@app.route('/Sonora/IndustriaTextilydeCalzado/')	
def A677():	
    
    return jsonify(resultadoCartera('Sonora','IndustriaTextilydeCalzado'))
@app.route('/Sonora/OrganismosInternacionales/')	
def A678():	
    return jsonify(resultadoCartera('Sonora','OrganismosInternacionales'))
@app.route('/Sonora/PetroleoMineriaGasyEnergia/')	
def A679():	
    return jsonify(resultadoCartera('Sonora','PetroleoMineriaGasyEnergia'))
@app.route('/Sonora/RestoIndustria/')	
def A680():	
    return jsonify(resultadoCartera('Sonora','RestoIndustria'))
@app.route('/Sonora/Salud/')	
def A681():	
    return jsonify(resultadoCartera('Sonora','Salud'))
@app.route('/Sonora/ServiciosComunalesySociales/')	
def A682():	
    return jsonify(resultadoCartera('Sonora','ServiciosComunalesySociales'))
@app.route('/Sonora/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A683():	
    return jsonify(resultadoCartera('Sonora','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Sonora/ServiciosFinancieros(NoBancarios)/')	
def A684():	
    return jsonify(resultadoCartera('Sonora','ServiciosFinancieros(NoBancarios)'))
@app.route('/Sonora/ServiciosProfesionalesyTecnicos/')	
def A685():	
    return jsonify(resultadoCartera('Sonora','ServiciosProfesionalesyTecnicos'))
@app.route('/Sonora/Transporte/')	
def A686():	
    
    return jsonify(resultadoCartera('Sonora','Transporte'))
@app.route('/Sonora/Bancario/')	
def A687():	
    return jsonify(resultadoCartera('Sonora','Bancario'))
@app.route('/Tabasco/AgriculturaSilviculturaGanaderiayPesca/')	
def A688():	
    return jsonify(resultadoCartera('Tabasco','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Tabasco/AlimentosBebidasyTabaco/')	
def A689():	
    return jsonify(resultadoCartera('Tabasco','AlimentosBebidasyTabaco'))
@app.route('/Tabasco/Comercio/')	
def A690():	
    return jsonify(resultadoCartera('Tabasco','Comercio'))
@app.route('/Tabasco/ComunicacionesyTelecomunicaciones/')	
def A691():	
    return jsonify(resultadoCartera('Tabasco','ComunicacionesyTelecomunicaciones'))
@app.route('/Tabasco/Construccion/')	
def A692():	
    return jsonify(resultadoCartera('Tabasco','Construccion'))
@app.route('/Tabasco/Educativo/')	
def A693():	return jsonify(resultadoCartera('Tabasco','Educativo'))
@app.route('/Tabasco/GobiernoFederal/')	
def A694():	
    return jsonify(resultadoCartera('Tabasco','GobiernoFederal'))
@app.route('/Tabasco/HotelesyRestaurantes/')	
def A695():	
    return jsonify(resultadoCartera('Tabasco','HotelesyRestaurantes'))
@app.route('/Tabasco/IndustriaAutomotriz/')	
def A696():	
    return jsonify(resultadoCartera('Tabasco','IndustriaAutomotriz'))
@app.route('/Tabasco/IndustriaMaterialesdeConstruccion/')	
def A697():	
    return jsonify(resultadoCartera('Tabasco','IndustriaMaterialesdeConstruccion'))
@app.route('/Tabasco/IndustriaQuimicayFarmaceutica/')	
def A698():	
    return jsonify(resultadoCartera('Tabasco','IndustriaQuimicayFarmaceutica'))
@app.route('/Tabasco/IndustriaTextilydeCalzado/')	
def A699():	
    return jsonify(resultadoCartera('Tabasco','IndustriaTextilydeCalzado'))
@app.route('/Tabasco/OrganismosInternacionales/')	
def A700():	
    return jsonify(resultadoCartera('Tabasco','OrganismosInternacionales'))
@app.route('/Tabasco/PetroleoMineriaGasyEnergia/')	
def A701():	
    return jsonify(resultadoCartera('Tabasco','PetroleoMineriaGasyEnergia'))
@app.route('/Tabasco/RestoIndustria/')	
def A702():	
    return jsonify(resultadoCartera('Tabasco','RestoIndustria'))
@app.route('/Tabasco/Salud/')	
def A703():	
    return jsonify(resultadoCartera('Tabasco','Salud'))
@app.route('/Tabasco/ServiciosComunalesySociales/')	
def A704():	
    return jsonify(resultadoCartera('Tabasco','ServiciosComunalesySociales'))
@app.route('/Tabasco/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A705():	
    return jsonify(resultadoCartera('Tabasco','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Tabasco/ServiciosFinancieros(NoBancarios)/')	
def A706():	
    return jsonify(resultadoCartera('Tabasco','ServiciosFinancieros(NoBancarios)'))
@app.route('/Tabasco/ServiciosProfesionalesyTecnicos/')
def A707():	
    return jsonify(resultadoCartera('Tabasco','ServiciosProfesionalesyTecnicos'))
@app.route('/Tabasco/Transporte/')	
def A708():	
    return jsonify(resultadoCartera('Tabasco','Transporte'))
@app.route('/Tabasco/Bancario/')	
def A709():	
    return jsonify(resultadoCartera('Tabasco','Bancario'))
@app.route('/Tamaulipas/AgriculturaSilviculturaGanaderiayPesca/')	
def A710():	
    return jsonify(resultadoCartera('Tamaulipas','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Tamaulipas/AlimentosBebidasyTabaco/')	
def A711():	
    return jsonify(resultadoCartera('Tamaulipas','AlimentosBebidasyTabaco'))
@app.route('/Tamaulipas/Comercio/')	
def A712():	
    return jsonify(resultadoCartera('Tamaulipas','Comercio'))
@app.route('/Tamaulipas/ComunicacionesyTelecomunicaciones/')	
def A713():	
    return jsonify(resultadoCartera('Tamaulipas','ComunicacionesyTelecomunicaciones'))
@app.route('/Tamaulipas/Construccion/')	
def A714():	
    return jsonify(resultadoCartera('Tamaulipas','Construccion'))
@app.route('/Tamaulipas/Educativo/')	
def A715():	
    return jsonify(resultadoCartera('Tamaulipas','Educativo'))
@app.route('/Tamaulipas/GobiernoFederal/')	
def A716():	
    return jsonify(resultadoCartera('Tamaulipas','GobiernoFederal'))
@app.route('/Tamaulipas/HotelesyRestaurantes/')	
def A717():	
    return jsonify(resultadoCartera('Tamaulipas','HotelesyRestaurantes'))
@app.route('/Tamaulipas/IndustriaAutomotriz/')	
def A718():	
    return jsonify(resultadoCartera('Tamaulipas','IndustriaAutomotriz'))
@app.route('/Tamaulipas/IndustriaMaterialesdeConstruccion/')	
def A719():	
    return jsonify(resultadoCartera('Tamaulipas','IndustriaMaterialesdeConstruccion'))
@app.route('/Tamaulipas/IndustriaQuimicayFarmaceutica/')	
def A720():	
    return jsonify(resultadoCartera('Tamaulipas','IndustriaQuimicayFarmaceutica'))
@app.route('/Tamaulipas/IndustriaTextilydeCalzado/')	
def A721():	
    return jsonify(resultadoCartera('Tamaulipas','IndustriaTextilydeCalzado'))
@app.route('/Tamaulipas/OrganismosInternacionales/')	
def A722():	
    return jsonify(resultadoCartera('Tamaulipas','OrganismosInternacionales'))
@app.route('/Tamaulipas/PetroleoMineriaGasyEnergia/')	
def A723():	
    return jsonify(resultadoCartera('Tamaulipas','PetroleoMineriaGasyEnergia'))
@app.route('/Tamaulipas/RestoIndustria/')	
def A724():	
    return jsonify(resultadoCartera('Tamaulipas','RestoIndustria'))
@app.route('/Tamaulipas/Salud/')	
def A725():	
    return jsonify(resultadoCartera('Tamaulipas','Salud'))
@app.route('/Tamaulipas/ServiciosComunalesySociales/')	
def A726():	
    return jsonify(resultadoCartera('Tamaulipas','ServiciosComunalesySociales'))
@app.route('/Tamaulipas/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A727():	
    return jsonify(resultadoCartera('Tamaulipas','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Tamaulipas/ServiciosFinancieros(NoBancarios)/')	
def A728():	
    return jsonify(resultadoCartera('Tamaulipas','ServiciosFinancieros(NoBancarios)'))
@app.route('/Tamaulipas/ServiciosProfesionalesyTecnicos/')	
def A729():	
    return jsonify(resultadoCartera('Tamaulipas','ServiciosProfesionalesyTecnicos'))
@app.route('/Tamaulipas/Transporte/')	
def A730():	
    return jsonify(resultadoCartera('Tamaulipas','Transporte'))
@app.route('/Tamaulipas/Bancario/')	
def A731():	
    return jsonify(resultadoCartera('Tamaulipas','Bancario'))
@app.route('/Tlaxcala/AgriculturaSilviculturaGanaderiayPesca/')	
def A732():
    return jsonify(resultadoCartera('Tlaxcala','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Tlaxcala/AlimentosBebidasyTabaco/')	
def A733():	
    return jsonify(resultadoCartera('Tlaxcala','AlimentosBebidasyTabaco'))
@app.route('/Tlaxcala/Comercio/')	
def A734():	
    
    return jsonify(resultadoCartera('Tlaxcala','Comercio'))
@app.route('/Tlaxcala/ComunicacionesyTelecomunicaciones/')	
def A735():	
    return jsonify(resultadoCartera('Tlaxcala','ComunicacionesyTelecomunicaciones'))
@app.route('/Tlaxcala/Construccion/')	
def A736():	
    return jsonify(resultadoCartera('Tlaxcala','Construccion'))
@app.route('/Tlaxcala/Educativo/')	
def A737():	
    return jsonify(resultadoCartera('Tlaxcala','Educativo'))
@app.route('/Tlaxcala/GobiernoFederal/')	
def A738():	
    
    return jsonify(resultadoCartera('Tlaxcala','GobiernoFederal'))
@app.route('/Tlaxcala/HotelesyRestaurantes/')	
def A739():	
    return jsonify(resultadoCartera('Tlaxcala','HotelesyRestaurantes'))
@app.route('/Tlaxcala/IndustriaAutomotriz/')	
def A740():	
    return jsonify(resultadoCartera('Tlaxcala','IndustriaAutomotriz'))
@app.route('/Tlaxcala/IndustriaMaterialesdeConstruccion/')	
def A741():	
    return jsonify(resultadoCartera('Tlaxcala','IndustriaMaterialesdeConstruccion'))
@app.route('/Tlaxcala/IndustriaQuimicayFarmaceutica/')	
def A742():	
    return jsonify(resultadoCartera('Tlaxcala','IndustriaQuimicayFarmaceutica'))
@app.route('/Tlaxcala/IndustriaTextilydeCalzado/')	
def A743():	
    return jsonify(resultadoCartera('Tlaxcala','IndustriaTextilydeCalzado'))
@app.route('/Tlaxcala/OrganismosInternacionales/')	
def A744():	
    return jsonify(resultadoCartera('Tlaxcala','OrganismosInternacionales'))
@app.route('/Tlaxcala/PetroleoMineriaGasyEnergia/')	
def A745():	
    return jsonify(resultadoCartera('Tlaxcala','PetroleoMineriaGasyEnergia'))
@app.route('/Tlaxcala/RestoIndustria/')	
def A746():	
    return jsonify(resultadoCartera('Tlaxcala','RestoIndustria'))
@app.route('/Tlaxcala/Salud/')	
def A747():	
    return jsonify(resultadoCartera('Tlaxcala','Salud'))
@app.route('/Tlaxcala/ServiciosComunalesySociales/')	
def A748():	
    return jsonify(resultadoCartera('Tlaxcala','ServiciosComunalesySociales'))
@app.route('/Tlaxcala/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A749():	
    return jsonify(resultadoCartera('Tlaxcala','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Tlaxcala/ServiciosFinancieros(NoBancarios)/')	
def A750():	
    return jsonify(resultadoCartera('Tlaxcala','ServiciosFinancieros(NoBancarios)'))
@app.route('/Tlaxcala/ServiciosProfesionalesyTecnicos/')	
def A751():	
    return jsonify(resultadoCartera('Tlaxcala','ServiciosProfesionalesyTecnicos'))
@app.route('/Tlaxcala/Transporte/')	
def A752():	
    
    return jsonify(resultadoCartera('Tlaxcala','Transporte'))
@app.route('/Tlaxcala/Bancario/')	

def A753():	
    return jsonify(resultadoCartera('Tlaxcala','Bancario'))
@app.route('/Veracruz/AgriculturaSilviculturaGanaderiayPesca/')	
def A754():	
    return jsonify(resultadoCartera('Veracruz','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Veracruz/AlimentosBebidasyTabaco/')	
def A755():	
    return jsonify(resultadoCartera('Veracruz','AlimentosBebidasyTabaco'))
@app.route('/Veracruz/Comercio/')	

def A756():	
    return jsonify(resultadoCartera('Veracruz','Comercio'))
@app.route('/Veracruz/ComunicacionesyTelecomunicaciones/')	
def A757():	
    return jsonify(resultadoCartera('Veracruz','ComunicacionesyTelecomunicaciones'))
@app.route('/Veracruz/Construccion/')	
def A758():	
    return jsonify(resultadoCartera('Veracruz','Construccion'))
@app.route('/Veracruz/Educativo/')	
def A759():	
    
    return jsonify(resultadoCartera('Veracruz','Educativo'))
@app.route('/Veracruz/GobiernoFederal/')	
def A760():	
    return jsonify(resultadoCartera('Veracruz','GobiernoFederal'))
@app.route('/Veracruz/HotelesyRestaurantes/')	
def A761():	
    return jsonify(resultadoCartera('Veracruz','HotelesyRestaurantes'))
@app.route('/Veracruz/IndustriaAutomotriz/')	
def A762():	
    return jsonify(resultadoCartera('Veracruz','IndustriaAutomotriz'))
@app.route('/Veracruz/IndustriaMaterialesdeConstruccion/')	
def A763():	
    return jsonify(resultadoCartera('Veracruz','IndustriaMaterialesdeConstruccion'))
@app.route('/Veracruz/IndustriaQuimicayFarmaceutica/')	
def A764():	
    return jsonify(resultadoCartera('Veracruz','IndustriaQuimicayFarmaceutica'))
@app.route('/Veracruz/IndustriaTextilydeCalzado/')	
def A765():	
    
    return jsonify(resultadoCartera('Veracruz','IndustriaTextilydeCalzado'))
@app.route('/Veracruz/OrganismosInternacionales/')	
def A766():	
    return jsonify(resultadoCartera('Veracruz','OrganismosInternacionales'))
@app.route('/Veracruz/PetroleoMineriaGasyEnergia/')	
def A767():	
    return jsonify(resultadoCartera('Veracruz','PetroleoMineriaGasyEnergia'))
@app.route('/Veracruz/RestoIndustria/')	
def A768():	
    return jsonify(resultadoCartera('Veracruz','RestoIndustria'))
@app.route('/Veracruz/Salud/')	
def A769():	
    return jsonify(resultadoCartera('Veracruz','Salud'))
@app.route('/Veracruz/ServiciosComunalesySociales/')	
def A770():	
    return jsonify(resultadoCartera('Veracruz','ServiciosComunalesySociales'))
@app.route('/Veracruz/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A771():	
    return jsonify(resultadoCartera('Veracruz','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Veracruz/ServiciosFinancieros(NoBancarios)/')	
def A772():	
    return jsonify(resultadoCartera('Veracruz','ServiciosFinancieros(NoBancarios)'))
@app.route('/Veracruz/ServiciosProfesionalesyTecnicos/')	

def A773():	
    return jsonify(resultadoCartera('Veracruz','ServiciosProfesionalesyTecnicos'))
@app.route('/Veracruz/Transporte/')	
def A774():	
    return jsonify(resultadoCartera('Veracruz','Transporte'))
@app.route('/Veracruz/Bancario/')	
def A775():	
    return jsonify(resultadoCartera('Veracruz','Bancario'))
@app.route('/Yucatan/AgriculturaSilviculturaGanaderiayPesca/')	
def A776():	
    return jsonify(resultadoCartera('Yucatan','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Yucatan/AlimentosBebidasyTabaco/')	
def A777():	
    return jsonify(resultadoCartera('Yucatan','AlimentosBebidasyTabaco'))
@app.route('/Yucatan/Comercio/')	
def A778():	
    return jsonify(resultadoCartera('Yucatan','Comercio'))
@app.route('/Yucatan/ComunicacionesyTelecomunicaciones/')	
def A779():	
    return jsonify(resultadoCartera('Yucatan','ComunicacionesyTelecomunicaciones'))
@app.route('/Yucatan/Construccion/')	
def A780():	
    return jsonify(resultadoCartera('Yucatan','Construccion'))
@app.route('/Yucatan/Educativo/')	
def A781():	
    return jsonify(resultadoCartera('Yucatan','Educativo'))
@app.route('/Yucatan/GobiernoFederal/')	
def A782():	
    return jsonify(resultadoCartera('Yucatan','GobiernoFederal'))
@app.route('/Yucatan/HotelesyRestaurantes/')	
def A783():	
    return jsonify(resultadoCartera('Yucatan','HotelesyRestaurantes'))
@app.route('/Yucatan/IndustriaAutomotriz/')	
def A784():	
    return jsonify(resultadoCartera('Yucatan','IndustriaAutomotriz'))
@app.route('/Yucatan/IndustriaMaterialesdeConstruccion/')	
def A785():	
    return jsonify(resultadoCartera('Yucatan','IndustriaMaterialesdeConstruccion'))
@app.route('/Yucatan/IndustriaQuimicayFarmaceutica/')	
def A786():	
    return jsonify(resultadoCartera('Yucatan','IndustriaQuimicayFarmaceutica'))
@app.route('/Yucatan/IndustriaTextilydeCalzado/')	

def A787():	
    
    return jsonify(resultadoCartera('Yucatan','IndustriaTextilydeCalzado'))
@app.route('/Yucatan/OrganismosInternacionales/')	
def A788():	
    return jsonify(resultadoCartera('Yucatan','OrganismosInternacionales'))
@app.route('/Yucatan/PetroleoMineriaGasyEnergia/')	
def A789():	
    return jsonify(resultadoCartera('Yucatan','PetroleoMineriaGasyEnergia'))
@app.route('/Yucatan/RestoIndustria/')	
def A790():	
    return jsonify(resultadoCartera('Yucatan','RestoIndustria'))
@app.route('/Yucatan/Salud/')	
def A791():	
    return jsonify(resultadoCartera('Yucatan','Salud'))
@app.route('/Yucatan/ServiciosComunalesySociales/')	
def A792():	
    return jsonify(resultadoCartera('Yucatan','ServiciosComunalesySociales'))
@app.route('/Yucatan/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A793():	
    return jsonify(resultadoCartera('Yucatan','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Yucatan/ServiciosFinancieros(NoBancarios)/')	
def A794():	
    return jsonify(resultadoCartera('Yucatan','ServiciosFinancieros(NoBancarios)'))
@app.route('/Yucatan/ServiciosProfesionalesyTecnicos/')	
def A795():	
    return jsonify(resultadoCartera('Yucatan','ServiciosProfesionalesyTecnicos'))
@app.route('/Yucatan/Transporte/')	
def A796():	
    return jsonify(resultadoCartera('Yucatan','Transporte'))
@app.route('/Yucatan/Bancario/')	
def A797():	
    return jsonify(resultadoCartera('Yucatan','Bancario'))
@app.route('/Zacatecas/AgriculturaSilviculturaGanaderiayPesca/')	
def A798():	
    return jsonify(resultadoCartera('Zacatecas','AgriculturaSilviculturaGanaderiayPesca'))
@app.route('/Zacatecas/AlimentosBebidasyTabaco/')	
def A799():	
    return jsonify(resultadoCartera('Zacatecas','AlimentosBebidasyTabaco'))
@app.route('/Zacatecas/Comercio/')	
def A800():	
    return jsonify(resultadoCartera('Zacatecas','Comercio'))
@app.route('/Zacatecas/ComunicacionesyTelecomunicaciones/')	
def A801():	
    return jsonify(resultadoCartera('Zacatecas','ComunicacionesyTelecomunicaciones'))
@app.route('/Zacatecas/Construccion/')	
def A802():	
    return jsonify(resultadoCartera('Zacatecas','Construccion'))
@app.route('/Zacatecas/Educativo/')	
def A803():	
    return jsonify(resultadoCartera('Zacatecas','Educativo'))
@app.route('/Zacatecas/GobiernoFederal/')	
def A804():	
    return jsonify(resultadoCartera('Zacatecas','GobiernoFederal'))
@app.route('/Zacatecas/HotelesyRestaurantes/')	
def A805():	
    return jsonify(resultadoCartera('Zacatecas','HotelesyRestaurantes'))
@app.route('/Zacatecas/IndustriaAutomotriz/')	
def A806():	
    return jsonify(resultadoCartera('Zacatecas','IndustriaAutomotriz'))
@app.route('/Zacatecas/IndustriaMaterialesdeConstruccion/')	
def A807():	
    return jsonify(resultadoCartera('Zacatecas','IndustriaMaterialesdeConstruccion'))
@app.route('/Zacatecas/IndustriaQuimicayFarmaceutica/')	
def A808():	
    return jsonify(resultadoCartera('Zacatecas','IndustriaQuimicayFarmaceutica'))
@app.route('/Zacatecas/IndustriaTextilydeCalzado/')	
def A809():	
    return jsonify(resultadoCartera('Zacatecas','IndustriaTextilydeCalzado'))
@app.route('/Zacatecas/OrganismosInternacionales/')	
def A810():	
    return jsonify(resultadoCartera('Zacatecas','OrganismosInternacionales'))
@app.route('/Zacatecas/PetroleoMineriaGasyEnergia/')	
def A811():	
    return jsonify(resultadoCartera('Zacatecas','PetroleoMineriaGasyEnergia'))
@app.route('/Zacatecas/RestoIndustria/')	
def A812():	
    return jsonify(resultadoCartera('Zacatecas','RestoIndustria'))
@app.route('/Zacatecas/Salud/')	
def A813():	
    return jsonify(resultadoCartera('Zacatecas','Salud'))
@app.route('/Zacatecas/ServiciosComunalesySociales/')	
def A814():	
    return jsonify(resultadoCartera('Zacatecas','ServiciosComunalesySociales'))
@app.route('/Zacatecas/ServiciosdeEsparcimientoyotrosServiciosRecreativo/')	
def A815():	
    return jsonify(resultadoCartera('Zacatecas','ServiciosdeEsparcimientoyotrosServiciosRecreativo'))
@app.route('/Zacatecas/ServiciosFinancieros(NoBancarios)/')	
def A816():	
    return jsonify(resultadoCartera('Zacatecas','ServiciosFinancieros(NoBancarios)'))
@app.route('/Zacatecas/ServiciosProfesionalesyTecnicos/')	
def A817():	
    return jsonify(resultadoCartera('Zacatecas','ServiciosProfesionalesyTecnicos'))
@app.route('/Zacatecas/Transporte/')	
def A818():	
    return jsonify(resultadoCartera('Zacatecas','Transporte'))
@app.route('/Zacatecas/Bancario/')	
def A819():	
    return jsonify(resultadoCartera('Zacatecas','Bancario'))



    

if __name__ == '__main__':
    app.run(debug=True)
