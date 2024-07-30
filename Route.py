import Connection

class Route(object):
#Constructors
    def __init__(self) :
        self.longueur = 0
        self.largeur = 0
        self.epaisseur = 0
    def __init__(self, longueur, largeur, epaisseur):
        self.longueur = longueur
        self.largeur = largeur
        self.epaisseur = epaisseur

    def getLongueur(self) :
        return self.longueur
    def getLargeur(self) :
        return self.largeur
    def getEpaisseur(self) :
        return self.epaisseur
#Fonctions

    #calcule le volume de la route
    def volume(self):
        return self.longueur*self.largeur*self.epaisseur

    def getRouteDetails(self, idRoute) :
        try :
            conne = Connection.Connection()
            conn = conne.connect()
            query = "SELECT * FROM madagascar_roads where gid = " + str(idRoute)
            conn.execute(query)
            data = conn.fetchone()

            return data
        except (Exception, psycopg2.DatabaseError) as error :
            print(error)

    def get_road_coordonate(self):
        conn = Connection.Connection()
        try:
            query = "SELECT geoJSON,longitude,latitude FROM roadCoordinate"
            print(query)
            connect = conn.connect()
            connect.execute(query)
            data = connect.fetchall()
            return data
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally :
            conn.disconnect()
            

            