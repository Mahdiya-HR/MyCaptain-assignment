# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:43:38 2022

@author: Mahdiya HR
"""

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
       
       # Python program to print positive Numbers in a List
 
# list of numbers
list1 = [11, -21, 0, 45, 66, -93]
 
# iterating each number in list
for num in list1:
 
    # checking condition
    if num & gt
    = 0:
        print(num, end=& quot
              & quot
              )