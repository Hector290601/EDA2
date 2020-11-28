#-*-coding:utf-8-*-
import random
import numpy as np
import sys

sys.setrecursionlimit(100)

count = 0

def reshapeData(data, targets):
    for i in targets:
        data.pop(i)
    return data

def getLen(data):
    global count
    count2 = 0
    for i in data:
        if type(i) is list:
            for j in i:
                count += 1
                count2 += 1
        else:
            count += 1
            count2 += 1
    return count2

def compareAndAppend(num, data, lenDataSorted, first = 0, last = 1):
    flag = False
    if lenDataSorted > 0:
        maxNum = data[-last]
        minNum = data[first]
        if num >= maxNum:
            flag = True
            if last == 1:
                last = lenDataSorted
            else:
                last = last - lenDataSorted + 1
            data.insert(last, num)
        elif num <= minNum:
            flag = True
            data.insert(first, num)
        elif not flag:
                middle = lenDataSorted // 2
                if lenDataSorted > middle:
                    if num > data[middle]:
                        return compareAndAppend(num, data, lenDataSorted, first = (middle + first) if first != 0 else middle, last = middle)
                    elif num < data[middle - 1]:
                        return compareAndAppend(num, data, lenDataSorted, first = first, last = (middle - last) if last != 1 else middle)
                    elif num > data[middle-1]:
                        data.insert(middle, num)
                    elif num > data[middle]:
                        data.insert(middle + 1)
                    else:
                        data.insert(middle, num)
                        flag = True
                else:
                    flag = true
                    data.insert(middle, num)
    return data

def sort(data, size):
    global count
    if size >= 0:
        sizeSorted = 0
        dataSorted = []
        dataSorted.append(data[0])
        sizeSorted += 1
        while size > 1:
            count += 1
            data.pop(0)
            dataSorted = compareAndAppend(data[0], dataSorted, sizeSorted)
            sizeSorted += 1
            size -= 1
        return dataSorted

def separe(data, size):
    global count
    separedData = []
    mod = (size // 5)
    for i in range(mod):
        separedData.append([])
    for i in data:
        count += 1
        if type(i) is list:
            for j in i:
                separedData[j%mod].append(j)
        else:
            separedData[i%mod].append(i)
    return separedData

def algorithm(data):
    size = getLen(data)
    separedData = separe(data, size)
    tmp = []
    sortedData = []
    for i in separedData:
        tmp.append(sort(i, getLen(i)))
    for i in tmp:
        sortedData.append(i)
    return sortedData

def toPlot(data):
    global count
    sortedData = algorithm(data)
    base = count
    count = 0
    sortedData = algorithm(sortedData)
    best = count
    count = 0
    algorithm(sortedData[::-1])
    worse = count
    count = 0
    return base, best, worse

def makeTestData(n):
    data = []
    for i in range(n):
        data.append(random.randint(0, (n**2)))
    return data

if __name__ == '__main__':
    data = makeTestData(100)
    count = 0
    print(toPlot(data))
