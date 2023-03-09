
class Traverse:
        def __init__(self, noTraverse, dateHeure, villeDepart, employeInscription, listeVehicule, listeClient):
            self.noTraverse = noTraverse
            self.dateHeure = dateHeure
            self.villeDepart = villeDepart
            self.employeInscription = employeInscription
            self.listeVehicule = listeVehicule
            self.listeClient = listeClient

        def __str__(self):
            return "Traverse [noTraverse=" + self.noTraverse + ", dateHeure=" + self.dateHeure + ", villeDepart=" + self.villeDepart + ", employeInscription=" + self.employeInscription + ", listeVehecule=" + self.listeVehecule + ", listeClient=" + self.listeClient + "]"

        def getHashCode(self):
            return self.noTraverse

        def Equals(self, other):
            return self.noTraverse == other.noTraverse


        def calculerRevenueTraverse(self):
            revenue = 0
            for vehicule in self.listeVehicule:
                revenue += vehicule.calculerRevenueVehicule()
            return revenue

        def ajouterClient(self, client):
            self.listeClient.append(client)

        def supprimerClient(self, client):
            self.listeClient.remove(client)

        def ajouterVehicule(self, vehicule):
            self.listeVehicule.append(vehicule)

        def supprimerVehicule(self, vehicule):
            self.listeVehicule.remove(vehicule)