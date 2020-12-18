from views.window_1 import Ui_MainWindow
from views.add_buy import Ui_MainWindow as AddBuy
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3


class Dialog(QMainWindow, AddBuy):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Добавить')
        self.parent = parent


class Window1(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(Window1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Покупки')
        self.path = path

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

        self.pushButton_add.clicked.connect(self.add)

    def add(self):
        win = Dialog(self)
        win.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Window1("../bd.db")
    mainWindow.show()
    sys.exit(app.exec())
