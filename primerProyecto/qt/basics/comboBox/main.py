import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

class Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("main.ui", self)
        self.send.clicked.connect(self.getItem)
        #Agregar items
        self.lenguajes.addItem("Java")
        #Eliminar items
        self.lenguajes.removeItem(0)

    def getItem(self):
        item = self.lenguajes.currentText()
        self.labelLenguaje.setText("Se ha seleccionado: " + item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = Dialog()
    dialogo.show()
    app.exec_()

