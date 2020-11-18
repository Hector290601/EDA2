# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:02:36 2020

@author: hrmha
"""

import random
import math

"""
def countingSort(data, exp1):
    complexCount = 0
    mx = max(data)
    number = len(data)
    output = [0] * number
    temp = [0] * (mx + 1)
    for i in range(number):
        complexCount += 1
        temp[data[i]] = temp[data[i]] +1
    temp[0] = temp[0] - 1
    for i in range(1, mx + 1):
        complexCount += 1
        temp[i] = temp[i] + temp[i-1]
    for i in range(number - 1, -1, -1):
        complexCount += 1
        output[temp[data[i]]] = data[i]
        temp[data[i]] = temp[data[i]] - 1
    return output, complexCount


def countingSort(data, exp1):
    cont = 0
    n = len(data)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        cont += 1
        index = (data[i] / exp1)
        count[int(index % 10)] += 1
    for i in range(1, 10):
        cont += 1
        count[i] += count[i-1]
    i = n-1
    while i >= 0:
        cont += 1
        index = data[i] / exp1
        output[count[int(index%10)] - 1] = data[i]
        count[int(index % 10)] -= 1
        i -= 1
    return output, cont

def radixSort(data):
    complexCount = 0
    mx = max(data)
    exp = 1
    while mx / exp > 0:
        complexCount += 1
        data, cmplx = countingSort(data, exp)
        exp *= 10
        complexCount += cmplx
    return data, complexCount
"""

def radixSort(data):
    complexCount = 0                                # 2, creación de memoria y asignación de valor
    radix = 10                                      # 2, creación de memoria y asignación de valor
    placement = 1                                   # 2, creación de memoria y asignación de valor
    maxDigit = max(data)                            # 3, un acceso a memoria, una creación de memoria y una operación básica
    while placement < maxDigit:                     # 2m-2, dos accesos a memoria 2(m-1)    Es constante por que es la base
        complexCount += 1                           #   2, un acceso a memoria y una operación básica (2m-2) = 4m-4
        buckets = [list() for _ in range(radix)]    #   5, 4 accesos a memoria y una asignación (9)(2m-2) = 90m-90
        for i in data:                              #   2n, dos accesos a memoria (2m-2) = 4mn-4n
            complexCount += 1                       #       2, dos accesos a memoria (4mn-4n) = 8mn-8n
            tmp = int((i/placement) % radix)        #       8, cuatro accesos a memoria, 3 operaciones básicas y una asignación (4mn-4n) = 32mn-32n
            buckets[tmp].append(i)                  #       5, cuatro accesos a memoria y una asignación (4mn-4n) = 20mn-20n
        a = 0                                       #   2, creación de memoria y una asignacion (2m-2) = 4m-4
        for b in range(radix):                      #   3, dos accesos a memoria y una operación básica (2m-2) = 6m-6
            complexCount += 1                       #       2, un acceso a memoria y una operación básica (6m-6) = 12m-12
            buck = buckets[b]                       #       4, tres accesos a memoria y una asignación (6m-6) = 24m-24
            for i in buck:                          #       2, dos accesos a memoria (6m-6) = 12m-12
                data[a] = i                         #           4, tres accesos a memoria y una signación (12m-12) = 48m-48
                a += 1                              #           2, un acceso a memori a y una asignación (12m-12) = 24m-24
        placement *= radix                          #       3, dos accesos a memoria y una asignación (6m-6) = 18m-18
    return data, complexCount                       # 3, dos accesos a memoria y una operación básica
#2+2+2+3+2m-2+4m-4+90m-90+4mn-4n+8mn-8n+32mn-32n+20mn-20n+4m-4+6m-6+12m-12+24m-24+12m-12+48m-48+24m-24+18m-18+3 = 241m-64n+64mn-49

def makeData(n):
    lista = [0]  * n
    for i in range(n):
        lista[i] = random.randint(0, 100)
    return lista

def toPlotRs(data):
    lst, complexBase = radixSort(data)
    lst, complexBest = radixSort(lst)
    lst, complexWorse = radixSort(lst[::-1])
    return complexBase, complexBest, complexWorse

if __name__ == '__main__':
    for i in range(1, 2):
        print(toPlotRs(makeData(i)))
