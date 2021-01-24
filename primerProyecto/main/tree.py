import sys, time
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QColor
from PyQt5 import uic
import os

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
        QMainWindow.__init__(self)
        uic.loadUi("tree.ui", self)
        self.resize(500, 700)
        tw = self.treeWidget
        cts = []
        temp = []
        cg = QtWidgets.QTreeWidgetItem(tw, ["America"])
        c1 = QtWidgets.QTreeWidgetItem(cg, ["Mexico"])
        path = "/home/hector"
        treeData = self.fillTree(path)
        self.treeWidget.clear()
        cnt = 0
        for i in treeData:
            for k in i:
                k.QPos = QtWidgets.QTreeWidgetItem(tw, [k.name])
                kType = type(k)
                if kType is Dir:
                    try:
                        newPath = path + os.path.sep + k.name
                        print(newPath)
                        tmp = self.fillTree(newPath)
                        print(tmp)
                        for j in tmp:
                            for l in j:
                                k.sons.append(None)
                                k.sons[-1] = QtWidgets.QTreeWidgetItem(k.QPos, [l.name])
                    except:
                        pass
    
    def fillTree(self, path):
        dirs = []
        files = []
        rows = []
        for name in os.listdir(path):
            pthInfo = path + os.path.sep + name
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


app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())