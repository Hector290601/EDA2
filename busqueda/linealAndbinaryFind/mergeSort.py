# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:58:51 2020

@author: hrmha
"""
import random

intI = 0
iteraciones = 0

def merge(left, right):
    global iteraciones
    iteraciones += 1
    if not len(left) or not len(right):
        return left or right
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result

def mergesort(lista):
    global intI
    intI += 1
    if len(lista) < 2:
        return lista
    middle = len(lista)//2
    left= mergesort(lista[:middle])
    right = mergesort(lista[middle:])
    return merge(left, right)

def makeData(n):
    lista = [0]  * n
    for i in range(n):
        lista[i] = random.randint(0, 100 * n)
    return lista

def toPlotMs(lst):
    global iteraciones, intI
    mrg = mergesort(lst)
    iteracionesN = iteraciones
    intI = 0
    iteraciones = 0
    mrgOrd = mergesort(mrg)
    iteracionesM = iteraciones
    intI = 0
    iteraciones = 0
    lstRvd = mrgOrd[::-1]
    intI = 0
    mrgOrd = mergesort(lstRvd)
    iteracionesP = iteraciones
    return iteracionesN, iteracionesM, iteracionesP, lst

if __name__ == "__main__":
    m, b, w = toPlotMs(10)
    print("Middle: ", m, " Best: ", b, " Worse: ", w)

