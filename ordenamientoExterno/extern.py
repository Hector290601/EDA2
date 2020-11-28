import random
from pythonCode import *

count = 0
baseGlobal = 0
bestGlobal = 0
worseGlobal = 0

def getLen(data):
    global count
    count1 = 0
    for i in data:
        count += 1
        count1 += 1
    return count1

def extern(data):
    global count, baseGlobal, bestGlobal, worseGlobal
    dataLittle = []
    lenData = getLen(data)
    step = lenData // 10
    last = 0
    base = 0
    best = 0
    worse = 0
    for i in range(step, lenData + 1, step):
        count += 1
        baseNew, bestNew, worseNew, dataSorted = toPlot(data[last:i])
        base += baseNew
        best += bestNew
        worse += worseNew
        dataLittle.append(dataSorted)
        last = i
    baseGlobal += base
    bestGlobal += best
    worseGlobal += worse
    return dataLittle

def joinAll(data):
    global count, baseGlobal, bestGlobal, worseGlobal
    dataJoin = []
    littleData = []
    lenData = getLen(data[0])
    step = lenData // 10
    last = 0
    base = 0
    best = 0
    worse = 0
    for i in range(step, lenData + 1, step):
        count += 1
        firstData = []
        for j in data:
            firstData += j[last : i]
        littleData.append(firstData)
        writeToFile(firstData)
        last = i
    baseGlobal += base
    bestGlobal += best
    worseGlobal += worse
    for i in littleData:
        count += 1
        baseNew, bestNew, worseNew, dataSorted = toPlot(i)
        base += baseNew
        best += bestNew
        worse += worseNew
        dataJoin += dataSorted
    baseGlobal += base
    bestGlobal += best
    worseGlobal += worse
    return dataJoin

def toPlotExtern(data):
    global count, baseGlobal, bestGlobal, worseGlobal
    dataLittle = extern(data)
    joined = joinAll(dataLittle)
    baseGlobal += count
    bestGlobal += count
    worseGlobal += count
    return baseGlobal, bestGlobal, worseGlobal

def writeToFile(data):
    file = None
    try:
        file = open("dataTmp.csv", "w+", encoding='utf-8')
        file.write(str(data))
    except:
        print("No fué posible abrir el archivo")
    finally:
        if file:
            file.close

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

