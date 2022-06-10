# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 15:01:48 2022

@author: anamc
"""

from sympy import *
import math
x = symbols('x')

# first gas injection - Pipe D
# funct1 # incorrect
# funct2 = 4161.9 * x - 2 *(10**8)
# funct3 = 6586.4 * x - 3 *(10**8)

# second gas injection - Pipe D
# funct1 = 6475 * x - 3 * (10**8)
funct2 = 9362.1 * x - 4 * (10**8)



print("Expression : {} ".format(funct2))

# Use sympy.diff() method
f_prime = diff(funct2, x)

print("Value of the derivative : {} ".format(f_prime))




# V = 2 liter = 0.002 m3, Volume of the chamber
# A = 0.067709 m2, area of cylinder filled with soil (assume height = 2.4 cm and radius = 9.25 cm)
V = 0.002
A = 0.067709
fg = V/A * f_prime
print(fg)


# First gas injection
# func1 - incorrect
# Fick's fg = 122.935 # funct2
# Fick's fg = 194.550 # funct3


# Second gas injection (averaged by minute)
# Fick's fg = 191.256 # funct1
# Fick's fg = 276.539 # funct2