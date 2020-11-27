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
    """
    elif getLen(data) == 1:
        if dataOrg[unknow] > num:
            return compareAndAppend(num, dataOrg[:unknow], unknow)
        elif dataOrg[unknow] < num:
            return compareAndAppend(num, dataOrg[:unknow], unknow)
        elif dataOrg[unknow] == num:
            return unknow
    else:
        return 0
    """

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
        print(dataSorted)
    return dataSorted

def makeTestData(n):
    data = []
    for i in range(n):
        data.append(random.randint(0, (n**2)))
    return data

if __name__ == '__main__':
    print("Main")
    #data = [1, 2, 0, 6]
    #data = [14, 6, 16, 8]
    #data = [13, 8, 6, 12]
    #data = [8, 4, 6]
    data = makeTestData(10)
    #data = [8529148895, 4177311179, 7851008984, 6621525306, 5605829259, 6197661161, 6971668060, 6621506146, 9222912901, 1475949613]
    print(data)
    sortedData = algorithm(data)
    #print(sortedData)
    #best = algorithm(sortedData)
    #worse = algorithm(best[::-1])

