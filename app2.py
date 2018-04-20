# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 548)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.projectname = QtWidgets.QLabel(self.centralwidget)
        self.projectname.setGeometry(QtCore.QRect(100, 60, 361, 31))
        self.projectname.setObjectName("projectname")
        self.category = QtWidgets.QLabel(self.centralwidget)
        self.category.setGeometry(QtCore.QRect(90, 150, 131, 16))
        self.category.setObjectName("category")
        self.btnFindByCat = QtWidgets.QPushButton(self.centralwidget)
        self.btnFindByCat.setGeometry(QtCore.QRect(380, 160, 51, 31))
        self.btnFindByCat.setObjectName("btnFindByCat")
        self.searchword = QtWidgets.QTextEdit(self.centralwidget)
        self.searchword.setGeometry(QtCore.QRect(60, 320, 251, 31))
        self.searchword.setObjectName("searchword")
        self.selecategory = QtWidgets.QComboBox(self.centralwidget)
        self.selecategory.setGeometry(QtCore.QRect(90, 170, 141, 22))
        self.selecategory.setObjectName("selecategory")
        self.selecategory.addItem("")
        self.selecategory.addItem("")
        self.selecategory.addItem("")
        self.selecategory.addItem("")
        self.selecategory.addItem("")
        self.selecategory.addItem("")
        self.selecategory.addItem("")
        self.selecategory.addItem("")
        self.selecategory.addItem("")
        self.selecategory.addItem("")
        self.selecategory.addItem("")
        self.btnSearchByName = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearchByName.setGeometry(QtCore.QRect(380, 320, 75, 31))
        self.btnSearchByName.setObjectName("btnSearchByName")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 300, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 190, 71, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 230, 61, 31))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.projectname.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">BOOK DISCOUNT FINDER</span></p></body></html>"))
        self.category.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Choose a category</span></p></body></html>"))
        self.btnFindByCat.setText(_translate("MainWindow", "FIND"))
        self.searchword.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.selecategory.setItemText(0, _translate("MainWindow", "select a category"))
        self.selecategory.setItemText(1, _translate("MainWindow", "biographies and autobiographies"))
        self.selecategory.setItemText(2, _translate("MainWindow", "business strategies and management"))
        self.selecategory.setItemText(3, _translate("MainWindow", "crime, thriller and mystery"))
        self.selecategory.setItemText(4, _translate("MainWindow", "personal development and self help"))
        self.selecategory.setItemText(5, _translate("MainWindow", "fantasy"))
        self.selecategory.setItemText(6, _translate("MainWindow", "exam preparation"))
        self.selecategory.setItemText(7, _translate("MainWindow", "romance"))
        self.selecategory.setItemText(8, _translate("MainWindow", "historical fiction"))
        self.selecategory.setItemText(9, _translate("MainWindow", "children\'s book"))
        self.selecategory.setItemText(10, _translate("MainWindow", "art and photography"))
        self.btnSearchByName.setText(_translate("MainWindow", "Search"))
        self.label_2.setText(_translate("MainWindow", "searching...."))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Status</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

