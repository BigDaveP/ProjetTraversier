# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Template.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1151, 772)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(20, 40, 1101, 711))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(20, 50, 151, 16))
        self.label_12.setObjectName("label_12")
        self.nomTraversier = QtWidgets.QLineEdit(self.tab_2)
        self.nomTraversier.setGeometry(QtCore.QRect(20, 70, 321, 20))
        self.nomTraversier.setObjectName("nomTraversier")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(20, 100, 151, 16))
        self.label_13.setObjectName("label_13")
        self.capaciteVehiculeTraversier = QtWidgets.QLineEdit(self.tab_2)
        self.capaciteVehiculeTraversier.setGeometry(QtCore.QRect(20, 120, 321, 20))
        self.capaciteVehiculeTraversier.setObjectName("capaciteVehiculeTraversier")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(20, 150, 161, 16))
        self.label_14.setObjectName("label_14")
        self.capacitePersonneTraversier = QtWidgets.QLineEdit(self.tab_2)
        self.capacitePersonneTraversier.setGeometry(QtCore.QRect(20, 170, 321, 20))
        self.capacitePersonneTraversier.setObjectName("capacitePersonneTraversier")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(20, 200, 161, 16))
        self.label_15.setObjectName("label_15")
        self.anneeFabricationTraversier = QtWidgets.QLineEdit(self.tab_2)
        self.anneeFabricationTraversier.setGeometry(QtCore.QRect(20, 220, 321, 20))
        self.anneeFabricationTraversier.setObjectName("anneeFabricationTraversier")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(20, 250, 161, 16))
        self.label_16.setObjectName("label_16")
        self.dateMiseServiceTraverse = QtWidgets.QLineEdit(self.tab_2)
        self.dateMiseServiceTraverse.setGeometry(QtCore.QRect(20, 270, 321, 20))
        self.dateMiseServiceTraverse.setObjectName("dateMiseServiceTraverse")
        self.listEmployeTraversier = QtWidgets.QListWidget(self.tab_2)
        self.listEmployeTraversier.setGeometry(QtCore.QRect(400, 60, 331, 571))
        self.listEmployeTraversier.setObjectName("listEmployeTraversier")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(400, 40, 111, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(750, 60, 151, 16))
        self.label_18.setObjectName("label_18")
        self.employeSelectionnerTraverse = QtWidgets.QLineEdit(self.tab_2)
        self.employeSelectionnerTraverse.setGeometry(QtCore.QRect(750, 80, 321, 20))
        self.employeSelectionnerTraverse.setObjectName("employeSelectionnerTraverse")
        self.btnSupprimerEmployer = QtWidgets.QPushButton(self.tab_2)
        self.btnSupprimerEmployer.setGeometry(QtCore.QRect(870, 120, 111, 41))
        self.btnSupprimerEmployer.setObjectName("btnSupprimerEmployer")
        self.btnModifierEmployer = QtWidgets.QPushButton(self.tab_2)
        self.btnModifierEmployer.setGeometry(QtCore.QRect(750, 120, 111, 41))
        self.btnModifierEmployer.setObjectName("btnModifierEmployer")
        self.btnAjouterEmployer = QtWidgets.QPushButton(self.tab_2)
        self.btnAjouterEmployer.setGeometry(QtCore.QRect(750, 210, 141, 51))
        self.btnAjouterEmployer.setObjectName("btnAjouterEmployer")
        self.btnAjouterTraversier = QtWidgets.QPushButton(self.tab_2)
        self.btnAjouterTraversier.setGeometry(QtCore.QRect(20, 310, 111, 41))
        self.btnAjouterTraversier.setObjectName("btnAjouterTraversier")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(550, 610, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 610, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.nomEmploye = QtWidgets.QLineEdit(self.tab)
        self.nomEmploye.setGeometry(QtCore.QRect(490, 100, 461, 21))
        self.nomEmploye.setObjectName("nomEmploye")
        self.listeEmploye = QtWidgets.QListWidget(self.tab)
        self.listeEmploye.setGeometry(QtCore.QRect(30, 80, 401, 571))
        self.listeEmploye.setObjectName("listeEmploye")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(490, 80, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(490, 130, 61, 16))
        self.label_2.setObjectName("label_2")
        self.adresseEmploye = QtWidgets.QLineEdit(self.tab)
        self.adresseEmploye.setGeometry(QtCore.QRect(490, 150, 461, 21))
        self.adresseEmploye.setObjectName("adresseEmploye")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(490, 180, 47, 13))
        self.label_3.setObjectName("label_3")
        self.villeEmploye = QtWidgets.QLineEdit(self.tab)
        self.villeEmploye.setGeometry(QtCore.QRect(490, 200, 461, 21))
        self.villeEmploye.setObjectName("villeEmploye")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(490, 230, 61, 16))
        self.label_4.setObjectName("label_4")
        self.provinceEmploye = QtWidgets.QLineEdit(self.tab)
        self.provinceEmploye.setGeometry(QtCore.QRect(490, 250, 461, 21))
        self.provinceEmploye.setObjectName("provinceEmploye")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(490, 280, 81, 16))
        self.label_5.setObjectName("label_5")
        self.codePostalEmploye = QtWidgets.QLineEdit(self.tab)
        self.codePostalEmploye.setGeometry(QtCore.QRect(490, 300, 461, 21))
        self.codePostalEmploye.setObjectName("codePostalEmploye")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(490, 340, 71, 16))
        self.label_6.setObjectName("label_6")
        self.telephoneEmploye = QtWidgets.QLineEdit(self.tab)
        self.telephoneEmploye.setGeometry(QtCore.QRect(490, 360, 461, 21))
        self.telephoneEmploye.setObjectName("telephoneEmploye")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(490, 400, 61, 16))
        self.label_7.setObjectName("label_7")
        self.courrielEmploye = QtWidgets.QLineEdit(self.tab)
        self.courrielEmploye.setGeometry(QtCore.QRect(490, 420, 461, 21))
        self.courrielEmploye.setObjectName("courrielEmploye")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(490, 450, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(30, 60, 171, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(490, 500, 101, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(490, 550, 81, 16))
        self.label_11.setObjectName("label_11")
        self.dateEmbaucheEmploye = QtWidgets.QDateEdit(self.tab)
        self.dateEmbaucheEmploye.setGeometry(QtCore.QRect(490, 520, 110, 22))
        self.dateEmbaucheEmploye.setObjectName("dateEmbaucheEmploye")
        self.dateArretEmploye = QtWidgets.QDateEdit(self.tab)
        self.dateArretEmploye.setGeometry(QtCore.QRect(490, 570, 110, 22))
        self.dateArretEmploye.setObjectName("dateArretEmploye")
        self.label_37 = QtWidgets.QLabel(self.tab)
        self.label_37.setGeometry(QtCore.QRect(490, 30, 101, 16))
        self.label_37.setObjectName("label_37")
        self.numEmploye = QtWidgets.QLineEdit(self.tab)
        self.numEmploye.setGeometry(QtCore.QRect(490, 50, 461, 21))
        self.numEmploye.setObjectName("numEmploye")
        self.nasEmploye = QtWidgets.QLineEdit(self.tab)
        self.nasEmploye.setGeometry(QtCore.QRect(490, 470, 461, 21))
        self.nasEmploye.setObjectName("nasEmploye")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.villeDepartTraverse = QtWidgets.QLineEdit(self.tab_3)
        self.villeDepartTraverse.setGeometry(QtCore.QRect(30, 150, 221, 21))
        self.villeDepartTraverse.setObjectName("villeDepartTraverse")
        self.label_20 = QtWidgets.QLabel(self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(30, 80, 47, 13))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(30, 180, 201, 16))
        self.label_21.setObjectName("label_21")
        self.label_38 = QtWidgets.QLabel(self.tab_3)
        self.label_38.setGeometry(QtCore.QRect(30, 30, 131, 16))
        self.label_38.setObjectName("label_38")
        self.label_24 = QtWidgets.QLabel(self.tab_3)
        self.label_24.setGeometry(QtCore.QRect(30, 130, 101, 16))
        self.label_24.setObjectName("label_24")
        self.numTraverse = QtWidgets.QLineEdit(self.tab_3)
        self.numTraverse.setGeometry(QtCore.QRect(30, 50, 221, 21))
        self.numTraverse.setObjectName("numTraverse")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 250, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.dateTraverse = QtWidgets.QDateTimeEdit(self.tab_3)
        self.dateTraverse.setGeometry(QtCore.QRect(30, 100, 221, 22))
        self.dateTraverse.setObjectName("dateTraverse")
        self.listVehiculeTraverse = QtWidgets.QListWidget(self.tab_3)
        self.listVehiculeTraverse.setGeometry(QtCore.QRect(330, 50, 301, 431))
        self.listVehiculeTraverse.setObjectName("listVehiculeTraverse")
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(330, 30, 141, 16))
        self.label_19.setObjectName("label_19")
        self.listClientTraverse = QtWidgets.QListWidget(self.tab_3)
        self.listClientTraverse.setGeometry(QtCore.QRect(680, 50, 301, 431))
        self.listClientTraverse.setObjectName("listClientTraverse")
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(680, 30, 141, 16))
        self.label_22.setObjectName("label_22")
        self.clientVehicule = QtWidgets.QLineEdit(self.tab_3)
        self.clientVehicule.setGeometry(QtCore.QRect(330, 510, 221, 21))
        self.clientVehicule.setReadOnly(True)
        self.clientVehicule.setObjectName("clientVehicule")
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setGeometry(QtCore.QRect(330, 490, 201, 16))
        self.label_23.setObjectName("label_23")
        self.numIdentificationVehiculeTraverse = QtWidgets.QLineEdit(self.tab_3)
        self.numIdentificationVehiculeTraverse.setGeometry(QtCore.QRect(330, 560, 221, 21))
        self.numIdentificationVehiculeTraverse.setReadOnly(True)
        self.numIdentificationVehiculeTraverse.setObjectName("numIdentificationVehiculeTraverse")
        self.label_25 = QtWidgets.QLabel(self.tab_3)
        self.label_25.setGeometry(QtCore.QRect(330, 540, 201, 16))
        self.label_25.setObjectName("label_25")
        self.typeVehiculeTraverse = QtWidgets.QLineEdit(self.tab_3)
        self.typeVehiculeTraverse.setGeometry(QtCore.QRect(330, 610, 221, 21))
        self.typeVehiculeTraverse.setReadOnly(True)
        self.typeVehiculeTraverse.setObjectName("typeVehiculeTraverse")
        self.label_26 = QtWidgets.QLabel(self.tab_3)
        self.label_26.setGeometry(QtCore.QRect(330, 590, 201, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_3)
        self.label_27.setGeometry(QtCore.QRect(330, 640, 201, 16))
        self.label_27.setObjectName("label_27")
        self.prixVehiculeTraverse = QtWidgets.QLineEdit(self.tab_3)
        self.prixVehiculeTraverse.setGeometry(QtCore.QRect(330, 660, 221, 21))
        self.prixVehiculeTraverse.setReadOnly(True)
        self.prixVehiculeTraverse.setObjectName("prixVehiculeTraverse")
        self.employeInscptionTraverse = QtWidgets.QComboBox(self.tab_3)
        self.employeInscptionTraverse.setGeometry(QtCore.QRect(30, 200, 221, 22))
        self.employeInscptionTraverse.setObjectName("employeInscptionTraverse")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.listClients = QtWidgets.QListWidget(self.tab_4)
        self.listClients.setGeometry(QtCore.QRect(30, 50, 361, 571))
        self.listClients.setObjectName("listClients")
        self.label_28 = QtWidgets.QLabel(self.tab_4)
        self.label_28.setGeometry(QtCore.QRect(30, 30, 171, 16))
        self.label_28.setObjectName("label_28")
        self.label_61 = QtWidgets.QLabel(self.tab_4)
        self.label_61.setGeometry(QtCore.QRect(430, 300, 81, 16))
        self.label_61.setObjectName("label_61")
        self.nomClient = QtWidgets.QLineEdit(self.tab_4)
        self.nomClient.setGeometry(QtCore.QRect(430, 120, 261, 21))
        self.nomClient.setObjectName("nomClient")
        self.adresseClient = QtWidgets.QLineEdit(self.tab_4)
        self.adresseClient.setGeometry(QtCore.QRect(430, 170, 261, 21))
        self.adresseClient.setObjectName("adresseClient")
        self.provinceClient = QtWidgets.QLineEdit(self.tab_4)
        self.provinceClient.setGeometry(QtCore.QRect(430, 270, 261, 21))
        self.provinceClient.setObjectName("provinceClient")
        self.label_62 = QtWidgets.QLabel(self.tab_4)
        self.label_62.setGeometry(QtCore.QRect(430, 100, 47, 13))
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self.tab_4)
        self.label_63.setGeometry(QtCore.QRect(430, 200, 47, 13))
        self.label_63.setObjectName("label_63")
        self.telephoneClient = QtWidgets.QLineEdit(self.tab_4)
        self.telephoneClient.setGeometry(QtCore.QRect(430, 370, 261, 21))
        self.telephoneClient.setObjectName("telephoneClient")
        self.codePostalClient = QtWidgets.QLineEdit(self.tab_4)
        self.codePostalClient.setGeometry(QtCore.QRect(430, 320, 261, 21))
        self.codePostalClient.setObjectName("codePostalClient")
        self.label_64 = QtWidgets.QLabel(self.tab_4)
        self.label_64.setGeometry(QtCore.QRect(430, 400, 61, 16))
        self.label_64.setObjectName("label_64")
        self.label_65 = QtWidgets.QLabel(self.tab_4)
        self.label_65.setGeometry(QtCore.QRect(430, 50, 131, 16))
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.tab_4)
        self.label_66.setGeometry(QtCore.QRect(430, 150, 61, 16))
        self.label_66.setObjectName("label_66")
        self.villeClient = QtWidgets.QLineEdit(self.tab_4)
        self.villeClient.setGeometry(QtCore.QRect(430, 220, 261, 21))
        self.villeClient.setObjectName("villeClient")
        self.label_67 = QtWidgets.QLabel(self.tab_4)
        self.label_67.setGeometry(QtCore.QRect(430, 250, 61, 16))
        self.label_67.setObjectName("label_67")
        self.numClient = QtWidgets.QLineEdit(self.tab_4)
        self.numClient.setGeometry(QtCore.QRect(430, 70, 261, 21))
        self.numClient.setObjectName("numClient")
        self.label_68 = QtWidgets.QLabel(self.tab_4)
        self.label_68.setGeometry(QtCore.QRect(430, 350, 71, 16))
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.tab_4)
        self.label_69.setGeometry(QtCore.QRect(430, 450, 47, 13))
        self.label_69.setObjectName("label_69")
        self.courrielClient = QtWidgets.QLineEdit(self.tab_4)
        self.courrielClient.setGeometry(QtCore.QRect(430, 420, 261, 21))
        self.courrielClient.setObjectName("courrielClient")
        self.label_70 = QtWidgets.QLabel(self.tab_4)
        self.label_70.setGeometry(QtCore.QRect(760, 50, 111, 16))
        self.label_70.setObjectName("label_70")
        self.vehiculeOui = QtWidgets.QRadioButton(self.tab_4)
        self.vehiculeOui.setGeometry(QtCore.QRect(760, 70, 82, 17))
        self.vehiculeOui.setObjectName("vehiculeOui")
        self.vehiculeNon = QtWidgets.QRadioButton(self.tab_4)
        self.vehiculeNon.setGeometry(QtCore.QRect(810, 70, 82, 17))
        self.vehiculeNon.setObjectName("vehiculeNon")
        self.numVehicule = QtWidgets.QLineEdit(self.tab_4)
        self.numVehicule.setGeometry(QtCore.QRect(760, 120, 261, 21))
        self.numVehicule.setObjectName("numVehicule")
        self.label_71 = QtWidgets.QLabel(self.tab_4)
        self.label_71.setGeometry(QtCore.QRect(760, 100, 151, 16))
        self.label_71.setObjectName("label_71")
        self.label_72 = QtWidgets.QLabel(self.tab_4)
        self.label_72.setGeometry(QtCore.QRect(760, 150, 151, 16))
        self.label_72.setObjectName("label_72")
        self.marqueVehicule = QtWidgets.QLineEdit(self.tab_4)
        self.marqueVehicule.setGeometry(QtCore.QRect(760, 170, 261, 21))
        self.marqueVehicule.setObjectName("marqueVehicule")
        self.label_73 = QtWidgets.QLabel(self.tab_4)
        self.label_73.setGeometry(QtCore.QRect(760, 200, 151, 16))
        self.label_73.setObjectName("label_73")
        self.modeleVehicule = QtWidgets.QLineEdit(self.tab_4)
        self.modeleVehicule.setGeometry(QtCore.QRect(760, 220, 261, 21))
        self.modeleVehicule.setObjectName("modeleVehicule")
        self.label_74 = QtWidgets.QLabel(self.tab_4)
        self.label_74.setGeometry(QtCore.QRect(760, 250, 151, 16))
        self.label_74.setObjectName("label_74")
        self.couleurVehicule = QtWidgets.QLineEdit(self.tab_4)
        self.couleurVehicule.setGeometry(QtCore.QRect(760, 270, 261, 21))
        self.couleurVehicule.setObjectName("couleurVehicule")
        self.label_75 = QtWidgets.QLabel(self.tab_4)
        self.label_75.setGeometry(QtCore.QRect(760, 300, 151, 16))
        self.label_75.setObjectName("label_75")
        self.anneeVehicule = QtWidgets.QLineEdit(self.tab_4)
        self.anneeVehicule.setGeometry(QtCore.QRect(760, 320, 261, 21))
        self.anneeVehicule.setObjectName("anneeVehicule")
        self.immatriculationVehicule = QtWidgets.QLineEdit(self.tab_4)
        self.immatriculationVehicule.setGeometry(QtCore.QRect(760, 370, 261, 21))
        self.immatriculationVehicule.setObjectName("immatriculationVehicule")
        self.label_76 = QtWidgets.QLabel(self.tab_4)
        self.label_76.setGeometry(QtCore.QRect(760, 350, 151, 16))
        self.label_76.setObjectName("label_76")
        self.label_123 = QtWidgets.QLabel(self.tab_4)
        self.label_123.setGeometry(QtCore.QRect(760, 400, 151, 16))
        self.label_123.setObjectName("label_123")
        self.typeVehicule = QtWidgets.QComboBox(self.tab_4)
        self.typeVehicule.setGeometry(QtCore.QRect(760, 420, 261, 22))
        self.typeVehicule.setObjectName("typeVehicule")
        self.dateNaissanceClient = QtWidgets.QLineEdit(self.tab_4)
        self.dateNaissanceClient.setGeometry(QtCore.QRect(430, 520, 261, 21))
        self.dateNaissanceClient.setText("")
        self.dateNaissanceClient.setObjectName("dateNaissanceClient")
        self.label_124 = QtWidgets.QLabel(self.tab_4)
        self.label_124.setGeometry(QtCore.QRect(430, 500, 111, 16))
        self.label_124.setObjectName("label_124")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_2.setGeometry(QtCore.QRect(430, 470, 261, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.tabWidget.addTab(self.tab_4, "")
        self.sauvegarder = QtWidgets.QPushButton(Form)
        self.sauvegarder.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.sauvegarder.setObjectName("sauvegarder")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_12.setText(_translate("Form", "Nom :"))
        self.label_13.setText(_translate("Form", "Capacité maximal de véhicule :"))
        self.label_14.setText(_translate("Form", "Capacité maxilmal de personne : "))
        self.label_15.setText(_translate("Form", "Année de fabrication : "))
        self.label_16.setText(_translate("Form", "Date de mise en service :"))
        self.label_17.setText(_translate("Form", "Liste d\'employé"))
        self.label_18.setText(_translate("Form", "Employé selectionné :"))
        self.btnSupprimerEmployer.setText(_translate("Form", "Supprimer"))
        self.btnModifierEmployer.setText(_translate("Form", "Modifier"))
        self.btnAjouterEmployer.setText(_translate("Form", "Ajouter un employé "))
        self.btnAjouterTraversier.setText(_translate("Form", "Ajouter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Traversier"))
        self.pushButton.setText(_translate("Form", "Ajouter"))
        self.pushButton_2.setText(_translate("Form", "Supprimer"))
        self.label.setText(_translate("Form", "Nom :"))
        self.label_2.setText(_translate("Form", "Adresse :"))
        self.label_3.setText(_translate("Form", "Ville :"))
        self.label_4.setText(_translate("Form", "Province : "))
        self.label_5.setText(_translate("Form", "Code Postal"))
        self.label_6.setText(_translate("Form", "Telephone : "))
        self.label_7.setText(_translate("Form", "Courriel :"))
        self.label_8.setText(_translate("Form", "NAS : "))
        self.label_9.setText(_translate("Form", "Liste d\'employé(s)"))
        self.label_10.setText(_translate("Form", "Date d\'embauche"))
        self.label_11.setText(_translate("Form", "Date d\'arrêt"))
        self.label_37.setText(_translate("Form", "Numéro employé :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Employer"))
        self.label_20.setText(_translate("Form", "Date :"))
        self.label_21.setText(_translate("Form", "Employé qui s\'occupe de l\'inscription : "))
        self.label_38.setText(_translate("Form", "Numéro de la traverse :"))
        self.label_24.setText(_translate("Form", "Ville de départ :"))
        self.pushButton_3.setText(_translate("Form", "Ajouter"))
        self.label_19.setText(_translate("Form", "Liste des véhicules :"))
        self.label_22.setText(_translate("Form", "Liste des clients :"))
        self.label_23.setText(_translate("Form", "Client propriétaire du véhicule : "))
        self.label_25.setText(_translate("Form", "Numéro d\'identification : "))
        self.label_26.setText(_translate("Form", "Type de véhicule : "))
        self.label_27.setText(_translate("Form", "Prix de la traverse : "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Traverse"))
        self.label_28.setText(_translate("Form", "Liste des clients"))
        self.label_61.setText(_translate("Form", "Code Postal"))
        self.label_62.setText(_translate("Form", "Nom :"))
        self.label_63.setText(_translate("Form", "Ville :"))
        self.label_64.setText(_translate("Form", "Courriel :"))
        self.label_65.setText(_translate("Form", "Numéro d\'identification :"))
        self.label_66.setText(_translate("Form", "Adresse :"))
        self.label_67.setText(_translate("Form", "Province : "))
        self.label_68.setText(_translate("Form", "Telephone : "))
        self.label_69.setText(_translate("Form", "Sexe : "))
        self.label_70.setText(_translate("Form", "Avec un véhicule ? :"))
        self.vehiculeOui.setText(_translate("Form", "Oui"))
        self.vehiculeNon.setText(_translate("Form", "Non"))
        self.label_71.setText(_translate("Form", "Numéro d\'identification : "))
        self.label_72.setText(_translate("Form", "Marque : "))
        self.label_73.setText(_translate("Form", "Modèle : "))
        self.label_74.setText(_translate("Form", "Couleur : "))
        self.label_75.setText(_translate("Form", "Année : "))
        self.label_76.setText(_translate("Form", "Immatriculation :"))
        self.label_123.setText(_translate("Form", "Type de véhicule : "))
        self.label_124.setText(_translate("Form", "Date de naissance : "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Client"))
        self.sauvegarder.setText(_translate("Form", "Sauvegarder"))
