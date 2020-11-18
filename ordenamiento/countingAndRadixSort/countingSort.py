# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 03:05:07 2020

@author: hrmha
"""

import random

def countingSort(data):
    complexCount = 0                            # 2, acceso a memoria y asignación a esta
    mx = max(data)                              # 4, 2 accesos a memoria, una asignación y una operación básica
    number = len(data)                          # 4, 2 accesos a memoria, una asignación y una operación básica
    output = [0] * number                       # 5, dos accesos a memoria, una asignación y una operación
    temp = [0] * (mx + 1)                       # 5, dos accesos a memoria, una asignación y una operación
    for i in range(number):                     # 3n, dos accesos a memoria y una operación básica
        complexCount += 1                       # 2, un acceso a memoria y una operación básica (3n) = 6n
        temp[data[i]] = temp[data[i]] + 1       # 7, seis accesos a memoria y una operación básica (3n) = 21n
    temp [0] = temp[0]-1                        # 3, dos accesos a memoria y una operación básica
    for i in range(1, mx+1):                    # 3m, dos accesos a memoria y una operación básica
        complexCount += 1                       # 2, un acceso a memoria y una operación básica (3m) = 6m
        temp[i] = temp[i] + temp[i-1]           # 10, seis accesos a memoria y cuatro operaciones básicas (3m) = 30m
    for i in range(number-1, -1, -1):           # 5n, dos accesos a memoria y tres operaciones
        complexCount += 1                       # 2, un acceso a memoria y una operación básica (5n) = 10n
        output[temp[data[i]]] = data[i]         # 7, 6 accesos a memoria y una asignación (5n) = 35n
        temp[data[i]] = temp[data[i]] - 1       # 7, 6 accesos a memoria y una adignación (5n) = 35n
    return output, complexCount                 # 3, dos accesos a memoria y una operación básica
#2+4+4+5+5+(3n+6n+21n)+3+(3m+6m+30m)+(5n+10n+35n+35n)+3 = 26+30n+39m+85n = 26+39m+115n

def makeData(n):
    lista = [0]  * n
    for i in range(n):
        lista[i] = random.randint(0, 1)
    return lista

def toPlotCs(data):
    lst, complexBase = countingSort(data)
    lst, complexBest = countingSort(lst)
    lst, complexWorse = countingSort(lst[::-1])
    return complexBase, complexBest, complexWorse

if __name__ == '__main__':
    data = makeData(10)
    print(toPlotCs(data))
