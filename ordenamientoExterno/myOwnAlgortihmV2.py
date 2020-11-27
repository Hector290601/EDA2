#-*-coding:utf-8-*-
import random
import numpy as np

count = 0

def reshapeData(data, targets):
    for i in targets:
        data.pop(i)
    return data

def getLen(data):
    count = 0
    for i in data:
        count += 1
    return count

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
                last = lenDataSorted - last
            data.insert(last, num)
        elif num <= minNum:
            flag = True
            data.insert(first, num)
        elif not flag:
                middle = lenDataSorted // 2
                if lenDataSorted > middle:
                    if num > data[middle]:
                        return compareAndAppend(num, data, lenDataSorted, first = first, last = middle)
                    elif num < data[middle]:
                        return compareAndAppend(num, data, lenDataSorted, first = middle, last = last)
                    else:
                        return data
                else:
                    return data.insert(middle, num)
    return data

def algorithm(data):
    count = 0
    size = getLen(data)
    sizeSorted = 0
    dataSorted = []
    dataSorted.append(data[0])
    sizeSorted += 1
    count += size
    while size > 1:
        count += 1
        data = reshapeData(data, [0])
        dataSorted = compareAndAppend(data[0], dataSorted, sizeSorted)
        sizeSorted += 1
        size -= 1
    return dataSorted

def makeTestData(n):
    data = []
    for i in range(n):
        data.append(random.randint(0, (n**2)))
    return data

if __name__ == '__main__':
    data = makeTestData(10)
    sortedData = algorithm(data)
    #best = algorithm(sortedData)
    #worse = algorithm(best[::-1])

