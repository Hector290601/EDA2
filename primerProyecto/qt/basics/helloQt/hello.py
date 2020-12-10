#-*-coding:utf-8-*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

#Clase heredada se QMainWindow(constructor de ventanas)

class Ventanta(QMainWindow):
    #Método contructor
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo ui
        uic.loadUi("hello.ui", self)
        self.setWindowTitle("Cambio de Título con setWindowTitle")

#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase ventana
ventana = Ventanta()
#Mostrar la ventana
ventana.show()
#Ejecutar la aplicación
app.exec_()

