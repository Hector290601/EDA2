from pathlib import Path 
import sys, os, time
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, QTreeWidgetItem, QDialog
from PyQt5 import uic
from os import scandir, getcwd, walk, listdir, path, stat
from PyQt5.QtGui import QIcon
import subprocess
from mimetypes import MimeTypes

class Window(QMainWindow):
    dirs = []
    sizes = []
    mods = []
    currentPat = ""
    flagSorted = False
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("main.ui", self)
        #crear barra de estado
        self.statusBar().showMessage("Welcome, made by Hector290601 on github")
        self.goToHome()
        #crear objeto de la clase menuBar
        menu = self.menuBar()
        #menu padre
        menuFile = menu.addMenu("&File")
        #menu padre
        #agregar elemento accion al menu file
        menuNewFile = QAction(QIcon(), "&New file", self)
        menuNewFile.setShortcut("Ctrl+n") #atajo del teclado
        menuNewFile.setStatusTip("newFile") #mensaje en la barra de estado
        menuNewFile.triggered.connect(self.menuNewFileAct)
        menuFile.addAction(menuNewFile)
        #Eventos:
        #   backButton          QPushButton
        #   homeButton          QPushButton
        self.homeButton.clicked.connect(self.goToHome)
        #   sortButton          QPushButton
        self.sortButton.clicked.connect(self.sortOrNot)
        #   absolutePath        QLineEdit
        #   treeWidgetView      QTreeWidget
        self.treeWidgetView.itemDoubleClicked.connect(self.openElement)
        #   lcdFilesCounter     QLCDNumber
        #   lcddirsCounter      QLCDNumber
        #   pathToSearch        QLineEdit
        #   searchButton        QPushButton
        self.searchButton.clicked.connect(self.find)

    def find(self):
        nameToFind = self.pathToSearch.text()
        if self.flagSorted:
            number = self.binaryFind(self.dirs, nameToFind)
        else:
            number = self.linealfind(self.dirs, nameToFind)
        if number == -1:
            pass
        else:
            self.treeWidgetView.setCurrentItem(self.treeWidgetView.topLevelItem(number))

    def linealfind(self, data, target):
        finded = False
        for i in range(len(data)):
            if not finded:
                if data[i] == target:
                    finded = True
                    return i
            else:
                break
        return -1

    def binaryFind(self, data, target):
        start = 0
        end = len(data)
        finded = False
        while start <= end and not finded:
            middle = (start + end) // 2
            if middle < len(data):
                if data[middle] == target:
                    finded = True
                    break
                else:
                    if target < data[middle]:
                        end = middle - 1
                    else:
                        start = middle + 1
            else:
                break
        if finded:
            return middle
        else:
            return -1

    def sortOrNot(self):
        if self.flagSorted:
            self.getAbsoulePath()
        else:
            self.sort()
        self.flagSorted = not self.flagSorted

    def sort(self):
        self.treeWidgetView.clear()
        dirsData = self.quickSort(self.dirs, 0, len(self.dirs)-1)
        pathDir = self.absolutePath.text()
        self.dirs = []
        for element in dirsData:
            name = element
            self.dirs.append(name)
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
            self.treeWidgetView.insertTopLevelItems(0, [QTreeWidgetItem(self.treeWidgetView, row)])

    def dividir(self, data, l, h):
        index = (l - 1) #4
        pivote = data[h] #4
        for j in range(l, h): #
            if data[j] <= pivote:
                index +=1
                data[index], data[j] = data[j], data[index]
        data[index+1], data[h] = data[h], data[index+1]
        return (index+1)

    def quickSort(self, data, l, h):
        if len(data) < 2:
            return data
        else:
            if l < h:
                pIndex = self.dividir(data, l, h)
                self.quickSort(data, l, pIndex-1)
                self.quickSort(data, pIndex +1, h)
        return data

    def menuNewFileAct(self):
        dialogo = self.Dialogo()
        dialogo.show()
        dialogo.exec_()
        name = dialogo.name
        file = None
        file = open((self.currentPat + os.path.sep + name), "w+")
        self.getAbsoulePath()

    def getRootPath(self):
        currentPath = os.getcwd()
        sep = os.path.sep
        rootNumber = 0
        for i in range(3):
            rootNumber = currentPath.find(sep, rootNumber) + 1
        rootPath = currentPath[:rootNumber]
        return rootPath

    def goToHome(self):
        self.treeWidgetView.clear()
        pathDir = self.getRootPath()
        self.absolutePath.setText(pathDir)
        self.currentPat = pathDir
        dirs = []
        sizes = []
        mods = []
        archivos = 0
        carpetas = 0
        if path.isdir(pathDir):
            for element in listdir(pathDir):
                name = element
                dirs.append(name)
                pathInfo = pathDir + os.path.sep + name
                informacion = stat(pathInfo)
                if path.isdir(pathInfo):
                    type = "Carpeta de archivos"
                    size = ""
                    carpetas += 1
                else:
                    mime = MimeTypes()
                    type = mime.guess_type(pathInfo)[0]
                    size = str(informacion.st_size) + "B"
                    archivos += 1
                sizes.append(size)
                #Fecha de modificación del archivo o carpeta
                date = str(time.ctime(informacion.st_mtime))
                mods.append(date)
                #crear un arreglo para almacenar items
                row = [name, date, type, size]
                #insertar la fila
                self.treeWidgetView.insertTopLevelItems(0, [QTreeWidgetItem(self.treeWidgetView, row)])
            self.dirs = dirs
            self.sizes = sizes
            self.mods = mods
        self.lcdFilesCounter.display(archivos)
        self.lcdDirsCounter.display(carpetas)

    def getAbsoulePath(self):
        self.treeWidgetView.clear()
        pathDir = self.absolutePath.text()
        dirs = []
        sizes = []
        mods = []
        archivos = 0
        carpetas = 0
        if pathDir == "":
            pathDir = self.getRootPath()
            self.absolutePath.setText(pathDir)
        self.currentPat = pathDir
        if path.isdir(pathDir):
            for element in listdir(pathDir):
                name = element
                dirs.append(name)
                pathInfo = pathDir + os.path.sep + name
                informacion = stat(pathInfo)
                if path.isdir(pathInfo):
                    type = "Carpeta de archivos"
                    size = ""
                    carpetas += 1
                else:
                    mime = MimeTypes()
                    type = mime.guess_type(pathInfo)[0]
                    size = str(informacion.st_size) + "B"
                    archivos += 1
                sizes.append(size)
                #Fecha de modificación del archivo o carpeta
                date = str(time.ctime(informacion.st_mtime))
                mods.append(date)
                #crear un arreglo para almacenar items
                row = [name, date, type, size]
                #insertar la fila
                self.treeWidgetView.insertTopLevelItems(0, [QTreeWidgetItem(self.treeWidgetView, row)])
            self.dirs = dirs
            self.sizes = sizes
            self.dirs = dirs
        self.lcdFilesCounter.display(archivos)
        self.lcdDirsCounter.display(carpetas)

    def openElement(self):
        #obtener el item
        item = self.treeWidgetView.currentItem()
        #crear la ruta accediendo al nombre del elemento
        elemento = self.absolutePath.text() + os.path.sep + item.text(0)
        #comprobar si es un directorio, navegar en él
        if os.path.isdir(elemento):
            self.absolutePath.setText(elemento)
            self.getAbsoulePath()
        else:   #abrirlo con el programa por defecto
            if sys.platform == "win32":
                os.startfile(elemento)
            else:
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, elemento])

    def completePath(fileName):
        pathFromRot = os.getcwd() + "/" + fileName
        return pathFromRot

    class Dialogo(QDialog):
        name = ""
        def __init__(self):
            QDialog.__init__(self)
            uic.loadUi("createNewFile.ui", self)
            self.createButton.clicked.connect(self.getName)
            self.createButton.clicked.connect(self.close)

        def getName(self):
            self.name = self.newName.text()

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()

