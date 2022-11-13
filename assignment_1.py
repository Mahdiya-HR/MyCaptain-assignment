# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 18:22:19 2022

@author: Mahdiya HR
"""

from math import pi
r = float(input ("input the radius of the circle: "))
print ("The area of the circle with radius " + str (r) + " is: " + str(pi * r**2)) 
                                                                                  
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
                                                                                                                                                                                  