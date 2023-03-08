
from Models.personne import Personne

class Client(Personne):
    def __init__(self, numeroIdentification, nom, adresse, ville, province, codePostal, telephone, courriel, sexe, dateNaissance, vehicule):
        super().__init__(nom, adresse, ville, province, codePostal, telephone, courriel)
        self.sexe = sexe
        self.dateNaissance = dateNaissance
        self.numeroIdentification = numeroIdentification
        self.vehicule = vehicule

    def __str__(self):
        return "Client [noClient=" + self.numeroIdentification + ", dateNaissance" + self.dateNaissance + "]"

    def getHashCode(self):
        return self.numeroIdentification

    def Equals(self, other):
        return self.numeroIdentification == other.numeroIdentification