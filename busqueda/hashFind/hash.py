# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:05:15 2020

@author: hrmha
"""

import random

def hash(key, mx):
    return key%mx

def wsHash():
    return 0

def makeWorseHashList(data, mx):
    arr = [0] * mx
    for i in data:
        hs = wsHash()
        if str(type(arr[hs])) == "<class 'list'>":
            arr[hs].append(i)
        elif str(type(arr[hs])) == "<class 'int'>":
            if arr[hs] == 0:
                arr[hs] = i
            elif str(type(arr[hs])) == "<class 'list'>":
                arr[hs].append(i)
            else:
                arr[hs] = [arr[hs], i]
    print(arr)
    return arr

def makeHashList(data, mx):
    arr = [0] * mx
    for i in data:
        hs = hash(i, mx)
        if str(type(arr[hs])) == "<class 'list'>":
            arr[hs].append(i)
        elif str(type(arr[hs])) == "<class 'int'>":
            if arr[hs] == 0:
                arr[hs] = i
            elif str(type(arr[hs])) == "<class 'list'>":
                arr[hs].append(i)
            else:
                arr[hs] = [arr[hs], i]
    return arr

def makeTestList(mx):
    data = []
    for i in range(0, mx):
        rand = random.randint(0, (mx*10))
        data.append(rand)
    return data

def test(mx):
    data = makeTestList(mx)
    hashList = makeHashList(data, mx)
    return hashList

if __name__ == '__main__':
    mx = 10
    print(test(mx))
