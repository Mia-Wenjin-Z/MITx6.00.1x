#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 03:01:36 2020

@author: miawenjinzhang
"""

# Paste your code into this box
#payment assumed to be integer

balance = 320000
annualInterestRate = 0.2



##Q2 must be a multiple of 10
#for payment in range(10, balance + 1, 10):
#    #calculate remain using fixed payment of mid
#    remainingBalance = balance
#    for i in range (0, 12):
#        remainingBalance = (remainingBalance - payment) * (1 + annualInterestRate / 12)
#    if remainingBalance <= 0:
#        print("Lowest Payment: ", low)
#        break



#Q3 do a binary search, first occurance where remainingBalance <= 0

def calculateRemainigBalance(payment, balance, annualInterestRate):
    remainingBalance = balance
    for i in range (0, 12):
        remainingBalance = (remainingBalance - payment) * (1 + annualInterestRate / 12)
    return remainingBalance

low = balance / 12
high = balance * ((1 + annualInterestRate / 12) ** 12) / 12
payment = balance

while low + 0.01 < high:
    mid = (high + low) / 2
    #calculate remain using fixed payment of mid
    remainingBalance = calculateRemainigBalance(mid, balance, annualInterestRate)
    if remainingBalance > 0:
        low = mid + 0.01
    else:
        high = mid
if (calculateRemainigBalance(low, balance, annualInterestRate) < 0):
    print("Lowest Payment: ", round(low, 2))
else:
    print("Lowest Payment: ", round(high, 2))



