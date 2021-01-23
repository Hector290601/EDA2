#-*-coding:utf-8-*-
import sys, time
from PyQt5.QtWidgets import QApplication, QDialog, QTreeWidgetItem
from PyQt5 import uic
from os import listdir, path, stat
import os
import subprocess
from mimetypes import MimeTypes

class Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("main.ui", self)
        self.search.clicked.connect(self.getDir)
        self.directorio.itemDoubleClicked.connect(self.openElement)

    def getDir(self):
        #limpiar árbol
        self.directorio.clear()
        #ruta indicada por el usuario
        pathDir = self.path.text()
        if pathDir == "":
            pathDir = "/home/hector"
            self.path.setText("/home/hector")
        #verificar si es directorio
        if path.isdir(pathDir):
            for element in listdir(pathDir):
                name = element
                pathInfo = pathDir + os.path.sep + name
                informacion = stat(pathInfo)
                if path.isdir(pathInfo):
                    type = "Carpeta de archivos"
                    size = ""
                else:
                    mime = MimeTypes()
                    type = mime.guess_type(pathInfo)[0]
                    size = str(informacion.st_size) + "B"
                #Fecha de modificación del archivo o carpeta
                date = str(time.ctime(informacion.st_mtime))
                #crear un arreglo para almacenar items
                row = [name, date, type, size]
                #insertar la fila
                self.directorio.insertTopLevelItems(0, [QTreeWidgetItem(self.directorio, row)])

    def openElement(self):
        #obtener el item
        item = self.directorio.currentItem()
        #crear la ruta accediendo al nombre del elemento
        elemento = self.path.text() + os.path.sep + item.text(0)
        #comprobar si es un directorio, navegar en él
        if os.path.isdir(elemento):
            self.path.setText(elemento)
            self.getDir()
        else:   #abrirlo con el programa por defecto
            if sys.platform == "win32":
                os.startfile(elemento)
            else:
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, elemento])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = Dialog()
    dialogo.show()
    app.exec_()
