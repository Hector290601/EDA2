# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:25:22 2020

@author: hrmha
"""
from math import log
from userClass import *
from userClass import *
from pythonCode import *
from getUsersData import *
import matplotlib.pyplot as plt

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
            transformedData.append((data[i]).lastName)
        elif args == 4:
            transformedData.append((data[i]).age)
        elif args == 5:
            transformedData.append((data[i]).gender)
        elif args == 6:
            transformedData.append(int((data[i]).phoneNumber))
        elif args == 7:
            transformedData.append(int((data[i]).creditCard))
        elif args == 8:
            transformedData.append((data[i]).cCType)
    return transformedData

def main():
    c = 2100
    x = range(1, c)
    yBstMo = []
    yBseMo = []
    yWseMo = []
    xCuadratico = []
    xLog = []
    userList = getData()
    data = transformData(userList)
    usersStack = addUserFromData(data, c)
    sortableData = transformToCountingSortType(usersStack, 6)
    for i in x:
        baseCaseMo, bestCaseMo, worseCaseMo = toPlot(sortableData[:i])
        xCuadratico.append(i * i)
        yBstMo.append(baseCaseMo)
        yBseMo.append(bestCaseMo)
        yWseMo.append(worseCaseMo)
    plt.subplot(331)
    plt.ylabel('My Own Algorithm')
    plt.xlabel('Caso Base')
    plt.plot(x, yBstMo, 'r-')
    plt.plot(x, x, 'm--')
    plt.plot(x, xCuadratico, 'k--')
    plt.subplot(335)
    plt.xlabel('Mejor Caso')
    plt.plot(x, yBseMo, 'g-')
    plt.subplot(339)
    plt.xlabel('Peor Caso')
    plt.plot(x, yWseMo, 'b-')
    plt.plot(x, x, 'm--')
    plt.plot(x, xCuadratico, 'k--')
    plt.savefig('plot.png')
    plt.show()

if __name__ == '__main__':
    main()
