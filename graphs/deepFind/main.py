# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:25:22 2020

@author: hrmha
"""

from userClass import *
from graph import *
from getUsersData import *
from makeCases import *
import matplotlib.pyplot as plt
import os

def getData():
    data = usersListFromCsv()
    return data
#, lastName, age, gender, phoneNumber, creditCard, cCType
def transformToCountingSortType(data, args):
    transformedData = []
    for i in range(len(data)):
        if args == 1:
            transformedData.append(data[i].userId)
        elif args == 2:
            transformedData.append(int(((data[i]).name), 36))
        elif args == 3:
            transformedData.append(int((data[i]).lastName), 36)
        elif args == 4:
            transformedData.append((data[i]).age)
        elif args == 5:
            transformedData.append((data[i]).gender)
        elif args == 6:
            transformedData.append(int((data[i]).phoneNumber))
        elif args == 7:
            transformedData.append(int((data[i]).creditCard))
        elif args == 8:
            transformedData.append(int(((data[i]).cCType), 36))
    return transformedData

def main():
    c = 10
    x = range(1, c)
    yBase = []
    yBest = []
    yWorse = []
    userList = getData()
    data = transformData(userList)
    usersStack = addUserFromData(data, c)
    sortableData = transformToCountingSortType(usersStack, 1)
    for i in x:
        a = baseCaseTime(sortableData[:i])
        b = bestCaseTime(sortableData[:i])
        c = worseCaseTime(sortableData[:i])
        yBase.append(a)
        yBest.append(b)
        yWorse.append(c)
    plt.figure(1)
    plt.suptitle('Busqueda por expansión por tiempo')
    plt.subplot(334)
    plt.plot(x, yBase, 'y.')
    plt.xlabel('Caso base')
    plt.subplot(335)
    plt.plot(x, yBest, 'g.')
    plt.xlabel('Mejor caso')
    plt.subplot(336)
    plt.plot(x, yWorse, 'r')
    plt.xlabel('Peor caso')
    plt.savefig('plot.png')
    plt.show()


if __name__ == '__main__':
    main()
