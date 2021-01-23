#-*-coding:utf-8-*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel
from PyQt5 import uic

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("main.ui", self)
        self.radioValue()
        self.send.clicked.connect(self.radioValue)
        self.checkBoxState()
        self.send.clicked.connect(self.checkBoxState)

    def radioValue(self):
        if self.python3.isChecked():
            self.labelLenguaje.setText("Python 3.X ha sido seleccionado")
        elif self.php.isChecked():
            self.labelLenguaje.setText("PHP ha sido seleccionado")
        elif self.python2.isChecked():
            self.labelLenguaje.setText("Python 2.X ha sido seleccionado")
        elif self.ansiC.isChecked():
            self.labelLenguaje.setText("C ha sido seleccionado")
        elif self.cpp.isChecked():
            self.labelLenguaje.setText("C++ ha sido seleccionado")
        else:
            self.labelLenguaje.setText("No se ha seleccionado ningún lenguaje")

    def checkBoxState(self):
        if self.accept.isChecked():
            self.labelSelected.setText("TyC aceptados")
        else:
            self.labelSelected.setText("TyC no aceptados")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Dialogo()
    ventana.show()
    app.exec_()
