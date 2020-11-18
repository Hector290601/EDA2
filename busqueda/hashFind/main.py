# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:25:22 2020

@author: hrmha
"""
if __name__ == '__main__':
    print('Starting')
from userClass import *
from userClass import *
from hash import *
from findHash import *
from getUsersData import *
import matplotlib.pyplot as plt

def getData():
    data = usersListFromCsv()
    return data
#, lastName, age, gender, phoneNumber, creditCard, cCType
def transformToSorteable(data, args):
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
    arg = 7
    c = 100
    x = range(1, c)
    yBa = []
    yBs = []
    yWs = []
    userList = getData()
    data = transformData(userList)
    usersStack = addUserFromData(data, c)
    sortableData = transformToSorteable(usersStack, arg)
    for i in x:
        if arg == 1 or arg == 4 or arg == 5:
            hashData = makeHashList(sortableData[:i], 10)
            worseData = makeWorseHashList(sortableData[:i], 10)
        else:
            worseData = makeWorseHashList(sortableData[:i], 10)
            hashData = makeHashList(sortableData[:i], 36)
        BaHf, BsHf, WsHf = toPlotHf(hashData, worseData)
        yBa.append(BaHf)
        yBs.append(BsHf)
        yWs.append(WsHf)
    plt.figure(1)
    plt.suptitle('Busqueda Por transformación de llaves')
    plt.subplot(334)
    plt.plot(x, yBa, 'y-')
    plt.xlabel('Caso base')
    plt.subplot(335)
    plt.plot(x, yBs, 'g-')
    plt.xlabel('Mejor caso')
    plt.subplot(336)
    plt.plot(x, yWs, 'r-')
    plt.xlabel('Peor caso')
    plt.savefig('hash.png')
    plt.show()

if __name__ == '__main__':
    main()

