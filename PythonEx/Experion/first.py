# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 22:51:34 2020

@author: Vishnu
"""


print ('hi')

L = ["Geeks\n", "for\n", "Geeks\n"] 
  
file = open('myfile.txt', 'w') 
file.writelines(L) 
file.close() 
  
 # Using readlines() 
file = open('myfile.txt', 'r') 
Lines = file.readlines() 
  
count = 0
# Strips the newline character 
for line in Lines: 
    print("Line{}: {}".format(count, line.strip())) 
