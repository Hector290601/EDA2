import os
import sys

def getRootPath():
    currentPath = os.getcwd()
    sep = os.path.sep
    rootNumber = 0
    for i in range(3):
        rootNumber = currentPath.find(sep, rootNumber) + 1
    rootPath = currentPath[:rootNumber]
    print(rootNumber)
    print(rootPath)
    return currentPath

def main():
    print(getRootPath())

if __name__ == "__main__":
    main()

