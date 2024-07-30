import Connection
import psycopg2

class Affaire:
    def __init__(self):
        self.puParMCube = 0
        self.tempsParMCube = 0
        self.typeRoad = 0

    def __init__(self, puParMCube, tempsParCube, typeRoad):
        self.puParMCube = puParMCube
        self.tempsParMCube = tempsParCube
        self.typeRoad = typeRoad

    def getPuParMcube(self) :
        return self.puMetreCube

    def getTempsParMCube(self) :
        return self.tempsMetreCube

    def getTypeRoad(self) :
        return self.typeRoad

    def setPuParMcube(self, puParMCube) :
        self.puParMCube = puParMCube

    def setTempsParMcube(self, tempsParMCube) :
        self.tempsParMCube = tempsParMCube

    def setTypeRoad(self, typeRoad) :
        self.typeRoad = typeRoad       

#Avoir la ligne de l'idType sur la table affaire
    def getAffaire(self, idType) :
        try :
            conne = Connection.Connection()
            conn = conne.connect()
            query = "SELECT * FROM affaire where typeRoad = " + str(idType)
            conn.execute(query)
            data = conn.fetchone()

            return data
        except (Exception, psycopg2.DatabaseError) as error :
            print(error)
    