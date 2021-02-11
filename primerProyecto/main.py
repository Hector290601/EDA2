from pathlib import Path 
import sys, os, time
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, QTreeWidgetItem, QDialog, QTreeView
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QColor
from PyQt5 import uic
import PyQt5.QtGui
from os import scandir, getcwd, walk, listdir, path, stat
from PyQt5.QtGui import QIcon
import subprocess
from mimetypes import MimeTypes

class File():
    name = ""
    dad = ""
    size = ""
    lastMod = ""

class Dir():
    name = ""
    dad  =""
    lastMod = ""
    sons = [None]
    QPos = None

class Window(QMainWindow):
    dirs = []
    sizes = []
    mods = []
    currentPat = ""
    currentPatL = ""
    files = [[], []]
    flagSorted = False
    archivos = 0
    carpetas = 0
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("main.ui", self)
        #crear barra de estado
        self.statusBar().showMessage("Welcome, made by Hector290601 on github")
        self.goToHome()
        self.showLeft(self.getRootPath)
        self.currentPatL = self.getAbsoulePath
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
        self.backButton.clicked.connect(self.returnPath)
        #   homeButton          QPushButton
        self.homeButton.clicked.connect(self.goToHome)
        #   sortButton          QPushButton
        self.sortButton.clicked.connect(self.sortOrNot)
        #   absolutePath        QLineEdit
        self.absolutePath.textChanged.connect(self.deleteSep)
        #   treeWidgetView      QTreeWidget
        self.treeWidgetView.itemDoubleClicked.connect(self.openElement)
        #   pathToSearch        QLineEdit
        self.pathToSearch.textChanged.connect(self.find)
        #   searchButton        QPushButton
        self.searchButton.clicked.connect(self.find)
    
    def showLeft(self, directorio):
        tw = self.leftView
        cts = []
        temp = []
        cg = QtWidgets.QTreeWidgetItem(tw, ["America"])
        c1 = QtWidgets.QTreeWidgetItem(cg, ["Mexico"])
        path = self.getRootPath()
        treeData = self.fillTree(path)
        tw.clear()
        cnt = 0
        for i in treeData:
            for k in i:
                k.QPos = QtWidgets.QTreeWidgetItem(tw, [k.name])
                kType = type(k)
                if kType is Dir:
                    newPath = path + os.path.sep + k.name
                    tmp = self.fillTree(newPath)
                    for j in tmp:
                        for l in j:
                            k.sons.append(None)
                            k.sons[-1] = QtWidgets.QTreeWidgetItem(k.QPos, [l.name])
    
    def fillTree(self, pth):
        dirs = []
        files = []
        rows = []
        if path.isdir(pth):
            for name in os.listdir(pth):
                pthInfo = pth + os.path.sep + name
                info = os.stat(pthInfo)
                if os.path.isdir(name):
                    current = Dir()
                    current.dad = path
                    current.lastMod = str(time.ctime(info.st_mtime))
                    current.name = name 
                    dirs.append(current)
                else:
                    current = File()
                    current.dad = path
                    current.name = name
                    current.lastMod = str(time.ctime(info.st_mtime))
                    files.append(current)
        rows.append(dirs)
        rows.append(files)
        return rows

    
    def makeTree(self, file):
        pathDir, dirs, rec, sizes, mods = ""
        if file.isdir():
            for element in listdir(pathDir):
                name = element
                dirs.append(name)
                pathInfo = pathDir + os.path.sep + name
                informacion = stat(pathInfo)
                if path.isdir(pathInfo):
                    type = "Carpeta de archivos"
                    size = ""
                    self.carpetas += 1
                    self.files[0].append(name)
                elif rec:
                    mime = MimeTypes()
                    type = mime.guess_type(pathInfo)[0]
                    size = str(informacion.st_size) + "B"
                    self.archivos += 1
                    self.files[1].append(name)
                else:
                    mime = MimeTypes()
                    type = mime.guess_type(pathInfo)[0]
                    size = str(informacion.st_size) + "B"
                    self.archivos += 1
                sizes.append(size)
                date = str(time.ctime(informacion.st_mtime))
                mods.append(date)
                row = [name, date, type, size]
                self.treeWidgetView.insertTopLevelItems(0, [QTreeWidgetItem(self.treeWidgetView, row)])

    
    def deleteSep(self):
        text = self.absolutePath.text()
        if text.endswith(os.path.sep):
            text = text[:-1]
        self.absolutePath.setText(text)

    def returnPath(self):
        self.treeWidgetView.clear()
        pathDir = self.absolutePath.text()
        pathDir = pathDir[::-1]
        pathDir = pathDir[pathDir.find(os.path.sep):]
        pathDir = pathDir[::-1]
        if pathDir.endswith(os.path.sep):
            pathDir = pathDir[:-1]
        if pathDir == "":
            pathDir = self.getRootPath()
        self.absolutePath.setText(pathDir)
        self.currentPat = pathDir
        self.getAbsoulePath()
        if self.flagSorted:
            self.sort()

    def find(self):
        nameToFind = self.pathToSearch.text()
        if self.flagSorted:
            number = self.binaryFind(self.dirs, nameToFind)
        else:
            number = self.linealfind(self.dirs, nameToFind)
        if number != -1:
            self.treeWidgetView.setCurrentItem(self.treeWidgetView.topLevelItem(number))

    def linealfind(self, data, target):
        finded = False
        for i in range(len(data)):
            if not finded:
                if (data[i]).startswith(target):
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
                if (data[middle]).startswith(target):
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

    def walkOnDirsData(self, dirsData, pathDir, rec = False):
        dirs = []
        sizes = []
        mods = []
        self.archivos = 0
        self.carpetas = 0
        for element in listdir(pathDir):
            name = element
            dirs.append(name)
            pathInfo = pathDir + os.path.sep + name
            informacion = stat(pathInfo)
            if path.isdir(pathInfo):
                type = "Carpeta de archivos"
                size = ""
                self.carpetas += 1
                self.files[0].append(name)
            elif rec:
                mime = MimeTypes()
                type = mime.guess_type(pathInfo)[0]
                size = str(informacion.st_size) + "B"
                self.archivos += 1
                self.files[1].append(name)
            else:
                mime = MimeTypes()
                type = mime.guess_type(pathInfo)[0]
                size = str(informacion.st_size) + "B"
                self.archivos += 1
            sizes.append(size)
            date = str(time.ctime(informacion.st_mtime))
            mods.append(date)
            row = [name, date, type, size]
            self.treeWidgetView.insertTopLevelItems(0, [QTreeWidgetItem(self.treeWidgetView, row)])

    
    def sort(self):
        self.treeWidgetView.clear()
        dirsData = self.quickSort(self.dirs, 0, len(self.dirs)-1)
        pathDir = self.absolutePath.text()
        self.dirs = []
        self.walkOnDirsData(dirsData, pathDir)

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
        if file == None:
            print("Error")
        self.getAbsoulePath()

    def getRootPath(self):
        currentPath = os.getcwd()
        sep = os.path.sep
        rootNumber = 0
        for i in range(3):
            rootNumber = currentPath.find(sep, rootNumber) + 1
        rootPath = currentPath[:rootNumber]
        return rootPath

    def goToHome(self, rec = False):
        self.treeWidgetView.clear()
        pathDir = self.getRootPath()
        self.absolutePath.setText(pathDir)
        self.currentPat = pathDir
        if path.isdir(pathDir):
            self.walkOnDirsData(listdir(pathDir), pathDir)
        self.lcdFilesCounter.display(self.archivos)
        self.lcdDirsCounter.display(self.carpetas)

    def getAbsoulePath(self):
        self.treeWidgetView.clear()
        pathDir = self.absolutePath.text()
        if pathDir == "":
            pathDir = self.getRootPath()
            self.absolutePath.setText(pathDir)
        self.currentPat = pathDir
        if path.isdir(pathDir):
            self.walkOnDirsData(listdir(pathDir), pathDir)
        self.lcdFilesCounter.display(self.archivos)
        self.lcdDirsCounter.display(self.carpetas)

    def openElement(self):
        item = self.treeWidgetView.currentItem()
        pth = self.absolutePath.text()
        if pth.endswith(os.path.sep):
            pth = pth[:-1]
        elemento = self.absolutePath.text() + os.path.sep + item.text(0)
        if os.path.isdir(elemento):
            self.absolutePath.setText(elemento)
            self.getAbsoulePath()
        else:
            if sys.platform == "win32":
                os.startfile(elemento)
            else:
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, elemento])

    def completePath(fileName):
        pathFromRot = os.getcwd() + os.path.sep + fileName
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
