
from Models.personne import Personne

class Employe(Personne):
    def __init__(self, noEmployer, nAS, dateEmbauche, dateArret, nom, adresse, ville, province,
                 codePostal, telephone, courriel):
        super().__init__(nom, adresse, ville, province, codePostal, telephone, courriel)
        self.noEmployer = noEmployer
        self.nAS = nAS
        self.dateEmbauche = dateEmbauche
        self.dateArret = dateArret

    def __str__(self):
        return "Employe [noEmployer=" + self.noEmployer + ", nAS=" + self.nAS + ", dateEmbauche=" + self.dateEmbauche + ", dateArret=" + self.dateArret + "]"

    def getHashCode(self):
        return self.noEmployer

    def Equals(self, other):
        return self.noEmployer == other.noEmployer
