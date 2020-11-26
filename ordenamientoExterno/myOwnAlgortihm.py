#-*-coding:utf-8-*-
import random

def algorithm(data):
    count = 0
    flag = False
    dataSorted = [] * max(data)
    maxN = 0
    maxM = 0
    for i in data:
        istr = str(i)
        icode = istr[0] + str(len(istr)) + istr[1:]
        ic0 = int(icode[0])
        ic1 = int(icode[1])
        if ic0 >= maxN or ic1 >= maxN:
            if ic0 > ic1:
                maxN = ic0
            else:
                maxN = ic1
            maxN += 1
            for i in range(len(dataSorted), maxN):
                dataSorted.append([])
        #if type(dataSorted[ic0]) is int: 
        #        maxM = ic1
        #        maxM += 1
        #        for i in range(len(dataSorted), maxM):
        #            dataSorted[ic0].append([])
        #    dataSorted[ic0][ic1].append(i)
        #else:
        dataSorted[ic0].append(i)
    print(dataSorted)

def makeTestData(n):
    data = []
    for i in range(n):
        data.append(random.randint(0, (n*10)))
    return data

if __name__ == '__main__':
    print("Main")
    data = makeTestData(10)
    print(data)
    sortedData = algorithm(data)
    print(sortedData)
    #best = algorithm(sortedData)
    #worse = algorithm(best[::-1])

