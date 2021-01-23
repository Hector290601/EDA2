import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QIcon

class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("main.ui", self)
        #crear barra de estado
        self.statusBar().showMessage("Welcome")
        #crear objeto de la clase menuBar
        menu = self.menuBar()
        #menu padre
        menuFile = menu.addMenu("&File")
        #menu padre
        menuEdit = menu.addMenu("&Edit")
        #agregar elemento accion al menu file
        menuFileOpen = QAction(QIcon(), "&Open", self)
        menuFileOpen.setShortcut("Ctrl+o") #atajo del teclado
        menuFileOpen.setStatusTip("Open") #mensaje en la barra de estado
        menuFileOpen.triggered.connect(self.menuFileOpenAct)
        menuFile.addAction(menuFileOpen)
        #agregar elemento accion al menu file
        menuFileClose = QAction(QIcon(), "&Close", self)
        menuFileClose.setShortcut("Ctrl+q") #atajo del teclado
        menuFileClose.setStatusTip("Close") #mensaje en la barra de estado
        menuFileClose.triggered.connect(self.menuFileCloseAct)
        menuFile.addAction(menuFileClose)
        #add a subMenu to edit
        menuEditOptions = menuEdit.addMenu("&Options")
        menuEditOptionsFind = QAction(QIcon(), "&Find", self)
        menuEditOptionsFind.setShortcut("Ctrl+f")
        menuEditOptionsFind.setStatusTip("Find")
        menuEditOptionsFind.triggered.connect(self.menuEditOptionsFindAcc)
        menuEditOptions.addAction(menuEditOptionsFind)

    def menuFileOpenAct(self):
        QMessageBox.information(self, "Open", "Open Action", QMessageBox.Discard)
    
    def menuFileCloseAct(self):
        QMessageBox.information(self, "Close", "Close Action", QMessageBox.Discard)

    def menuEditOptionsFindAcc(self):
        QMessageBox.information(self, "Find", "Find Action", QMessageBox.Discard)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
