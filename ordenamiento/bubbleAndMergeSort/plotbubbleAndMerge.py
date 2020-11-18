# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:37:31 2020

@author: hrmha
"""

import matplotlib.pyplot as plt
import threading
import concurrent.futures
from mergeSort import *
from bubbleSort import *

def plot(n):
    global ranged
    with concurrent.futures.ThreadPoolExecutor() as executor:
        mergeSort = executor.submit(toPlotMs, n)
        bubbleSort = executor.submit(toPlotBs, n)
        PMs, BMs, WMs = mergeSort.result()
        PBs, BBs, WBs = bubbleSort.result()
    return PMs, BMs, WMs, PBs, BBs, WBs

if __name__ == '__main__':
    print("Making Plot")
    PMsArr = []
    BMsArr = []
    WMsArr = []
    PBsArr = []
    BBsArr = []
    WBsArr = []
    ranged = range(1, 100)
    for i in ranged:
        PMs, BMs, WMs, PBs, BBs, WBs = plot(i)
        #print("Promedio MergeSort: ", PMs, " Mejor MergeSort: ", BMs, " Peor MergeSort: ", WMs)
        #print("Promedio BubbleSort: ", PBs, " Mejor BubbleSort: ", BBs, " Peor BubbleSort: ", WBs)        
        print(i)
        PMsArr.append(PMs)
        BMsArr.append(BMs)
        WMsArr.append(WMs)
        PBsArr.append(PBs)
        BBsArr.append(BBs)
        WBsArr.append(WBs)
    fig1, ax1 = plt.subplots()
    plt.subplot(211)
    plt.ylabel("Iteraciones de la función")
    ax1.set_aspect('equal')
    plt.plot(ranged, PMsArr, 'r--', ranged, BMsArr, 'go', ranged, WMsArr, 'b--')
    plt.grid(True)
    plt.subplot(212)
    ax1.set_aspect('equal')
    plt.plot(ranged, PBsArr, 'r', ranged, BBsArr, 'go', ranged, WBsArr, 'b')
    plt.grid(True)
    plt.show()