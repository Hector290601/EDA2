#-*-coding:utf-8-*-
import random

count = 0
lenData = 0

def algorithm(data):
    count = 0                                                   # 2, creación de memoria y asignación de valor
    flag = True                                                 # 2, creación de memoria y asignación de valor
    while flag:                                                 # 2m, una entrada a memoria y una comparación
        count += 1                                              # 2, un acceso a memoriay una asignación de valor (2m) = 4m
        for i in range(len(data) -3):                           # 5n, 4 accesos a memoria y una operación básica (2m) = 10nm
            count += 1                                          # 2, acceso a memoria y una asignación de valor (10mn) = 20mn
            if data[i] > data[i+1] :                            # 6, 4 accesos a memoria y dos operaciones básicas (10mn) = 60mn
                data[i], data[i+1] = data[i+1], data[i]         # 12, 8 accesos a memoria y cuatro operaciones básicas (10mn) = 120mn
                flag = False                                    # 2, un acceso a memria y una asignación de valor (10mn) = 20mn
            if data[i] > data[i+2] :                            # 6, 4 accesos a memoria y dos operaciones básicas (10mn) = 60mn
                data[i], data[i+2] = data[i+2], data[i]         # 12, 8 accesos a memoria y cuatro operaciones básicas (10mn) = 120mn
                flag = False                                    # 2, un acceso a memria y una asignación de valor (10mn) = 20mn
            if data[i] > data[i+3] :                            # 6, 4 accesos a memoria y dos operaciones básicas (10mn) = 60mn
                data[i], data[i+3] = data[i+3], data[i]         # 12, 8 accesos a memoria y cuatro operaciones básicas (10mn) = 120mn
                flag = False                                    # 2, un acceso a memria y una asignación de valor (10mn) = 20mn
            if data[i + 1] > data[i+2] :                        # 6, 4 accesos a memoria y dos operaciones básicas (10mn) = 60mn
                data[i+1], data[i+2] = data[i+2], data[i+1]     # 12, 8 accesos a memoria y cuatro operaciones básicas (10mn) = 120mn
                flag = False                                    # 2, un acceso a memria y una asignación de valor (10mn) = 20mn
            if data[i + 1] > data[i+3] :                        # 6, 4 accesos a memoria y dos operaciones básicas (10mn) = 60mn
                data[i+1], data[i+3] = data[i+3], data[i+1]     # 12, 8 accesos a memoria y cuatro operaciones básicas (10mn) = 120mn
                flag = False                                    # 2, un acceso a memria y una asignación de valor (10mn) = 20mn
            if data[i + 2] > data[i+3] :                        # 6, 4 accesos a memoria y dos operaciones básicas (10mn) = 60mn
                data[i+2], data[i+3] = data[i+3], data[i+2]     # 12, 8 accesos a memoria y cuatro operaciones básicas (10mn) = 120mn
                flag = False                                    # 2, un acceso a memria y una asignación de valor (10mn) = 20mn
        flag = not flag                                         # 3, un acceso a memria, una asignación de valor y una operación básica (2m) = 6m
    return data, count                                          # 3, dos accesos a memoria y una operación básica

# 2+2+2m+4m+10mn+(6*(20mn+60mn+120mn))+6m+3 = 12m+1210mn+7

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

