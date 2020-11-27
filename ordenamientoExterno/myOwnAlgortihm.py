#-*-coding:utf-8-*-
import random

def makeCode(num):
    numStr = str(num)
    numCode = [numStr[0]] + [str(len(numStr))] + [numStr[1:]]
    nc0 = int(numCode[0])
    nc1 = int(numCode[1])
    print(numCode, '=>', nc0, nc1)
    return numCode, nc0, nc1

def resize(newSize):
    data = []
    for i in range(0, newSize):
        data.append([])
    return data

def rankNumber(nc0, nc1, data):
    if nc1 == 1:
        return nc0, 2
    if len(data[nc0]) > len(data[nc1]):
        return nc0, 0
    elif len(data[nc0]) < len(data[nc1]):
        return nc1, 1
    else:
        return nc0, 0

def enlist():
    pass

def algorithm(data):
    count = 0
    flag = False
    dataSorted = []
    maxN = 0
    maxM = 0
    for i in range(0, len(data)):
        icode, ic0, ic1 = makeCode(data[i])
        pos, rank = rankNumber(ic0, ic1, dataSorted)
        """if rank = 0:
        elif rank = 1:
        elif rank = 2:
        else:
            print('Error inesperado')
        """
        print(data[i], '=>', pos, rank)

def makeTestData(n):
    data = []
    for i in range(n):
        data.append(random.randint(0, (n**2)))
    return data

if __name__ == '__main__':
    print("Main")
    data = makeTestData(100)
    #data = [8529148895, 4177311179, 7851008984, 6621525306, 5605829259, 6197661161, 6971668060, 6621506146, 9222912901, 1475949613]
    print(data)
    sortedData = algorithm(data)
    print(sortedData)
    #best = algorithm(sortedData)
    #worse = algorithm(best[::-1])

