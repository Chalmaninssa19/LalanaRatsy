class Time(object):
    "Encore une nouvelle classe temporelle"
    def __init__(self):
        self.heure =12
        self.minute =0
        self.seconde =0
    def affiche_heure(self):
        print("{0}:{1}:{2}".format(self.heure, self.minute, self.seconde))
tstart = Time()
tstart.affiche_heure()