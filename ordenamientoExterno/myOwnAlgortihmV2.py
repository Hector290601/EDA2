#-*-coding:utf-8-*-
import random
import numpy as np

def reshapeData(data, targets):
    for i in targets:
        data.pop(i)
    return data

def getLen(data):
    count = 0
    for i in data:
        count += 1
    return count

def compareAndAppend(num, data, unknow = 0, dataOrg = []):
    dataOrg = data
    flag = False
    if getLen(data) > 1:
        maxNum = data[-1]
        minNum = data[0]
        if num > maxNum:
            unknow += 1
            flag = True
            return getLen(data)
        elif num < minNum:
            unknow -= 1
            flag = True
            return 0
        elif not flag:
                middle = getLen(data)
                if num > middle:
                    unknow += 1
                    return compareAndAppend(num, data[middle:-1], unknow, dataOrg)
                elif num < middle:
                    unknow -= 1
                    return compareAndAppend(num, data[0:middle], unknow, dataOrg)
                else:
                    return middle
    elif getLen(data) == 1:
        if dataOrg[unknow] > num:
            return compareAndAppend(num, dataOrg[:unknow], unknow)
        elif dataOrg[unknow] < num:
            return compareAndAppend(num, dataOrg[:unknow], unknow)
        elif dataOrg[unknow] == num:
            return unknow
    else:
        return 0

def compare(data):
    for i in range(len(data)):
        if data[i] > data[i+1]:
            return True

def algorithm(data):
    count = 0
    dataSorted = []
    dataSorted.append(data[0])
    while getLen(data) > 1:
        count += 1 + getLen(data)
        data = reshapeData(data, [0])
        pos = compareAndAppend(data[0], dataSorted)
        dataSorted.insert(pos, data[0])
    print(count)
    print(dataSorted)

def makeTestData(n):
    data = []
    for i in range(n):
        data.append(random.randint(0, (n**2)))
    return data

if __name__ == '__main__':
    print("Main")
    data = makeTestData(10)
    #data = [8529148895, 4177311179, 7851008984, 6621525306, 5605829259, 6197661161, 6971668060, 6621506146, 9222912901, 1475949613]
    print(data)
    sortedData = algorithm(data)
    print(sortedData)
    #best = algorithm(sortedData)
    #worse = algorithm(best[::-1])

