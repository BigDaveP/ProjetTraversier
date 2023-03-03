
class Personne:
    def __init__(self, nom, adresse, ville, province, codePostal, telephone, courriel):
        self.nom = nom
        self.adresse = adresse
        self.ville = ville
        self.province = province
        self.codePostal = codePostal
        self.telephone = telephone
        self.courriel = courriel


    def __str__(self):
        return "Personne [numeroIdentification=" + self.nom + ", adresse=" + self.adresse + ", ville=" + self.ville + ", province=" + self.province + ", codePostal=" + self.codePostal + ", telephone=" + self.telephone + ", courriel=" + self.courriel + "]"

    def getHashCode(self):
        return self.nom

    def Equals(self, other):
        return self.nom == other.nom