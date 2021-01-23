import sys, re
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic

class Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("poll.ui", self)
        self.name.textChanged.connect(self.validarNombre)
        self.email.textChanged.connect(self.validarEmail)
        self.send.clicked.connect(self.validarFormulario)

    def validarNombre(self):
        nombre = self.name.text()
        validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', nombre, re.I)
        if nombre == "":
            self.name.setStyleSheet("border: 1px solid yellow")
            return False
        elif not validar:
            self.name.setStyleSheet("border: 1px solid red")
            return False
        else:
            self.name.setStyleSheet("border: 1px solid green")
            return True
    
    def validarEmail(self):
        email = self.email.text()
        validar = re.match('^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$', email, re.I)
        if email == "":
            self.email.setStyleSheet("border: 1px solid yellow")
            return False
        elif not validar:
            self.email.setStyleSheet("border: 1px solid red")
            return False
        else:
            self.email.setStyleSheet("border: 1px solid green")
            return True

    def validarFormulario(self):
        if self.validarNombre() and self.validarEmail():
            QMessageBox.information(self, "Formulario correcto", "validación correcta", QMessageBox.Discard)
        else:
            QMessageBox.warning(self, "Formulario incorrecto", "Fallo en la validación", QMessageBox.Discard)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = Dialog()
    dialogo.show()
    app.exec_()
