from datetime import date

from template import Ui_Form
from PyQt5 import QtWidgets
import sys
from Models.employe import Employe
from Models.traversier import Traversier
from Models.client import Client
from Models.traverse import Traverse
from Models.vehicule import Vehicule
import xml.etree.ElementTree as ET


class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    unTraversier = Traversier("", "", "", "", "", [])
    unEmploye = Employe("", "", "", "", "", "", "", "", "", "", "")
    unClient = Client("", "", "", "", "", "", "", "", "", "", "")
    uneTraverse = Traverse("", "", "", "", [], [])
    unVehicule = Vehicule("", "", "", "", "", "", "")

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        ### Initialisation de l'application ###

        try:
            tree = ET.parse('traversier.xml')
            root = tree.getroot()

            if root.find('noTraverse') is not None and root.find('date') is not None and root.find(
                    'villeDepart') is not None and root.find('employeInscription') is not None:
                self.uneTraverse = Traverse(root.find('noTraverse').text, root.find('date').text,
                                            root.find('villeDepart').text, root.find('employeInscription').text, [], [])

            if root.find('nomTraversier') is not None and root.find('capaciteVehicule') is not None and root.find(
                    'capacitePersonne') is not None and root.find('anneeFabrication') is not None and root.find(
                    'dateMiseService') is not None:
                self.unTraversier = Traversier(root.find('nom').text, root.find('capaciteVehicule').text,
                                               root.find('capacitePersonne').text, root.find('anneeFabrication').text,
                                               root.find('dateMiseService').text, [])

            # on ajoute les employés du traversier
            listWidget1 = self.listeEmploye
            listWidget2 = self.listEmployeTraversier
            for employe in root.findall('.//employe'):
                self.unEmploye = Employe(employe.find('noEmployer').text, employe.find('nAS').text,
                                         employe.find('dateEmbauche').text, employe.find('dateArret').text,
                                         employe.find('nom').text, employe.find('adresse').text,
                                         employe.find('ville').text, employe.find('province').text,
                                         employe.find('codePostal').text, employe.find('telephone').text,
                                         employe.find('courriel').text)
                self.unTraversier.ajouterEmploye(self.unEmploye)
                listWidget1.addItem(self.unEmploye.nom)
                listWidget2.addItem(self.unEmploye.nom)
                self.employeInscptionTraverse.addItem(self.unEmploye.nom)

            self.numTraverse.setText(self.uneTraverse.noTraverse)
            self.dateTraverse.setDate(date(int(self.uneTraverse.dateHeure[0:4]), int(self.uneTraverse.dateHeure[5:7]),
                                           int(self.uneTraverse.dateHeure[8:10])))
            self.villeDepartTraverse.setText(self.uneTraverse.villeDepart)
            self.employeInscptionTraverse.setCurrentText(self.uneTraverse.employeInscription)

            self.nomTraversier.setText(self.unTraversier.nom)
            self.capaciteVehiculeTraversier.setText(self.unTraversier.capaciteVehicule)
            self.capacitePersonneTraversier.setText(self.unTraversier.capacitePersonne)
            self.anneeFabricationTraversier.setText(self.unTraversier.anneeFabrication)
            self.dateMiseServiceTraverse.setText(self.unTraversier.dateMiseService)
        except:
            print("Erreur lors de la lecture du fichier traversier.xml")


        ### Actions de l'application ###

        self.pushButton.clicked.connect(self.addEmployee)
        self.btnAjouterTraversier.clicked.connect(self.addTraversier)
        self.btnAjouterEmployer.clicked.connect(self.addEmployee)
        self.sauvegarder.clicked.connect(self.save)
        self.btnAjouterEmployer.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))
        self.vehiculeOui.clicked.connect(self.enableInput)
        self.vehiculeNon.clicked.connect(self.disableInput)
        self.btnAjouterClient.clicked.connect(self.addClient)
        self.btnAjouterTraverse.clicked.connect(self.addTraverse)

    def addTraversier(self):
        if self.unTraversier.listeEmploye:
            print("Ce traversier contient des employés")
        else:
            self.unTraversier = Traversier(self.nomTraversier.text(), self.capaciteVehiculeTraversier.text(),
                                           self.capacitePersonneTraversier.text(),
                                           self.anneeFabricationTraversier.text(),
                                           self.anneeFabricationTraversier.text(), [])

    def addEmployee(self):
        self.unEmploye = Employe(self.numEmploye.text(), self.nasEmploye.text(), self.dateEmbaucheEmploye.text(),
                                 self.dateArretEmploye.text(), self.nomEmploye.text(), self.adresseEmploye.text(),
                                 self.villeEmploye.text(), self.provinceEmploye.text(), self.codePostalEmploye.text(),
                                 self.telephoneEmploye.text(), self.courrielEmploye.text())
        self.unTraversier.ajouterEmploye(self.unEmploye)
        listWidget1 = self.listeEmploye
        listWidget1.addItem(self.unEmploye.nom)
        listWidget2 = self.listEmployeTraversier
        listWidget2.addItem(self.unEmploye.nom)
        self.employeInscptionTraverse.addItem(self.unEmploye.nom)

    def addClient(self):
        if self.vehiculeOui.isChecked():
            self.unVehicule = Vehicule(self.numVehicule.text(), self.marqueVehicule.text(),
                                       self.modeleVehicule.text(), self.couleurVehicule.text(),
                                       self.anneeVehicule.text(), self.immatriculationVehicule.text(),
                                       self.typeVehicule.currentText())
            self.unClient = Client(self.numClient.text(), self.nomClient.text(), self.adresseClient.text(),
                                   self.villeClient.text(), self.provinceClient.text(), self.codePostalClient.text(),
                                   self.telephoneClient.text(), self.courrielClient.text(),
                                   self.sexeClient.currentText(),
                                   self.dateNaissanceClient.text(), self.unVehicule)
            self.uneTraverse.ajouterClient(self.unClient)
            self.uneTraverse.ajouterVehicule(self.unVehicule)
            listWidget3 = self.listClients
            listWidget3.addItem(self.unClient.nom)
            listWidget4 = self.listClientTraverse
            listWidget4.addItem(self.unClient.nom)
            listWidget5 = self.listVehiculeTraverse
            listWidget5.addItem(self.unVehicule.immatriculation)

        elif self.vehiculeNon.isChecked():
            self.unClient = Client(self.numClient.text(), self.nomClient.text(), self.adresseClient.text(),
                                   self.villeClient.text(), self.provinceClient.text(), self.codePostalClient.text(),
                                   self.telephoneClient.text(), self.courrielClient.text(),
                                   self.sexeClient.currentText(),
                                   self.dateNaissanceClient.text(), None)
            self.uneTraverse.ajouterClient(self.unClient)
            listWidget3 = self.listClients
            listWidget3.addItem(self.unClient.nom)
            listWidget4 = self.listClientTraverse
            listWidget4.addItem(self.unClient.nom)

    def addTraverse(self):
        self.uneTraverse = Traverse(self.numTraverse.text(), self.dateTraverse.text(),
                                    self.villeDepartTraverse.text(), self.employeInscptionTraverse.currentText(),
                                    [], [])

    def enableInput(self):
        self.numVehicule.setEnabled(True)
        self.marqueVehicule.setEnabled(True)
        self.modeleVehicule.setEnabled(True)
        self.couleurVehicule.setEnabled(True)
        self.anneeVehicule.setEnabled(True)
        self.immatriculationVehicule.setEnabled(True)
        self.typeVehicule.setEnabled(True)

    def disableInput(self):
        self.numVehicule.setEnabled(False)
        self.marqueVehicule.setEnabled(False)
        self.modeleVehicule.setEnabled(False)
        self.couleurVehicule.setEnabled(False)
        self.anneeVehicule.setEnabled(False)
        self.immatriculationVehicule.setEnabled(False)
        self.typeVehicule.setEnabled(False)

    def save(self):
        root = ET.Element("Traverse")
        tree = ET.ElementTree(root)
        noTraverse = ET.SubElement(root, "noTraverse")
        noTraverse.text = self.uneTraverse.noTraverse
        date = ET.SubElement(root, "date")
        date.text = self.uneTraverse.dateHeure
        villeDepart = ET.SubElement(root, "villeDepart")
        villeDepart.text = self.uneTraverse.villeDepart
        employeInscription = ET.SubElement(root, "employeInscription")
        employeInscription.text = self.uneTraverse.employeInscription
        nomTraversier = ET.SubElement(root, "nomTraversier")
        nomTraversier.text = self.unTraversier.nom
        capaciteVehicule = ET.SubElement(root, "capaciteVehicule")
        capaciteVehicule.text = self.unTraversier.capaciteVehicule
        capacitePersonne = ET.SubElement(root, "capacitePersonne")
        capacitePersonne.text = self.unTraversier.capacitePersonne
        anneeFabrication = ET.SubElement(root, "anneeFabrication")
        anneeFabrication.text = self.unTraversier.anneeFabrication
        dateMiseEnService = ET.SubElement(root, "dateMiseEnService")
        dateMiseEnService.text = self.unTraversier.dateMiseService
        listeEmploye = ET.SubElement(root, "listeEmploye")
        for e in self.unTraversier.listeEmploye:
            employe = ET.SubElement(listeEmploye, "employe")
            noEmployer = ET.SubElement(employe, "noEmployer")
            noEmployer.text = e.noEmployer
            nAS = ET.SubElement(employe, "nAS")
            nAS.text = e.nAS
            dateEmbauche = ET.SubElement(employe, "dateEmbauche")
            dateEmbauche.text = e.dateEmbauche
            dateArret = ET.SubElement(employe, "dateArret")
            dateArret.text = e.dateArret
            nom = ET.SubElement(employe, "nom")
            nom.text = e.nom
            adresse = ET.SubElement(employe, "adresse")
            adresse.text = e.adresse
            ville = ET.SubElement(employe, "ville")
            ville.text = e.ville
            province = ET.SubElement(employe, "province")
            province.text = e.province
            codePostal = ET.SubElement(employe, "codePostal")
            codePostal.text = e.codePostal
            telephone = ET.SubElement(employe, "telephone")
            telephone.text = e.telephone
            courriel = ET.SubElement(employe, "courriel")
            courriel.text = e.courriel

        ET.indent(root, space="    ")
        tree.write("traversier.xml")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
