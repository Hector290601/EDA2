# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 13:15:37 2020

@author: hrmha
"""

import random

iteraciones = 0

def heapify(data, n, i):
    global iteraciones
    iteraciones += 1
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and data[i] < data[left]:
        largest = left
    if right < n and data[largest] < data[right]:
        largest = right
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)
    return data

def heapSort(data):
    global iteraciones
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        iteraciones += 1
        heapify(data, n, i)
    for i in range(n-1, 0, -1):
        iteraciones += 1
        data[i], data[0] = data[0], data[i]
        sortedData = heapify(data, i, 0)
    return sortedData
    
def makeData(n):
    lista = [0]  * n
    for i in range(n):
        lista[i] = random.randint(0, 100 * n)
    return lista

def toPlotHs(n):
    global iteraciones, intI
    lst = makeData(n)
    mrg = heapSort(lst)
    iteracionesN = iteraciones
    print(iteracionesN)
    intI = 0
    iteraciones = 0
    mrgOrd = heapSort(mrg)
    iteracionesM = iteraciones
    intI = 0
    iteraciones = 0
    lstRvd = mrgOrd[::-1]
    intI = 0
    mrgOrdW = heapSort(lstRvd)
    iteracionesP = iteraciones
    return iteracionesN, iteracionesM, iteracionesP

if __name__ == '__main__':
    print(toPlotHs(5))