import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

class Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("main.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = Dialog()
    dialogo.show()
    app.exec_()
