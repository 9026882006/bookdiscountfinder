from PyQt5 import QtCore, QtGui, QtWidgets
import amazon_mining
from get_book_urls import fetch

from get_book_details import get_details_for_book


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 548)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.projectname = QtWidgets.QLabel(self.centralwidget)
        self.projectname.setGeometry(QtCore.QRect(100, 30, 361, 31))
        self.projectname.setObjectName("projectname")
        self.category = QtWidgets.QLabel(self.centralwidget)
        self.category.setGeometry(QtCore.QRect(100, 120, 131, 16))
        self.category.setObjectName("category")
        self.btnFindByCat = QtWidgets.QPushButton(self.centralwidget)
        self.btnFindByCat.setGeometry(QtCore.QRect(380, 130, 51, 31))
        self.btnFindByCat.setObjectName("btnFindByCat")
        self.option = QtWidgets.QLabel(self.centralwidget)
        self.option.setGeometry(QtCore.QRect(100, 210, 111, 20))
        self.option.setObjectName("option")
        self.btnFindByOpt = QtWidgets.QPushButton(self.centralwidget)
        self.btnFindByOpt.setGeometry(QtCore.QRect(380, 230, 51, 31))
        self.btnFindByOpt.setObjectName("btnFindByOpt")
        self.searchword = QtWidgets.QTextEdit(self.centralwidget)
        self.searchword.setGeometry(QtCore.QRect(50, 410, 251, 31))
        self.searchword.setObjectName("searchword")
        self.selecategory = QtWidgets.QComboBox(self.centralwidget)
        self.selecategory.setGeometry(QtCore.QRect(100, 140, 141, 22))
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
        self.selecategory.addItem("")
        self.selectoption = QtWidgets.QComboBox(self.centralwidget)
        self.selectoption.setGeometry(QtCore.QRect(100, 230, 141, 22))
        self.selectoption.setObjectName("selectoption")
        self.selectoption.addItem("")
        self.selectoption.addItem("")
        self.selectoption.addItem("")
        self.selectoption.addItem("")
        self.selectoption.addItem("")
        self.btnSearchByName = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearchByName.setGeometry(QtCore.QRect(380, 410, 75, 31))
        self.btnSearchByName.setObjectName("btnSearchByName")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 310, 101, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 330, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.btnFindByUrl = QtWidgets.QPushButton(self.centralwidget)
        self.btnFindByUrl.setGeometry(QtCore.QRect(380, 320, 51, 31))
        self.btnFindByUrl.setObjectName("btnFindByUrl")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 390, 61, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btnFindByCat.clicked.connect(self.find_by_category)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def find_by_category(self):
        text = str(self.selecategory.currentText())
        text = "_".join(text.split())
        url = amazon_mining.categories[text]
        results = fetch(url,self.headers)
        print(results)
        if not isinstance(results, str):
            book_list = []
            for book_url in results:
                print(book_url)
                bookDetails = get_details_for_book(book_url,self.headers)
                book_list.append(bookDetails)
                # send url and collect data
            print("finished")
            print(book_list)

    def find_by_option(self):
        text = str(self.selectoption.currentText())
        text = "_".join(text.split())
        print(text)
        url = amazon_mining.populars[text]
        print(url)

    def find_by_url(self):
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.projectname.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">BOOK DISCOUNT FINDER</span></p></body></html>"))
        self.category.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Choose a category</span></p></body></html>"))
        self.btnFindByCat.setText(_translate("MainWindow", "FIND"))
        self.option.setText(_translate("MainWindow",
                                       "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Choose a option</span></p></body></html>"))
        self.btnFindByOpt.setText(_translate("MainWindow", "FIND"))
        self.searchword.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.selecategory.setItemText(0, _translate("MainWindow", "select a category"))
        self.selecategory.setItemText(1, _translate("MainWindow", "arts and photography"))
        self.selecategory.setItemText(2, _translate("MainWindow", "biographies and memories"))
        self.selecategory.setItemText(3, _translate("MainWindow", "business and investing"))
        self.selecategory.setItemText(4, _translate("MainWindow", "children book"))
        self.selecategory.setItemText(5, _translate("MainWindow", "cookbooks food and wine"))
        self.selecategory.setItemText(6, _translate("MainWindow", "history"))
        self.selecategory.setItemText(7, _translate("MainWindow", "literature and fiction"))
        self.selecategory.setItemText(8, _translate("MainWindow", "mystery and suspense"))
        self.selecategory.setItemText(9, _translate("MainWindow", "romance"))
        self.selecategory.setItemText(10, _translate("MainWindow", "sci-fi and fantasy"))
        self.selecategory.setItemText(11, _translate("MainWindow", "teen and young adult books"))
        self.selectoption.setItemText(0, _translate("MainWindow", "select an option"))
        self.selectoption.setItemText(1, _translate("MainWindow", "Popular books"))
        self.selectoption.setItemText(2, _translate("MainWindow", "top20 books"))
        self.selectoption.setItemText(3, _translate("MainWindow", "best books of the month"))
        self.selectoption.setItemText(4, _translate("MainWindow", "award winners"))
        self.btnSearchByName.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Choose the URL</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "select the url"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Amazon"))
        self.comboBox.setItemText(2, _translate("MainWindow", "snapdeal"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Good reads"))
        self.comboBox.setItemText(4, _translate("MainWindow", "flipkart"))
        self.btnFindByUrl.setText(_translate("MainWindow", "FIND"))
        self.label_2.setText(_translate("MainWindow", "searching...."))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
