#-*-coding:utf-8-*-
import random

def getPriorityNumbers(data):
        middle = (len(data)//2)
        maxData = data[-1]
        minData = data[0]
        middleData = data[middle]
        return middle, maxData, minData, middleData

def compareAndAppend(num, maxNum, minNum, middleNum, middle, data):
    flag = False
    if num > maxNum:
        data.append(num)
        flag = True
    elif num < minNum:
        data.insert(0, num)
        flag = True
    elif num == middleNum:
        data.insert(middle + 1, num)
        flag = True
    elif not flag:
        newData = data[:middle]
        newMiddle, newMax, newMin, newMiddleData = getPriorityNumbers(newData)
        return compareAndAppend(num, newMax, newMin, newMiddleData, newData)
    elif not flag:
        newData = data[:middle]
        newMiddle, newMax, newMin, newMiddleData = getPriorityNumbers(newData)
        return compareAndAppend(num, newMax, newMin, newMiddleData, newData)
    return data

def algorithm(data):
    count = 0
    dataSorted = []
    dataSorted.append(data[0])
    for i in range(1, len(data)):
        count += 1
        middle, maxI, minI, middleI = getPriorityNumbers(data)
        dataSorted = compareAndAppend(i, maxI, minI, middleI, middle, dataSorted)
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

