# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:25:22 2020

@author: hrmha
"""
import random
from treeClasses import *
from makeCases import *
import matplotlib.pyplot as plt
import os

count = 0

def makeDataTree(xSize):
    data = []
    for i in xSize:
        if i%5 == 0:
            data.append(random.choice(["+", "-", "*", "/"]))
        else:
            data.append(random.choice(["A", "E", "I", "O", "U"]))
    return data

def main():
    global count
    n = 1000
    c = (n*5) + 1
    x = range(c)
    yExplore = []
    yInsert = []
    sortableData = makeDataTree(x)
    grafo = graph()
    j = 0
    for i in range(5, c, 5):
        subString = sortableData[j:i]
        j = i
        case(grafo, subString)
        stringGraph, count = grafo.string(1)
        yExplore.append(count)
        yInsert.append(grafo.count)
        print(i)
    xExplore = range(len(yExplore))
    xInsert = range(len(yInsert))
    print(stringGraph)
    plt.figure(1)
    plt.suptitle('Árboles B')
    plt.subplot(334)
    plt.plot(xExplore, yExplore)
    plt.xlabel('Explorar el arbol')
    plt.subplot(336)
    plt.plot(xInsert, yInsert)
    plt.xlabel('Insertar en el arbol')
    plt.savefig('plot.png')
    plt.show()

if __name__ == '__main__':
    main()
