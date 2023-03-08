
class Vehicule:
    def __init__(self, noIdentification, marque, modele, couleur, annee, immitraculation, typeDeVehicule):
        self.noIdentification = noIdentification
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.annee = annee
        self.immitraculation = immitraculation
        self.typeDeVehicule = typeDeVehicule

    def __str__(self):
        return "Vehicule [noIdentification=" + self.noIdentification + ", marque=" + self.marque + ", modele=" + self.modele + ", couleur=" + self.couleur + ", annee=" + self.annee + ", immitraculation=" + self.immitraculation + ", typeDeVehicule=" + self.typeDeVehicule + "]"

    def getHashCode(self):
        return self.noIdentification

    def Equals(self, other):
        return self.noIdentification == other.noIdentification

