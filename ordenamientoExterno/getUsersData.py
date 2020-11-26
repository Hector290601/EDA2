# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 01:59:18 2020

@author: hrmha
"""

import pandas as pd
from userClass import *
import random

usersList = pd.DataFrame(columns=[
    'id', 'name', 'lastName', 'gender', 'phoneNumber', 'creditCard', 'cCType'
    ])


usersData = []

def usersListFromCsv():
    userList = pd.read_csv('data.csv', sep = ',', )
    return userList

def transformData(userList):
    userList = userList.to_records(index = 'False')
    return userList

def addUserFromData(userList, n):
    for i in range(n):
        newUser = user(userList[i][1], userList[i][2], 
                       userList[i][3], random.randint(0, 100), 
                       userList[i][4], userList[i][5],
                       userList[i][6],userList[i][7])
        usersData.append(newUser)
    return usersData

if __name__ == '__main__':
    userList = usersListFromCsv()
    dataTranformed = transformData(userList)
    print(addUserFromData(dataTranformed, 1))
