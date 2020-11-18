# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:25:45 2020

@author: hrmha
"""
import random

complexRecursive = 0

def iterativeLinealFind(data, target):
    complexIterative = 0                    # 2, un acceso a memoria y una asignación a esa memoria
    finded = False                          # 2, un acceso a memoria y una adignación a esa memoria
    for i in range(len(data)):              # 5 * (n-1), dos accesos a memoria y tres operaciones básicas
        if not finded:                      #   2, un acceso a memoria y una comparación (n-1)
            complexIterative += 1           #       2, un acceso a memoria y un aumento a esta (n-1)
            if data[i] == target:           #       4, tres accesos a memoria y una comparación (n-1)
                finded = True               #           2, un acceso a memoria y una asignación a esta (n-1)
                return i, complexIterative  #           3, dos accesos a memoria y una operación básica  (n-1)
        else:                               #   0 (n-1)
            break                           #       1, una operación básica (n-1)
    return -1, complexIterative             # 2, un acceso a memoria y una operación básica
#2+2+5((n-1)(2+3+4+2+3))+0+1+2=7+5((n-1)(14))=7+5((14n-14))=7+70n-70=70n-63

def recursiveLinealFind(data, target, i = 0):
    global complexRecursive                                     # 1, acceso a memoria global
    complexRecursive += 1                                       # 2, acceso a memoria y aumento a esta
    if i < (len(data)):                                         # 4, dos accesos a memoria, una operación básica y una comparación
        if data[i] == target:                                   # 4, tres accesos a memoria y una comparación
            return i                                            # 2, un acceso a memoria y una operación básica
        else:                                                   # 0
            return recursiveLinealFind(data, target, i + 1)     # 4 (n-1), 3 accesos a memoria, una resta y una llamada recursiva
    else:                                                       # 0
        return -1                                               # 1, una operación básica
#1+2+4+4+2+0+4(n-1)+0+1=14+4n-4=4n+10

def makeData(n):
    lista = [0]  * n
    for i in range(n):
        lista[i] = i
    return lista

def toPlotLf(data):
    global complexRecursive
    indexBaseIterative, baseComplexIterative = iterativeLinealFind(data, data[random.randint(0, (len(data) - 1 ))])
    indexBestIterative, bestComplexIterative = iterativeLinealFind(data, data[0])
    indexWorseIterative, worseComplexIterative = iterativeLinealFind(data, (len(data)+1))
    indexBaseRecursive = recursiveLinealFind(data, data[random.randint(0, (len(data) - 1 ))])
    baseComplexRecursive  = complexRecursive
    complexRecursive = 0
    indexBestRecursive = recursiveLinealFind(data, data[0])
    bestComplexRecursive = complexRecursive
    complexRecursive = 0
    indexWorseRecursive = recursiveLinealFind(data, (len(data)+1))
    worseComplexRecursive = complexRecursive
    complexRecursive = 0
    return baseComplexIterative, bestComplexIterative, worseComplexIterative, baseComplexRecursive, bestComplexRecursive, worseComplexRecursive

if __name__ == '__main__':
    for i in range(1, 20):
        data = makeData(i)
        print('i: ', i)
        print(toPlotLf(data))
    #print(recursiveLinealFind(data, (random.randint(0, (len(data)-1)))))
    #print(complexRecursive)
