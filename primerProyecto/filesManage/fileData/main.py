import os
import time

def fileModifiedTime(fileName):
    return time.ctime(os.path.getmtime(fileName))

def sizeFromFile(fileName):
    return os.path.getsize(fileName)

def main(fileName):
    modified = fileModifiedTime(fileName)
    size = sizeFromFile(fileName)
    print("modified: ", modified, "\nsize: ", size, "b")

if __name__ == '__main__':
    main("algo.txt")
