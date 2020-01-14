#importation des modules
from design.bizch import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from bd import lienBaseDeDonnee
import random


class main(QMainWindow):
    "classe principale"
    def __init__(self):
        super(main, self).__init__()
        self.ui = Ui_MainWindow()   
        self.ui.setupUi(self)

        #signal lors d'un clic sur un bouton
        self.ui.visualiser.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.accueil.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.inscrire.clicked.connect(self.inscription)
        self.ui.annuler.clicked.connect(self.annule)
        self.ui.sauver.clicked.connect(self.sauver)
        self.ui.modifier.clicked.connect(self.modifier)
        self.ui.table.clicked.connect(self.on_click)
        #self.ui.table.setStyleSheet("gridline-color: rgb(191, 191, 191)")
        #self.ui.table.resizeColumnsToContents()
        self.op=""
        self.initial()
        self.afficheTable()
        
    def initial(self):
        self.ui.modifier.setEnabled(False)
        self.ui.supprimer.setEnabled(False)
        self.ui.noms.setEnabled(False)
        self.ui.solde.setEnabled(False)
        self.ui.pseudo.setEnabled(False)
        self.ui.mp.setEnabled(False)
        self.ui.sauver.setEnabled(False)
        self.onlyInt = QIntValidator()
        self.ui.solde.setValidator(self.onlyInt)
        self.ui.solde.setMaxLength (4)
        self.insertBd = lienBaseDeDonnee()
        
    def annule(self):
        self.ui.inscrire.setEnabled(True)
        self.ui.modifier.setEnabled(False)
        self.ui.supprimer.setEnabled(False)
        self.ui.noms.setEnabled(False)
        self.ui.solde.setEnabled(False)
        self.ui.pseudo.setEnabled(False)
        self.ui.mp.setEnabled(False)
        self.ui.noms.setText("")
        self.ui.solde.setText("")
        self.ui.pseudo.setText("")
        self.ui.mp.setText("")
        self.ui.sauver.setEnabled(False)
        
    def active(self):
        self.ui.modifier.setEnabled(True)
        self.ui.supprimer.setEnabled(True)
        self.ui.inscrire.setEnabled(False)
        
    def inscription(self):
        self.op="ins"
        self.ui.noms.setEnabled(True)
        self.ui.solde.setEnabled(True)
        #self.ui.pseudo.setEnabled(True)
        #self.ui.mp.setEnabled(True)
        self.ui.sauver.setEnabled(True)
    def sauver(self):
        if self.op=="ins":
            self.noms=self.ui.noms.text()
            self.solde=self.ui.solde.text()
           
            if self.noms=="" or self.solde=="":
            
                QMessageBox.information(self,"info ereur","veillez renseignez des \n champs valide")
            else:
                
                pseudo,mp=self.genere()
                
                self.insertBd.insert("candidats",[self.noms,self.solde,pseudo,mp])
                QMessageBox.information(self,"info","Enregistrement effectuer\npseudo : "+pseudo+"\nmot de passe : "+mp)
                self.annule()
                self.afficheTable()
        elif self.op=="mo":
            print("mise a jour")
            noms=self.ui.noms.text()
            solde=self.ui.solde.text()
            pseudo=self.ui.pseudo.text()
            mp=self.ui.mp.text()
            #self.insertBd.update("candidats",[noms,solde,pseudo,mp])
        else:
            print("aucune aupeation en cour")
    def genere(self):
       
        pseudo=self.noms+str(random.randint(100,999))
       
        mp="biz"+str(random.randint(10,99))
        return [pseudo,mp]

    def afficheTable(self):
        res=self.insertBd.select("candidats")
        self.ui.table.setRowCount(len(res))
        for i in range(len(res)):
            for j in range(1,5):
                #print(i,j)
                self.ui.table.setItem(i,j-1, QTableWidgetItem(res[i][j]))
        #print(res)

    def on_click(self):
        print("\n")
        self.row = self.ui.table.currentRow()
        self.active()
        #print(self.ui.table.item(self.row, 0).text())
##        for currentQTableWidgetItem in self.ui.table.selectedItems():
##            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
            #print(self.ui.table.setSelectionBehavior(QAbstractItemView.SelectRows))

    def modifier(self):
        self.op="mo"
        self.ui.noms.setEnabled(True)
        self.ui.solde.setEnabled(True)
        self.ui.pseudo.setEnabled(True)
        self.ui.mp.setEnabled(True)
        self.ui.sauver.setEnabled(True)
        self.ui.noms.setText(self.ui.table.item(self.row, 0).text())
        self.ui.solde.setText(self.ui.table.item(self.row, 1).text())
        self.ui.pseudo.setText(self.ui.table.item(self.row, 2).text())
        self.ui.mp.setText(self.ui.table.item(self.row, 3).text())
        
if __name__ == "__main__":
    import sys,os
    app = QtWidgets.QApplication(sys.argv)
    ui = main()
    ui.show()     #lancement de l'application
    sys.exit(app.exec_())
