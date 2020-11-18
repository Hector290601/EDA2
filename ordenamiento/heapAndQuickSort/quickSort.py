# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 12:28:14 2020

@author: hrmha
"""

import random

counter = 0

def dividir(A, l, h):
    global counter #1
    index = (l - 1) #4
    pivote = A[h] #4
    for j in range(l, h): #
        counter += 1
        if A[j] <= pivote:
            index +=1
            A[index], A[j] = A[j], A[index]
    A[index+1], A[h] = A[h], A[index+1]
    return (index+1)

def quickSort(A, l, h):
    global counter
    counter += 1
    if len(A) < 2:
        return A
    else:
        if l < h:
            pIndex = dividir(A, l, h)
            quickSort(A, l, pIndex-1)
            quickSort(A, pIndex +1, h)
    return A
        
    
def makeData(n):
    data = []
    for i in range(n):
        data.append(random.randint(0, 100))
    return data

def toPlotQs(n):
    global counter
    lst = makeData(n)
    counter = 0
    mrg = quickSort(lst, 0, n-1)
    iteracionesN = counter
    counter = 0
    mrgOrd = quickSort(mrg, 0, n-1)
    iteracionesM = counter
    lstRvd = mrgOrd[::-1]
    counter = 0
    mrgInv = quickSort(lstRvd, 0, n-1)
    iteracionesP = counter
    return iteracionesN, iteracionesM, iteracionesP


if __name__ == '__main__':
    for i in range(10000):
        cN, cM, cW = toPlotQs(i)
        print("cN: ", cN, "cM: ", cM, "cW: ", cW)