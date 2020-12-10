# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:25:22 2020

@author: hrmha
"""

from userClass import *
from userClass import *
from binaryFind import *
from linealFind import *
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
    c = 100
    x = range(1, c)
    yBaBiItQs = []
    yBsBiItQs = []
    yWsBiItQs = []
    yBaBiRvQs = []
    yBsBiRvQs = []
    yWsBiRvQs = []
    yBaBiItBs = []
    yBsBiItBs = []
    yWsBiItBs = []
    yBaBiRvBs = []
    yBsBiRvBs = []
    yWsBiRvBs = []
    yBaLiIt = []
    yBsLiIt = []
    yWsLiIt = []
    yBaLiRv = []
    yBsLiRv = []
    yWsLiRv = []
    userList = getData()
    data = transformData(userList)
    usersStack = addUserFromData(data, c)
    sortableData = transformToCountingSortType(usersStack, 1)
    for i in x:
        BaBiItQs, BsBiItQs, WsBiItQs, BaBiRvQs, BsBiRvQs, WsBiRvQs, BaBiItBs, BsBiItBs, WsBiItBs, BaBiRvBs, BsBiRvBs, WsBiRvBs = toPlotBf(sortableData[:i])
        BaLiIt, BsLiIt, WsLiIt, BaLiRv, BsLiRv, WsLiRv = toPlotLf(sortableData[:i])
        yBaBiItQs.append(BaBiItQs)
        yBsBiItQs.append(BsBiItQs)
        yWsBiItQs.append(WsBiItQs)
        yBaBiRvQs.append(BaBiRvQs)
        yBsBiRvQs.append(BsBiRvQs)
        yWsBiRvQs.append(WsBiRvQs)
        yBaBiItBs.append(BaBiItBs)
        yBsBiItBs.append(BsBiItBs)
        yWsBiItBs.append(WsBiItBs)
        yBaBiRvBs.append(BaBiRvBs)
        yBsBiRvBs.append(BsBiRvBs)
        yWsBiRvBs.append(WsBiRvBs)
        yBaLiIt.append(BaLiIt)
        yBsLiIt.append(BsLiIt)
        yWsLiIt.append(WsLiIt)
        yBaLiRv.append(BaLiRv)
        yBsLiRv.append(BsLiRv)
        yWsLiRv.append(WsLiRv)
    plt.figure(1)
    plt.suptitle('Busqueda Binaria MergeSort')
    plt.subplot(331)
    plt.plot(x, yBaBiItQs, 'y.')
    plt.xlabel('Caso base')
    plt.ylabel('Iterativa')
    plt.subplot(332)
    plt.plot(x, yBsBiItQs, 'g.')
    plt.xlabel('Mejor caso')
    plt.subplot(333)
    plt.plot(x, yWsBiItQs, 'r.')
    plt.xlabel('Peor caso')
    plt.subplot(337)
    plt.xlabel('Caso base')
    plt.ylabel('Recursiva')
    plt.plot(x, yBaBiRvQs, 'y.')
    plt.subplot(338)
    plt.xlabel('Mejor caso')
    plt.plot(x, yBsBiRvQs, 'g.')
    plt.subplot(339)
    plt.xlabel('Peor caso')
    plt.plot(x, yWsBiRvQs, 'r.')
    plt.savefig('plot1.png')
    plt.figure(2)
    plt.suptitle('Busqueda Binaria BuubleSort')
    plt.subplot(331)
    plt.ylabel('Iterativa')
    plt.plot(x, yBaBiItBs, 'y.')
    plt.xlabel('Caso base')
    plt.subplot(332)
    plt.plot(x, yBsBiItBs, 'g.')
    plt.xlabel('Mejor caso')
    plt.subplot(333)
    plt.plot(x, yWsBiItBs, 'r.')
    plt.xlabel('Peor caso')
    plt.subplot(337)
    plt.ylabel('Recursiva')
    plt.xlabel('Caso base')
    plt.plot(x, yBaBiRvBs, 'y.')
    plt.subplot(338)
    plt.xlabel('Mejor caso')
    plt.plot(x, yBsBiRvBs, 'g.')
    plt.subplot(339)
    plt.xlabel('Peor caso')
    plt.plot(x, yWsBiRvBs, 'r.')
    plt.savefig('plot2.png')
    plt.figure(3)
    plt.suptitle('Busqueda Lineal')
    plt.subplot(331)
    plt.xlabel('Caso base')
    plt.ylabel('Iterativa')
    plt.plot(x, yBaLiIt, 'y.')
    plt.subplot(332)
    plt.xlabel('Mejor caso')
    plt.plot(x, yBsLiIt, 'g.')
    plt.subplot(333)
    plt.xlabel('Peor caso')
    plt.plot(x, yWsLiIt, 'r.')
    plt.subplot(337)
    plt.xlabel('Caso base')
    plt.ylabel('Recursiva')
    plt.plot(x, yBaLiRv, 'y.')
    plt.subplot(338)
    plt.xlabel('Mejor caso')
    plt.plot(x, yBsLiRv, 'g.')
    plt.subplot(339)
    plt.xlabel('Peor caso')
    plt.plot(x, yWsLiRv, 'r.')
    plt.savefig('plot3.png')
    plt.show()

if __name__ == '__main__':
    main()
