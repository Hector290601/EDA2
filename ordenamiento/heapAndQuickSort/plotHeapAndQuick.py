# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:46:51 2020

@author: hrmha
"""
import matplotlib.pyplot as plt
import pandas as pd
from heapSort import *
from quickSort import *

data = pd.DataFrame(columns=('ArraySize', 'MiddleMergeSort', 'BestMergeSort',
                             'WorseMergeSort', 'MiddleBubbleSort',
                             'BestBubbleSort', 'WorseBubbleSort', ))

def plot(n):
    global ranged
    PHs, BHs, WHs = toPlotHs(n)
    PQs, BQs, WQs = toPlotQs(n)
    return PHs, BHs, WHs, PQs, BQs, WQs

if __name__ == '__main__':
    print("Making Plot")
    PMsArr = []
    BMsArr = []
    WMsArr = []
    PBsArr = []
    BBsArr = []
    WBsArr = []
    ranged = range(2, 102)
    for i in ranged:
        PMs, BMs, WMs, PBs, BBs, WBs = plot(i)
        data.loc[len(data)]=[i, PMs, BMs, WMs, PBs, BBs, WBs]
        print("Promedio MergeSort: ", PMs, " Mejor MergeSort: ", BMs, " Peor MergeSort: ", WMs)
        print("Promedio BubbleSort: ", PBs, " Mejor BubbleSort: ", BBs, " Peor BubbleSort: ", WBs)        
        print("Tamaño del arreglo: ", i)
        PMsArr.append(PMs)
        BMsArr.append(BMs)
        WMsArr.append(WMs)
        PBsArr.append(PBs)
        BBsArr.append(BBs)
        WBsArr.append(WBs)
    fig1, ax1 = plt.subplots()
    plt.subplot(321)
    ax1.set_aspect('equal')
    plt.plot(ranged, PMsArr, 'r+')
    plt.grid(True)
    plt.subplot(323)
    ax1.set_aspect('equal')
    plt.plot(ranged, BMsArr, 'g+')
    plt.grid(True)
    plt.ylabel("Iteraciones de la función")
    plt.subplot(325)
    ax1.set_aspect('equal')
    plt.plot(ranged, WMsArr, 'b+')
    plt.xlabel("HeapSort")
    plt.grid(True)
    plt.subplot(322)
    ax1.set_aspect('equal')
    plt.plot(ranged, PBsArr, 'r+')
    plt.grid(True)
    plt.subplot(324)
    ax1.set_aspect('equal')
    plt.plot(ranged, BBsArr, 'g+')
    plt.grid(True)
    plt.subplot(326)
    ax1.set_aspect('equal')
    plt.xlabel("QuickSort")
    plt.plot(ranged, WBsArr, 'b+')
    plt.grid(True)
    plt.savefig("plot.png")
    plt.show()
    data.to_csv("savedData.csv")
