#-*-coding:utf-8-*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
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
    def showEvent(self, event):
        self.labelOne.setText("¡¡HOLA EVENTOS!!")

    def closeEvent(self, event):
        resultado = QMessageBox.question(self, '¿Salir?', '¿Seguro que desea salir?', QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def moveEvent(self, event):
        x = str(event.pos().x())
        y = str(event.pos().y())
        self.labelPos.setText('X: ' + x + ' Y: ' + y)

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

