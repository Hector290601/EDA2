import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

class Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("main.ui", self)
        self.send.clicked.connect(self.getItems)
        #Agregar nuevos items
        self.lenguajes.addItem("Java")
        self.deleteItem("Python")

    def deleteItem(self, label):
        items = []
        for i in range(self.lenguajes.count()):
            item = self.lenguajes.item(i)
            items.append(item)
        labels = [i.text() for i in items]
        for i in range(len(labels)):
            if labels[i]== label:
                item = self.lenguajes.indexFromItem(self.lenguajes.item(i))
                self.lenguajes.model().removeRow(item.row())

    def getItems(self):
        items = self.lenguajes.selectedItems()
        selected = []
        for i in range(len(items)):
            selected.append(self.lenguajes.selectedItems()[i].text())
        self.labelLenguaje.setText("Seleccionados: " + "-".join(selected))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = Dialog()
    dialogo.show()
    app.exec_()
