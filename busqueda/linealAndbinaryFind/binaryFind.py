# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 18:08:25 2020

@author: hrmha
"""

import random
from mergeSort import *
from bubbleSort import *

complexRecursive = 0
findedInRecursive = False
def iterativeBinaryFind(data, target):
    complexCount = 0                        # 2, un acceso a memoria y una asignación de valor a este
    start = 0                               # 2, creación de variable y asignación de valor
    end = len(data)                         # 4, creación de variable, asignación de valor, entrada a memoria para obetner data y operación para obtener su valor
    finded = False                          # 2, creación de variable y asignación de valor
    while start <= end and not finded:      # 6log_2(n), 3 entradas a memoria y 3 comparaciones, el logaritmo es por que irá disminuyendo por mitades
        middle = (start + end) // 2         #   4, creación de variable, asignación de valor y dos accesos a memoria log_2(n)
        complexCount += 1                   #   2, un acceso a memoria y una asignación a esta log_2(n)
        if middle < len(data):              #   4, dos accesos a memoria, una operación básica y una comparación log_2(n)
            if data[middle] == target:      #       5, 3 accesos a memoria, un acceso a memoria en un lugar específico del arreglo y una comparación log_2(n)
                finded = True               #           2, un acceso a memoria y un cambio de valor log_2(n)
                break                       #           1, operación básica log_2(n)
            else:                           #       0 log_2(n)
                if target < data[middle]:   #           5, 3 accesos a memoria, un acceso a memoria en un lugar específico del arreglo y una comparación log_2(n)
                    end = middle - 1        #               4, dos accesos a memoria, una asignación de valor y una operación básica log_2(n)
                else:                       #           0 log_2(n)
                    start = middle + 1      #               4, dos accesos a memoria, una asignación de valor y una operación básica log_2(n)
        else:                               #   0 log_2(n)
            break                           #       1, operación básica log_2(n)
    if finded:                              # 1,acceso a memoria
        return middle, complexCount         #   3, dos accesos a memoria y una operación básica
    else:                                   # 0
        return -1, complexCount             #   2, un accesos a memoria y una operación básica
#2+2+4+2+6(4+2+4+5+2+1+0+5+4+0+34+0)log_2( n )+1+3+0+2=14+6(61)log_2(n) = 14+366log_2(n)

def recursiveBinaryFind(data, target, start, end, complexCount = 0):                            # 7log(n), 5 accesos a memoria, una llamada a función, una operación básica
    global complexRecursive, findedInRecursive                                                  # 2, acceso a momoria global
    middle = (start + end) // 2                                                                 # 7, tres accesos a memoria, dos 
    if middle < len(data) and not findedInRecursive and ( middle > start  or middle < end):     # 14, 7 accesos a memoria, 6 comparaciones y 1 operación básica
        complexCount += 1                                                                       # 2, un acceso a memoria y una adición a esta
        complexRecursive += 1                                                                   # 2, un acceso a memoria y una adición a esta
        if data[middle] == target:                                                              # 4, 3 accesos a memoria y una comparación
            findedInRecursive = True                                                            # 2, 1 acceso a memoria y una asignación de valor a esta
            return middle                                                                       # 2, un acceso a memoria y una operación básica
        else:                                                                                   # 0
            if target < data[middle]:                                                           # 4, 3 accesos a memoria y una comparación
                return recursiveBinaryFind(data, target, start, (middle - 1), (complexCount))   # 7log(n), 5 accesos a memoria, una llamada a función, una operación básica
            else:                                                                               # 0
                return recursiveBinaryFind(data, target, (middle + 1), end, (complexCount))     # 7log(n), 5 accesos a memoria, una llamada a función, una operación básica
    else:                                                                                       # 0
        return -1                                                                               # 1, una operación básica
#2+7+14+2+2+4+2+2+0+7log(n)+0+7log(n)+0+1=36+14log(n)

def makeData(n):
    data = [0] * n
    for i in range(n):
        data[i] = i
    return data

def toPlotBf(data1):
    global complexRecursive, findedInRecursive
    iteracionesN, iteracionesM, iteracionesP, data = toPlotMs(data1)
    complexNumP, complexNumB, complexNumW = toPlotBs(data1)
    start = 0
    end = len(data)
    indexBaseIterative, baseComplexIterative = iterativeBinaryFind(data, data[random.randint(0, (len(data) - 1 ))])
    indexBestIterative, bestComplexIterative = iterativeBinaryFind(data, data[len(data) // 2])
    indexWorseIterative, worseComplexIterative = iterativeBinaryFind(data, (len(data)+1))
    indexBaseRecursive = recursiveBinaryFind(data, data[random.randint(0, (len(data) - 1 ))], start, end)
    baseComplexRecursive = complexRecursive
    complexRecursive = 0
    findedInRecursive = False
    indexBestRecursive = recursiveBinaryFind(data, data[len(data) // 2], start, end)
    bestComplexRecursive = complexRecursive
    complexRecursive = 0
    findedInRecursive = False
    indexWorseRecursive = recursiveBinaryFind(data, (len(data)+1), start, end)
    worseComplexRecursive = complexRecursive
    complexRecursive = 0
    findedInRecursive = False
    baseComplexIterativeQs = iteracionesN + baseComplexIterative
    bestComplexIterativeQs = iteracionesM + bestComplexIterative
    worseComplexIterativeQs = iteracionesP + worseComplexIterative
    baseComplexRecursiveQs = iteracionesN + baseComplexRecursive
    bestComplexRecursiveQs = iteracionesM + bestComplexRecursive
    worseComplexRecursiveQs = iteracionesP + worseComplexRecursive
    baseComplexIterativeBs = complexNumP + baseComplexIterative
    bestComplexIterativeBs = complexNumB + bestComplexIterative
    worseComplexIterativeBs = complexNumW + worseComplexIterative
    baseComplexRecursiveBs = complexNumP + baseComplexRecursive
    bestComplexRecursiveBs = complexNumB + bestComplexRecursive
    worseComplexRecursiveBs = complexNumW + worseComplexRecursive
    return baseComplexIterativeQs, bestComplexIterativeQs, worseComplexIterativeQs, baseComplexRecursiveQs, bestComplexRecursiveQs, worseComplexRecursiveQs,  baseComplexIterativeBs, bestComplexIterativeBs, worseComplexIterativeBs, baseComplexRecursiveBs, bestComplexRecursiveBs, worseComplexRecursiveBs

if __name__ == '__main__':
    for i in range(1, 20):
        data = makeData(i)
        print(toPlotBf(data))
    """
    print('recursive: ', iterativeBinaryFind(data, 20))
    print('iterative: ', recursiveBinaryFind(data, 20, 0, len(data)))
    """