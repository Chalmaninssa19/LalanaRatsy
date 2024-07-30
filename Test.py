#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import *
from PartieDetruit import *
from Route import *
from TypeRoad import *
from Affaire import *

app = Flask(__name__)

@app.route('/')
def accueil():
    mots = ["bonjour", "à", "toi,", "visiteur."]
    pd = PartieDetruit(0, 0, 0, 0, 0)
    datas = pd.allRoadDetruit()
    donnees = []
    for data in datas :
        donnees.append(pd.getRoadDetails(data[1]))
    return render_template('index.html', titre="Route national simba !", donnes = donnees)

@app.route('/', methods=["GET","POST"])
def affiche():
    idRoute = request.form.get('lalana') 
    pd = PartieDetruit(0, 0, 0, 0, 0)
    pdDetails = pd.getRoadDetruit(idRoute)  
    roadDetails = pd.getRoadDetails(idRoute)
    longueurDetruit = pdDetails[4]-pdDetails[3]
    largeurDetruit = 5
    epaisseurDetruit = pdDetails[5]/10
    route = Route(longueurDetruit, largeurDetruit, epaisseurDetruit)
    volume = route.volume()

    affaire = Affaire(0, 0, 0)
    typeRoad = TypeRoad(0, "")
    aff = affaire.getAffaire(typeRoad.getIdTypeRoad("goudron")[0])
    affaire.setPuParMcube(aff[1])
    affaire.setTempsParMcube(aff[2])
    affaire.setTypeRoad(aff[3])
    partieDetruit = PartieDetruit(route, affaire, pdDetails[3], pdDetails[4], epaisseurDetruit)
    coutReparation = partieDetruit.coutReparation()
    dureeReparaton = partieDetruit.dureeReparaton()

    return render_template('affiche.html', titre="Details du route detruit", detailsRoad=roadDetails, partieD=pdDetails, epaisseur=epaisseurDetruit, coutR=coutReparation, timeR=dureeReparaton, volumeD=volume)


@app.route('/')
def traceRoute():
    datas = Route.get_road_coordonate()
    return render_template('index.html', titre="Route national simba !", roads = datas)
if __name__ == '__main__':
    app.run(debug=True)     