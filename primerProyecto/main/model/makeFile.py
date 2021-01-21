import os

def makeFile(stringName = "sinNombre.txt", path = "."):
    file = None
    file = open((path+"/"+stringName), "w+")
    if file is not None:
        return 1
    return 0

if __name__ == '__main__':
    makeFile()

