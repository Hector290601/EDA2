#-*-coding:utf-8-*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

#Clase heredada se QMainWindow(constructor de ventanas)
class Ventanta(QMainWindow):
    #Método contructor
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo ui
        uic.loadUi("main.ui", self)
        self.setWindowTitle("Elements Properties")
        #Maximizar la ventana al iniciar
        #self.showMaximized()
        #Fijar el tamaño de la ventana
        #Ajustar mínimo
        self.setMinimumSize(500, 500)
        #Ajustar máximo
        self.setMaximumSize(500, 500)
        #Mover la ventana y centrarla en el escritorio
        resolution = screenSize()
        resolutionAncho = resolution[0]
        resolutionAlto = resolution[1]
        left = int((resolutionAncho/2) - (self.frameSize().width()/2))
        top = int((resolutionAlto/2) - (self.frameSize().height()/2))
        self.move(left, top)
        #Desactivar ventana
        #self.setEnabled(False)
        #Cambiar el tipo de fuente
        #qfont = QFont("Arial", 12, QFont.Bold)
        #self.setFont(qfont)
        #Cambiar el tipo de mouse
        #self.setCursor(Qt.BusyCursor)
        #Cambiar vista mediante CSS
        #self.setStyleSheet("Background-color:blue; color:purple")
        self.pushButtonOne.setStyleSheet("background-color:black;color:white;font:14px;")

def screenSize():
    import platform
    sistema = platform.system()
    if sistema == 'Windows':
        import ctypes
        size = ctypes.windll.user32
        size = [size.GetSystemMetrics(0), size.GetSyztemMetrics(1)]
    else:
        import subprocess
        size = (None, None)
        args = ["xrandr", "-q", "-d", ":0"]
        proc = subprocess.Popen(args,stdout=subprocess.PIPE)
        for line in proc.stdout:
            if isinstance(line, bytes):
                line = line.decode("utf-8")
                if "Screen" in line:
                    size = (int(line.split()[7]),  int(line.split()[9][:-1]))
    return size

#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase ventana
ventana = Ventanta()
#Mostrar la ventana
ventana.show()
#Ejecutar la aplicación
app.exec_()

