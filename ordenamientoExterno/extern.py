import random
from pythonCode import *

count = 0                                                               # 2, un acceso a memoria y una asignación de valor
baseGlobal = 0                                                          # 2, un acceso a memoria y una asignación de valor
bestGlobal = 0                                                          # 2, un acceso a memoria y una asignación de valor
worseGlobal = 0                                                         # 2, un acceso a memoria y una asignación de valor

# 2+2+2+2 = 8

def getLen(data):
    global count                                                        # 1, un acceso a memoria
    count1 = 0                                                          # 2, un acceso a memoria y una asignación de valor
    for i in data:                                                      # 2n, un acceso a memoria y una asignación de valor
        count += 1                                                      # 2, un acceso a memoria y una asignación de valor (2n) = 4n
        count1 += 1                                                     # 2, un acceso a memoria y una asignación de valor (2n) = 4n
    return count1                                                       # 2, un acceso a memoria y una operación básica

# 1+2+4n+4n+2 = 5+8n

def extern(data):
    global count, baseGlobal, bestGlobal, worseGlobal                   # 4, cuatro accesos a memoria
    file = None                                                         # 2, un acceso a memoria y una asignación de valor
    file = open("dataTmpA.csv", "w+", encoding='utf-8')                 # 2, un acceso a memoria y una asignación de valor
    dataLittle = []                                                     # 2, un acceso a memoria y una asignación de valor
    lenData = getLen(data)                                              # 5+8n
    step = lenData // 10                                                # 2, un acceso a memoria y una asignación de valor
    last = 0                                                            # 2, un acceso a memoria y una asignación de valor
    base = 0                                                            # 2, un acceso a memoria y una asignación de valor
    best = 0                                                            # 2, un acceso a memoria y una asignación de valor
    worse = 0                                                           # 2, un acceso a memoria y una asignación de valor
    for i in range(step, lenData + 1, step):                            # 6q, 4 accesos a memoria y 3 operaciones básicas
        count += 1                                                      # 2, un acceso a memoria y una asignación de valor (6q) = 12q
        baseNew, bestNew, worseNew, dataSorted = toPlot(data[last:i])   # 12m+1210mn+7 (6q) = 72mq+12600mnq+42q
        base += baseNew                                                 # 2, un acceso a memoria y una asignación de valor (6q) = 12q
        best += bestNew                                                 # 2, un acceso a memoria y una asignación de valor (6q) = 12q
        worse += worseNew                                               # 2, un acceso a memoria y una asignación de valor (6q) = 12q
        dataLittle.append(dataSorted)                                   # 3, dos accesos a memoria y una operación básica (6q) = 18q
        writeToFile(dataSorted, 'little', file)                         # 34t + 10 (6q) = 204qt + 60q
        last = i                                                        # 2, un acceso a memoria y una asignación de valor (6m) = 12m
    if file:                                                            # 2, un acceso a memoria y una operación básica
        file.close                                                      # 2, un acceso a memoria y una asignación de valor
    return dataLittle, baseNew, bestNew, worseNew                       # 5, cuatro accesos a memoria y una operación básica
#4+2+2+2+5+8n+2+2+2+2+2+6q+12q+72mq+12600mnq+42q+12q+12q+12q+18q+204qt+60q+12m+2+2+2+5 = 12m+8n+173q+12600mnq+72mq+204qt+38

def joinAll(data):
    global count, baseGlobal, bestGlobal, worseGlobal                   # 4, cuatro accesos a memoria
    dataJoin = []                                                       # 2, un acceso a memoria y una asignación de valor
    littleData = []                                                     # 2, un acceso a memoria y una asignación de valor
    lenData = getLen(data[0])                                           # 5+8n
    step = lenData // 10                                                # 2, un acceso a memoria y una asignación de valor
    last = 0                                                            # 2, un acceso a memoria y una asignación de valor
    base = 0                                                            # 2, un acceso a memoria y una asignación de valor
    best = 0                                                            # 2, un acceso a memoria y una asignación de valor
    worse = 0                                                           # 2, un acceso a memoria y una asignación de valor
    file = None                                                         # 2, un acceso a memoria y una asignación de valor
    file = open("dataTmpB.csv", "w+", encoding='utf-8')                 # 2, un acceso a memoria y una asignación de valor
    for i in range(step, lenData + 1, step):                            # 6q, 4 accesos a memoria y 3 operaciones básicas
        count += 1                                                      # 2, un acceso a memoria y una asignación de valor (6q) = 12q
        firstData = []                                                  # 2, un acceso a memoria y una asignación de valor (6q) = 12q
        for j in data:                                                  # 3r, dos accesos a memoria y una operación básica (6q) = 12qr
            firstData += j[last : i]                                    # 7, 4 accesos a memoria y 3 operaciones (12qr) = 84qr
        littleData.append(firstData)                                    # 3, dos accesos a memoria y una operación b+asica (6q)
        writeToFile(firstData, 'join', file)                            # 6 (6q) = 36q
        last = i                                                        # 2, un acceso a memoria y una asignación de valor (6q) = 12q
    if file:                                                            # 2, un acceso a memoria y una operación básica
        file.close                                                      # 2, un acceso a memoria y una asignación de valor
    j = 0                                                               # 2, un acceso a memoria y una asignación de valor
    file = None                                                         # 2, un acceso a memoria y una asignación de valor
    file = open("dataTmpA.csv", "r+", encoding='utf-8')                 # 2, un acceso a memoria y una asignación de valor
    for i in littleData:                                                # 3s, dos accesos a memoria y una operación básica
        dataFromFile = readFromFile(j, file)                            # 34t+10 (3s) = 102st+30s
        j+= 1                                                           # 2, un acceso a memoria y una asignación de valor (3s) = 6s
        count += 1                                                      # 2, un acceso a memoria y una asignación de valor (3s) = 6s
        baseNew, bestNew, worseNew, dataSorted = toPlot(dataFromFile)   # 12m+1210mn+7 (3s) = 36ms+3630mns+7
        dataJoin += dataSorted                                          # 2, un acceso a memoria y una asignación de valor (3s) = 6s
    if file:                                                            # 2, un acceso a memoria y una operación básica
        file.close                                                      # 2, un acceso a memoria y una asignación de valor
    file = None                                                         # 2, un acceso a memoria y una asignación de valor
    file = open("sorted.csv", "w+", encoding='utf-8')                   # 2, un acceso a memoria y una asignación de valor
    writeToFile(dataJoin, 'sorted', file)                               # 6
    return dataJoin                                                     # 2, un acceso a memoria y una operación básica
# 4+2+2+5+8n+2+2+2+2+2+2+2+6q+12q+12q+12qr+84qr+6q+36q+12q+2+2+2+2+2+2+102st+30s+6s+6s+36ms+3630mns+7+6s+2+2+2+2+6+2 = 48s+8n+84q+3630mns+36ms+96qr+102st+62

def toPlotExtern(data):
    global count, baseGlobal, bestGlobal, worseGlobal                   # 4, cuatro accesos a memoria
    count = 0                                                           # 2, un acceso a memoria y una asignación de valor
    dataLittle, bsN, bN, wN = extern(data)                              # 12m+8n+173q+12600mnq+72mq+204qt+38
    joined = joinAll(dataLittle)                                        # 48s+8n+84q+3630mns+36ms+96qr+102st+62
    baseGlobal += count                                                 # 2, un acceso a memoria y una asignación de valor
    count = 0                                                           # 2, un acceso a memoria y una asignación de valor
    dataLittle, _, _, _ = extern(data)                                  # 12m+8n+173q+12600mnq+72mq+204qt+38
    joined = joinAll(dataLittle)                                        # 48s+8n+84q+3630mns+36ms+96qr+102st+62
    bestGlobal += count                                                 # 2, un acceso a memoria y una asignación de valor
    count = 0                                                           # 2, un acceso a memoria y una asignación de valor
    dataLittle, _, _, _ = extern(data)                                  # 12m+8n+173q+12600mnq+72mq+204qt+38
    joined = joinAll(dataLittle)                                        # 48s+8n+84q+3630mns+36ms+96qr+102st+62
    worseGlobal += count                                                # 2, un acceso a memoria y una asignación de valor
    return baseGlobal, bestGlobal, worseGlobal                          # 4, tres accesos a memoria y una operación básica
#6+12m+8n+173q+12600mnq+72mq+204qt+38+48s+8n+84q+3630mns+36ms+96qr+102st+62+4+12m+8n+173q+12600mnq+72mq+204qt+38+48s+8n+84q+3630mns+36ms+96qr+102st+62+4++12m+8n+173q+12600mnq+72mq+204qt+38+48s+8n+84q+3630mns+36ms+96qr+102st+62+6 = 144s+36m+48n+771q+288qr+37800+10890mns+216mq+108ms+612qt+306st+324

def writeToFile(data, typeData, file):
    strData = str(data)                                                 # 2, un acceso a memoria y una asignación de valor
    strData = strData[1:-2]                                             # 2, un acceso a memoria y una asignación de valor
    file.write(strData + '\n')                                          # 2, un acceso a memoria y una asignación de valor
# 2+2+2 = 6

def readFromFile(n, file):
    cnt = 0                                                             # 2, un acceso a memoria y una asignación de valor
    line = 'a'                                                          # 2, un acceso a memoria y una asignación de valor
    toSort = []                                                         # 2, un acceso a memoria y una asignación de valor
    char = ''                                                           # 2, un acceso a memoria y una asignación de valor
    while line != '':                                                   # 2t, un acceso a memoria y una operación básica
        ant = 0                                                         # 2, un acceso a memoria y una asignación de valor (2t) = 4t
        i = 0                                                           # 2, un acceso a memoria y una asignación de valor (2t) = 4t
        line = file.readline()                                          # 2, un acceso a memoria y una asignación de valor (2t) = 4t
        if line != '':                                                  # 2, un acceso a memoria y una operación básica (2t) = 4t
            numbers = line.split(sep=',')                               # 3, dos accesos a memoria y una operación básica (2t) = 6t
            num = numbers[n]                                            # 2, un acceso a memoria y una asignación de valor (2t) = 4t
            toSort.append(num)                                          # 3, dos accesos a memoria y una operación básica (2t) = 6t
    return toSort                                                       # 2, un acceso a memoria y una operación básica
# 2+2+2+2+2t+4t+4t+4t+4t+6t+4t+6t+2 = 34t + 10


def makeTestData(n):
    data = []
    for i in range(n):
        data.append(random.randint(0, (n*10)))
    return data

if __name__ == '__main__':
    data = makeTestData(100)
    toPlotExtern(data)
    print(baseGlobal)
    print(bestGlobal)
    print(worseGlobal)
