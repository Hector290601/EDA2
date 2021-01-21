import os
import time

def completePath(fileName):
    pathFromRot = os.getcwd() + "/" + fileName
    return pathFromRot

def fileModifiedTime(fileName, path = "."):
    size = os.path.getsize((path + "/" + fileName))
    return time.ctime(os.path.getmtime(fileName))

def sizeFromFile(fileName, path = "."):
    return os.path.getsize((path + "/" + fileName))

def main(fileName):
    modified = fileModifiedTime(fileName)
    size = sizeFromFile(fileName)
    print("modified: ", modified, "\nsize: ", size, "b")

if __name__ == '__main__':
    main("algo.txt")
