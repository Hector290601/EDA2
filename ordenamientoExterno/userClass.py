# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:28:09 2020

@author: hrmha
"""

class user:
    def __init__(self, userId, name, lastName, age, gender, phoneNumber, creditCard, cCType):
        self.userId = userId
        self.name = name
        self.last = lastName
        self.age = age
        self.gender = gender
        self.phoneNumber = phoneNumber
        self.creditCard = creditCard
        self.cCType = cCType

if __name__ == '__main__':
    print(user(0, 'Hector', "Robles", 19, 'M', 5510604869, 000000000000000000, 'Visa'))