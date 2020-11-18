# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:25:22 2020

@author: hrmha
"""

from userClass import *
from userClass import *
from countingSort import *
from radixSort import *
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
    c = 100
    x = range(1, c)
    yBstCs = []
    yBseCs = []
    yWseCs = []
    yBstRs = []
    yBseRs = []
    yWseRs = []
    userList = getData()
    data = transformData(userList)
    usersStack = addUserFromData(data, c)
    sortableData = transformToCountingSortType(usersStack, 1)
    for i in x:
        baseCaseCs, bestCaseCs, worseCaseCs = toPlotCs(sortableData[:i])
        baseCaseRs, bestCaseRs, worseCaseRs = toPlotRs(sortableData[:i])
        yBstCs.append(baseCaseCs)
        yBseCs.append(bestCaseCs)
        yWseCs.append(worseCaseCs)
        yBstRs.append(baseCaseRs)
        yBseRs.append(bestCaseRs)
        yWseRs.append(worseCaseRs)
    plt.subplot(331)
    plt.ylabel('Counting sort')
    plt.xlabel('Caso Base')
    plt.plot(x, yBstCs, 'r-')
    plt.subplot(332)
    plt.xlabel('Mejor Caso')
    plt.plot(x, yBseCs, 'g-')
    plt.subplot(333)
    plt.xlabel('Peor Caso')
    plt.plot(x, yWseCs, 'b-')
    plt.subplot(337)
    plt.xlabel('Caso Base')
    plt.ylabel('Radix sort')
    plt.plot(x, yBstRs, 'r-')
    plt.subplot(338)
    plt.xlabel('Mejor Caso')
    plt.plot(x, yBseRs, 'g-')
    plt.subplot(339)
    plt.xlabel('Peor Caso')
    plt.plot(x, yWseRs, 'b-')
    plt.savefig('plot.png')
    plt.show()

if __name__ == '__main__':
    main()
