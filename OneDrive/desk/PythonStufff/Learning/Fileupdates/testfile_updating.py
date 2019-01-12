# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 13:34:41 2019

@author: ojasw
"""

import os

f = open("test_file.txt", "a")
name = input("Enter your name: ")
numBags = int(input("Enter the number of bags you've counted:"))

w = open("test_updated.txt", "w")

for line in f:
    details = line.split(",")
    if details[0] == name:
        total = numBags + int(details[1])
        w.write(name + "," + str(total) + "\n")
    else:
        w.write(details[0] + "," + details[1] + "\n")
        
f.close()  
w.close()

os.remove("test_file.txt")
os.rename("test_updated.txt", "test_file.txt")