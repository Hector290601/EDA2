# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:58:51 2020

@author: hrmha
"""

import random

def bubbleSort(data):
    k = 0
    n = len(data)
    for i in range(n - 1):
        i = i + 1
        for j in range(n - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                k += 1
            else:
                k += 1
    return data, k

def makeData(n):
    lista = [0]  * n
    for i in range(n):
        lista[i] = random.randint(0, 1000)
    return lista

def toPlotBs(n):
    arr = makeData(n)
    sortedData, complexNumP = bubbleSort(arr)
    sortedDataB, complexNumB = bubbleSort(sortedData)
    lstRvd = sortedDataB[::-1]
    sortedDataW, complexNumW = bubbleSort(lstRvd)
    return complexNumP, complexNumB, complexNumW

if __name__ == '__main__':
    m, b, w = toPlotBs(10)
    print("Middle: ", m, " Best: ", b, " Worse: ", w)