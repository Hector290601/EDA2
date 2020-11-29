# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:25:22 2020

@author: hrmha
"""
from math import log
from userClass import *
from userClass import *
from extern import *
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
    x = range(100, c)
    yBstMoEx = []
    yBseMoEx = []
    yWseMoEx = []
    xCuadratico = []
    xLog = []
    userList = getData()
    data = transformData(userList)
    usersStack = addUserFromData(data, c)
    sortableData = transformToCountingSortType(usersStack, 6)
    for i in x:
        baseCaseMoEx, bestCaseMoEx, worseCaseMoEx = toPlotExtern(sortableData[:i])
        xCuadratico.append(i * i)
        yBstMoEx.append(baseCaseMoEx)
        yBseMoEx.append(bestCaseMoEx)
        yWseMoEx.append(worseCaseMoEx)
    plt.subplot(331)
    plt.ylabel('ExternSort')
    plt.xlabel('Caso Base')
    plt.plot(x, yBstMoEx, 'r-')
    plt.plot(x, x, 'm--')
    plt.plot(x, xCuadratico, 'k--')
    plt.subplot(335)
    plt.xlabel('Mejor Caso')
    plt.plot(x, yBseMoEx, 'g-')
    plt.subplot(339)
    plt.xlabel('Peor Caso')
    plt.plot(x, yWseMoEx, 'b-')
    plt.plot(x, x, 'm--')
    plt.plot(x, xCuadratico, 'k--')
    plt.savefig('plot.png')
    plt.show()

if __name__ == '__main__':
    main()
