#-*-coding:utf-8-*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.resize(200, 200)
        self.setWindowTitle('Dialog box')
        self.etiqueta = QLabel(self)

class Ventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(400, 400)
        self.setWindowTitle('Main Window')
        self.boton = QPushButton(self)
        self.boton.setText('Open Dialog Box')
        self.boton.resize(200, 30)
        self.dialogo = Dialogo()
        self.boton.clicked.connect(self.openDialog)
    def openDialog(self):
        self.dialogo.etiqueta.setText('Hello Dialog Boxes')
        self.dialogo.exec_()

app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
app.exec_()
