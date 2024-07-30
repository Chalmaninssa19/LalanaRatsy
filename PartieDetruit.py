import Connection
import psycopg2

class PartieDetruit:
    def __init__(self, route, affaire, pkDebut, pkFin, niveau):
        self.route = route
        self.affaire = affaire
        self.pkDebut = pkDebut
        self.pkFin = pkFin
        self.niveau = niveau

#Getters et setters
    def getRoute(self):
        return self.route

    def getAffaire(self):
        return self.affaire

    def getPkDebut(self):
        return self.pkDebut

    def getPkFin(self):
        return self.pkFin

    def getNiveau(self):
        return self.niveau

    def setRoute(self, route) :
        self.route = route

    def setAffaire(self, affaire) :
        self.affaire = affaire

    def setPkDebut(self, pkDebut) :
        self.pkDebut = pkDebut

    def setPkFin(self, pkFin) :
        self.pkFin = pkFin

    def setNiveau(self, niveau) :
        self.niveau = niveau

#Avoir la liste des routes detruits
    def allRoadDetruit(self) :
        try :
            conne = Connection.Connection()
            conn = conne.connect()
            query = "SELECT * FROM partieDetruit"
            conn.execute(query)
            data = conn.fetchall()

            return data
        except (Exception, psycopg2.DatabaseError) as error :
            print(error)

    def getRoadDetails(self, idRoute) :
        try :
            conne = Connection.Connection()
            conn = conne.connect()
            query = "SELECT * FROM madagascar_roads where gid = " + str(idRoute)
            conn.execute(query)
            data = conn.fetchone()

            return data
        except (Exception, psycopg2.DatabaseError) as error :
            print(error)

    def getRoadDetruit(self, idRoute) :
        try :
            conne = Connection.Connection()
            conn = conne.connect()
            query = "SELECT * FROM partieDetruit where idRoute = " + str(idRoute)
            conn.execute(query)
            data = conn.fetchone()

            return data
        except (Exception, psycopg2.DatabaseError) as error :
            print(error)

    def getCoordRoadDetruit(self, idRoute) :
        try :
            conne = Connection.Connection()
            conn = conne.connect()
            query = "SELECT * FROM RoadCoordinate"
            conn.execute(query)
            data = conn.fetchall()

            return data
        except (Exception, psycopg2.DatabaseError) as error :
            print(error)

#Cout pour preparer la partie detruit
    def coutReparation(self) :
        return self.route.volume()*self.affaire.puParMCube

#duree pour finir la construction
    def dureeReparaton(self) :
        return self.route.volume()*self.affaire.tempsParMCube
