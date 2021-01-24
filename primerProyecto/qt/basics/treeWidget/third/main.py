import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QFont, QColor

class StandardItem(QStandardItem):
    def __init__(self, txt = "", fontSize = 12, setBold = False, color = QColor(0, 0, 0)):
        super().__init__()
        fnt = QFont('Open Sans', fontSize)
        fnt.setBold(setBold)
        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)

class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("World diagram")
        self.resize(500, 700)
        treeView = QTreeView()
        treeView.setHeaderHidden(True)
        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()
        america = StandardItem("America", 16, setBold = True)
        california = StandardItem("California", 14)
        okland = StandardItem("Okland", 14)
        texas = StandardItem("Texas", 14)
        america.appendRow(california)
        canada = StandardItem("Canada", 16, setBold = True)
        california.appendRow(okland)
        rootNode.appendRow(america)
        rootNode.appendRow(canada)
        treeView.setModel(treeModel)
        treeView.expandAll()
        self.setCentralWidget(treeView)


app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())
