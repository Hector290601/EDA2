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
        if i%3 == 0:
            data.append(random.choice(["+", "-", "*", "/"]))
        else:
            data.append(random.choice(["A", "E", "I", "O", "U"]))
    return data

def main():
    global count
    n = 1000
    c = (n*3) + 1
    x = range(c)
    yInf = []
    yPre = []
    yPos = []
    sortableData = makeDataTree(x)
    grafo = graph()
    j = 0
    for i in range(3, c, 3):
        subString = sortableData[j:i]
        j = i
        case(grafo, subString)
        _, count = grafo.string(1)
        yPos.append(count)
        _, count = grafo.string(2)
        yInf.append(count)
        _, count = grafo.string(3)
        yPre.append(count)
        print(i)
    xInf = range(len(yInf))
    xPos = range(len(yPos))
    xPre = range(len(yPre))
    plt.figure(1)
    plt.suptitle('Tipos de notaciones de árboles binarios')
    plt.subplot(334)
    plt.plot(xPre, yPre, 'y')
    plt.xlabel('Notación prefija')
    plt.subplot(335)
    plt.plot(xInf, yInf, 'g')
    plt.xlabel('Notación infija')
    plt.subplot(336)
    plt.plot(xPos, yPos, 'r')
    plt.xlabel('Notación sufija')
    plt.savefig('plot.png')
    plt.show()

if __name__ == '__main__':
    main()
