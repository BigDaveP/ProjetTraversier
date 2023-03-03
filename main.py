from template import Ui_Form
from PyQt5 import QtWidgets
import sys
from Models.employe import Employe
from Models.traversier import Traversier
import xml.etree.ElementTree as ET
import xml.dom.minidom

unTraversier = Traversier("Traversier1", 100, 100, 2000, 2000, [])
class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.addEmployee)
        self.btnAjouterTraversier.clicked.connect(self.addTraversier)
        self.btnAjouterEmployer.clicked.connect(self.addEmployee)


    def addTraversier(self):
        unTraversier = Traversier(self.nomTraversier.text(), self.capaciteVehiculeTraversier.text(), self.capacitePersonneTraversier.text(), self.anneeFabricationTraversier.text(), self.anneeFabricationTraversier.text(), [])


    def addEmployee(self):
        unEmploye = Employe(self.numEmploye.text(), self.nasEmploye, self.dateEmbaucheEmploye, self.dateArretEmploye ,self.nomEmploye.text(), self.adresseEmploye.text(), self.villeEmploye.text(), self.provinceEmploye.text(), self.codePostalEmploye.text(), self.telephoneEmploye.text(), self.courrielEmploye.text())
        unTraversier.ajouterEmploye(unEmploye)
        listWidget1 = self.listeEmploye
        listWidget1.addItem(unEmploye.nom)
        listWidget2 = self.listEmployeTraversier
        listWidget2.addItem(unEmploye.nom)

    def save(self):
        root = ET.Element("traversier")
        nom = ET.SubElement(root, "nom")
        nom.text = self.nomTraversier.text()
        capaciteVehicule = ET.SubElement(root, "capaciteVehicule")
        capaciteVehicule.text = self.capaciteVehiculeTraversier.text()
        capacitePersonne = ET.SubElement(root, "capacitePersonne")
        capacitePersonne.text = self.capacitePersonneTraversier.text()
        anneeFabrication = ET.SubElement(root, "anneeFabrication")
        anneeFabrication.text = self.anneeFabricationTraversier.text()
        dateMiseService = ET.SubElement(root, "dateMiseService")
        dateMiseService.text = self.dateMiseServiceTraverse.text()
        employe = ET.SubElement(root, "employe")
        for item in self.listEmployeTraversier:
            nom = ET.SubElement(employe, "nom")
            nom.text = item.text()
        tree = ET.ElementTree(root)
        ET.indent(tree, space="    ")
        tree.write("traversier.xml")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())