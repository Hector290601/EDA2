#-*-coding:utf-8-*-
import random

def algorithm(data):
    count = 0
    flag = False
    dataSorted = [[], [], [], [], [], [], [], [], [], []]
    key = len(dataSorted)
    for i in data:
        count += 1
        mod = i % key
        print(type(dataSorted))
        dataSorted[mod].append(i)
        if len(dataSorted[mod]) > 1:
            for i in range(len(dataSorted[mod])):
                count += 1
                if i + 1 < len(dataSorted[mod]):
                    if dataSorted[mod][i] < dataSorted[mod][i+1]:
                        dataSorted[mod][i], dataSorted[mod][i+1] = dataSorted[mod][i+1], dataSorted[mod][i]
                        flag = False
                    flag = not flag
                    if flag:
                        break
    return dataSorted

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

