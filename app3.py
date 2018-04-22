import pandas as pd
import time
import pickle
from PyQt5 import QtCore, QtGui, QtWidgets
import mining
from get_book_details import get_details_from_amazon, get_details_from_snapdeal
from get_book_urls import fetch_amazon, fetch_snapdeal


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # header
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

        MainWindow.setObjectName("MCA Project")
        MainWindow.resize(380, 350)
        self.mw = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.projectname = QtWidgets.QLabel(self.centralwidget)
        self.projectname.setGeometry(QtCore.QRect(10, 10, 361, 31))
        self.projectname.setObjectName("projectname")
        self.category = QtWidgets.QLabel(self.centralwidget)
        self.category.setGeometry(QtCore.QRect(10, 50, 131, 16))
        self.category.setObjectName("category")
        self.btnFindByCat = QtWidgets.QPushButton(self.centralwidget)
        self.btnFindByCat.setGeometry(QtCore.QRect(10, 120, 171, 31))
        self.btnFindByCat.setObjectName("btnFindByCat")
        self.searchword = QtWidgets.QTextEdit(self.centralwidget)
        self.searchword.setGeometry(QtCore.QRect(10, 240, 251, 31))
        self.searchword.setObjectName("searchword")
        self.selecategory = QtWidgets.QComboBox(self.centralwidget)
        self.selecategory.setGeometry(QtCore.QRect(10, 70, 351, 22))
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
        self.btnSearchByName.setGeometry(QtCore.QRect(270, 240, 101, 31))
        self.btnSearchByName.setObjectName("btnSearchByName")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 220, 102, 13))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 190, 71, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 361, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 419, 13))
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 200, 381, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.recentBtn = QtWidgets.QPushButton(self.centralwidget)
        self.recentBtn.setGeometry(QtCore.QRect(200, 120, 161, 31))
        self.recentBtn.setObjectName("recentBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSchedule_Crawler = QtWidgets.QAction(MainWindow)
        self.actionSchedule_Crawler.setObjectName("actionSchedule_Crawler")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionSchedule_Crawler)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # listener
        self.btnFindByCat.clicked.connect(self.find_by_category)
        self.recentBtn.clicked.connect(self.load_recent_run)
        self.actionExit.setShortcut("Ctrl+Q")
        self.actionExit.setStatusTip('Leave The App')
        self.actionExit.triggered.connect(self.closeapp)
        self.actionSchedule_Crawler.setShortcut("Ctrl+Q")
        self.actionSchedule_Crawler.setStatusTip('Set a time to autorun')
        self.actionSchedule_Crawler.triggered.connect(self.schedule)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.projectname.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">BOOK DISCOUNT FINDER</span></p></body></html>"))
        self.category.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Choose a category</span></p></body></html>"))
        self.btnFindByCat.setText(_translate("MainWindow", "Run Discount Finder"))
        self.searchword.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
        self.label_2.setText(_translate("MainWindow", "Type a Name of Book"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", " click search to start the web spider and wait for completion"))
        self.recentBtn.setText(_translate("MainWindow", "Recent Search Results"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSchedule_Crawler.setText(_translate("MainWindow", "Schedule Crawler"))
        self.actionExit.setText(_translate("MainWindow", "exit"))

    # main code
    def closeapp(self):
        sys.exit(0)

    def schedule(self):
        pass

    def find_by_category(self):
        try:
            text = str(self.selecategory.currentText())
            text = "_".join(text.split())
            url = mining.amz_categories.get(text)
            url_2 = mining.snapdeal_categories.get(text)
            results = fetch_amazon(url, self.headers)
            results_2 = fetch_snapdeal(url_2, self.headers)
            book_list = []
            if not isinstance(results, str):
                for book_url in results:
                    book_list = get_details_from_amazon(book_url, self.headers, book_list)
                print(book_list)
            else:
                self.label_3.setText("there was an error fetching data from amazon")
            if not isinstance(results_2, str):
                for book_url in results_2:
                    book_list = get_details_from_snapdeal(book_url, self.headers, book_list)
                print(book_list)
            else:
                self.label_3.setText("there was an error fetching data from amazon")
            if book_list:
                # save data in pandas
                df = pd.DataFrame(book_list)
                current_day = time.strftime("%d_%m_%Y")
                csv_file = text + '_' + current_day + ".csv"
                df.to_csv(csv_file)
                pickle.dump({'path':csv_file}, open("recent.p", "wb"))

                self.label_3.setText("completed task, saved to " + csv_file)
            else:
                self.label_3.setText("there was an error")
        except Exception as e:
            self.label_3.setText(str(e))

    def load_recent_run(self):
        csv_file=pickle.load(open("recent.p", "rb"))
        file_path = csv_file['path']


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
