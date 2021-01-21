#-*-coding:utf-8-*-
from fileData import *
from listFiles import *
from makeFile import *

def testFunctions():
    name = "test.txt"
    path = os.getcwd()
    currentWorkDir = completePath(name)
    files = lsOsScandir(path)
    if name not in files:
        if makeFile(stringName=name, path=path) == 1:
            print("Archivo ", name, " creado")
            lastTime = fileModifiedTime(name, path)
            tamanio = sizeFromFile(name, path)
            print("Ultima modificacion: ", lastTime)
            print("Tamaño del archivo (en bits): ", tamanio)
        else:
            print("Algo malo ha ocurrido")
    else:
        print("El archivo ", name, " ya existe en la ruta: ", path, " y está en: ", currentWorkDir)
        lastTime = fileModifiedTime(name, path)
        tamanio = sizeFromFile(name, path)
        print("Ultima modificacion: ", lastTime)
        print("Tamaño del archivo (en bits): ", tamanio)
    return 1

if __name__ == '__main__':
    testFunctions()
