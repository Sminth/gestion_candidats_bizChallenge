# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bizch.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 403)
        MainWindow.setMaximumSize(QtCore.QSize(698, 403))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/prefix1/Bible.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(9, -1, 681, 361))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(-4, 2, 691, 371))
        self.label.setStyleSheet("border-image: url(:/prefix1/image.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 291, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(90, 190, 201, 3))
        self.label_3.setStyleSheet("background-color: rgb(0, 116, 205);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(80, 210, 261, 31))
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.visualiser = QtWidgets.QPushButton(self.page)
        self.visualiser.setGeometry(QtCore.QRect(480, 120, 71, 71))
        self.visualiser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.visualiser.setStyleSheet("background:transparent")
        self.visualiser.setText("")
        self.visualiser.setObjectName("visualiser")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(-4, 2, 691, 361))
        self.label_5.setStyleSheet("background-color:rgb(0, 32, 79);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(0, 2, 151, 361))
        self.label_7.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.table = QtWidgets.QTableWidget(self.page_2)
        self.table.setGeometry(QtCore.QRect(150, 160, 531, 201))
        self.table.setStyleSheet("background:transparent;\n"
"border:1px solid #fff")
        self.table.setObjectName("table")
        self.table.setColumnCount(4)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        self.table.horizontalHeader().setDefaultSectionSize(130)
        self.noms = QtWidgets.QLineEdit(self.page_2)
        self.noms.setGeometry(QtCore.QRect(180, 40, 171, 31))
        self.noms.setStyleSheet("background:transparent;\n"
"border:1px solid #fff;\n"
"border-radius:20%;\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.noms.setClearButtonEnabled(True)
        self.noms.setObjectName("noms")
        self.pseudo = QtWidgets.QLineEdit(self.page_2)
        self.pseudo.setGeometry(QtCore.QRect(180, 100, 171, 31))
        self.pseudo.setStyleSheet("background:transparent;\n"
"border:1px solid #fff;\n"
"border-radius:20%;\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.pseudo.setClearButtonEnabled(True)
        self.pseudo.setObjectName("pseudo")
        self.solde = QtWidgets.QLineEdit(self.page_2)
        self.solde.setGeometry(QtCore.QRect(390, 40, 171, 31))
        self.solde.setStyleSheet("background:transparent;\n"
"border:1px solid #fff;\n"
"border-radius:20%;\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.solde.setClearButtonEnabled(True)
        self.solde.setObjectName("solde")
        self.mp = QtWidgets.QLineEdit(self.page_2)
        self.mp.setGeometry(QtCore.QRect(390, 100, 171, 31))
        self.mp.setStyleSheet("background:transparent;\n"
"border:1px solid #fff;\n"
"border-radius:20%;\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.mp.setClearButtonEnabled(True)
        self.mp.setObjectName("mp")
        self.inscrire = QtWidgets.QPushButton(self.page_2)
        self.inscrire.setGeometry(QtCore.QRect(10, 80, 131, 41))
        self.inscrire.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inscrire.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:3px solid rgb(255, 85, 0)")
        self.inscrire.setObjectName("inscrire")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(590, 60, 51, 51))
        self.label_8.setStyleSheet("\n"
"border:1px solid #fff;\n"
"border-radius:20%;\n"
"background-color: rgb(255, 85, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.sauver = QtWidgets.QPushButton(self.page_2)
        self.sauver.setGeometry(QtCore.QRect(590, 60, 51, 51))
        self.sauver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sauver.setStyleSheet("background:transparent")
        self.sauver.setText("")
        self.sauver.setObjectName("sauver")
        self.modifier = QtWidgets.QPushButton(self.page_2)
        self.modifier.setGeometry(QtCore.QRect(10, 160, 131, 41))
        self.modifier.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.modifier.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:3px solid rgb(255, 85, 0)")
        self.modifier.setObjectName("modifier")
        self.supprimer = QtWidgets.QPushButton(self.page_2)
        self.supprimer.setGeometry(QtCore.QRect(10, 240, 131, 41))
        self.supprimer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.supprimer.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:3px solid rgb(255, 85, 0)")
        self.supprimer.setObjectName("supprimer")
        self.accueil = QtWidgets.QPushButton(self.page_2)
        self.accueil.setGeometry(QtCore.QRect(10, 10, 131, 41))
        self.accueil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.accueil.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background:transparent;\n"
"border:none;\n"
"border:1px solid #fff;\n"
"color: rgb(255, 255, 255);")
        self.accueil.setObjectName("accueil")
        self.annuler = QtWidgets.QPushButton(self.page_2)
        self.annuler.setGeometry(QtCore.QRect(10, 310, 131, 41))
        self.annuler.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.annuler.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:3px solid rgb(255, 85, 0)")
        self.annuler.setObjectName("annuler")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 698, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "bizChallenge"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#ffffff;\">Biz Challenge</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">challengeons-nous vivant !</span></p></body></html>"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Noms"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Solde"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Pseudo"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Mot de passe"))
        self.noms.setPlaceholderText(_translate("MainWindow", "Noms"))
        self.pseudo.setPlaceholderText(_translate("MainWindow", "pseudo"))
        self.solde.setPlaceholderText(_translate("MainWindow", "solde"))
        self.mp.setPlaceholderText(_translate("MainWindow", "mot de passe"))
        self.inscrire.setText(_translate("MainWindow", "Inscrire"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">S</span></p></body></html>"))
        self.modifier.setText(_translate("MainWindow", "Modifier"))
        self.supprimer.setText(_translate("MainWindow", "Supprimer"))
        self.accueil.setText(_translate("MainWindow", "Biz Challenge"))
        self.annuler.setText(_translate("MainWindow", "Annuler"))
import im_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
