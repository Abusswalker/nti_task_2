from views.window_2 import Ui_MainWindow
from views.add_operation import Ui_MainWindow as AddOperation
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3


class Dialog(QMainWindow, AddOperation):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Добавить')
        self.parent = parent


class Window2(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(Window2, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Продажи')
        self.path = path

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        self.pushButton_add.clicked.connect(self.add)

    def add(self):
        win = Dialog(self)
        win.show()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Window2("../bd.db")
    mainWindow.show()
    sys.exit(app.exec())
