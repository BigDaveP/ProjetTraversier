class Type:
    def __init__(self, nom, nombreRoues, prixTraverse):
        self.nom = nom
        self.nombreRoues = nombreRoues
        self.prixTraverse = prixTraverse

    def __str__(self):
        return "Type [nom=" + self.nom + ", nombreRoues=" + self.nombreRoues + ", prixTraverse=" + self.prixTraverse + "]"

    def getHashCode(self):
        return self.nom

    def Equals(self, other):
        return self.nom == other.nom

