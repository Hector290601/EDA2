#-*-coding:utf-8-*-
import random

count = 0
lenData = 0

def algorithm(data):
    count = 0
    flag = True
    while flag:
        count += 1
        for i in range(len(data) -3):
            count += 1
            if data[i] > data[i+1] :
                data[i], data[i+1] = data[i+1], data[i]
                flag = False
            if data[i] > data[i+2] :
                data[i], data[i+2] = data[i+2], data[i]
                flag = False
            if data[i] > data[i+3] :
                data[i], data[i+3] = data[i+3], data[i]
                flag = False
            if data[i + 1] > data[i+2] :
                data[i+1], data[i+2] = data[i+2], data[i+1]
                flag = False
            if data[i + 1] > data[i+3] :
                data[i+1], data[i+3] = data[i+3], data[i+1]
                flag = False
            if data[i + 2] > data[i+3] :
                data[i+2], data[i+3] = data[i+3], data[i+2]
                flag = False
        flag = not flag
    return data, count

def toPlot(data):
    sortedData, base = algorithm(data)
    bestData, best = algorithm(sortedData)
    worseData, worse = algorithm(bestData[::-1])
    return base, best, worse, sortedData

def makeTestData(n):
    data = []
    for i in range(n):
        data.append(random.randint(0, (n*10)))
    return data

if __name__ == '__main__':
    print("Main")
    data = makeTestData(100)
    toPlot(data)

