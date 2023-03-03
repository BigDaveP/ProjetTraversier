
class Traversier:
    def __init__(self, nom, capaciteVehicule, capacitePersonne, anneeFabrication, dateMiseService, listeEmploye):
        self.nom = nom
        self.capaciteVehicule = capaciteVehicule
        self.capacitePersonne = capacitePersonne
        self.anneeFabrication = anneeFabrication
        self.dateMiseService = dateMiseService
        self.listeEmploye = listeEmploye

    def __str__(self):
        return "Traversier [nom=" + self.nom + ", capaciteVehicule=" + self.capaciteVehicule + ", capacitePersonne=" + self.capacitePersonne + ", anneeFabrication=" + self.anneeFabrication + ", dateMiseService=" + self.dateMiseService + ", listeEmploye=" + self.listeEmploye + "]"

    def getHashCode(self):
        return self.nom

    def Equals(self, other):
        return self.nom == other.nom

    def ajouterEmploye(self, employe):
        self.listeEmploye.append(employe)

    def supprimerEmploye(self, employe):
        self.listeEmploye.remove(employe)

