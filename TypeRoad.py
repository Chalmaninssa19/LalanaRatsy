import Connection
import psycopg2

class TypeRoad:
    def __init__(self, idTypeRoad, nom):
        self.idTypeRoad = idTypeRoad
        self.nom = nom

    def getIdTypeRoad(self) :
        return self.idTypeRoad

    def getNom(self) :
        return self.nom

    def setIdTypeRoad(self, idTypeRoad) :
        self.idTypeRoad = idTypeRoad

    def setNom(self, nom) :
        self.nom = nom

#Avoir la ligne de l'idType sur la table affaire
    def getIdTypeRoad(self, nom) :
        try :
            conne = Connection.Connection()
            conn = conne.connect()
            query = "SELECT id FROM typeRoad where value = '" + nom + "'"
            conn.execute(query)
            data = conn.fetchone()

            return data
        except (Exception, psycopg2.DatabaseError) as error :
            print(error)
    