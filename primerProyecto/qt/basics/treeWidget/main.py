#-*-coding:utf-8-*-
import sys, time
from PyQt5.QtWidgets import QApplication, QDialog, QTreeWidgetItem
from PyQt5 import uic
from os import  listdir, path, stat
from mimetypes import MimeTypes

class Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("main.ui", self)
        self.search.clicked.connect(self.getDir)

    def getDir(self):
        #limpiar árbol
        self.directorio.clear()
        #ruta indicada por el usuario
        pathDir = self.path.text()
        #verificar si es directorio
        if path.isdir(pathDir):
            for element in listdir(pathDir):
                name = element
                pathInfo = pathDir + "/" + name
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = Dialog()
    dialogo.show()
    app.exec_()
