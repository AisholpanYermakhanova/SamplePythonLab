# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:10:51 2022

@author: Айшолпан
"""
import math
from cmath import pi, sqrt
""" --1
x = int(input("enter number x: "))
y = int(input("enter number y: "))

print("sum: " + str(x+y))
print("difference : " + str(x-y))
print("product: " + str(x*y))
"""

""" --2
x = float(input("enter number x: "))
y = float(input("enter number y: "))

r = (abs(x) - abs(y))/(1 + abs(x*y))
print(r)
"""

""" --3
x = int(input("enter the length of an edge of cube: "))
print("volume of a cube: " + str(x**3))
print("lateral surface area: " + str(x*x))
"""

""" --4
x = float(input("enter number x: "))
y = float(input("enter number y: "))
print("arithmetic mean : ", (x+y)/2)
print("geometric mean : " , math.sqrt(x*y))
"""

""" --5
x = float(input("enter number h: "))
y = float(input("enter number b: "))
print("arithmetic mean : ", abs((x+y)/2))
print("geometric mean : " , abs(math.sqrt(x*y)))
"""
 



""" --15
x = float(input("enter leg x: "))
y = float(input("enter leg y: "))
print("hypotenuse of a right triangle: ", math.sqrt(x**2 + y**2))
print("area of a right triangle: ", 0.5*x*y)
"""

""" --7
import numpy as np
x = float(input("enter x: "))
y = float(input("enter y: "))
z = float(input("enter z: "))

a = np.log(abs(y-math.sqrt(abs(x)))*(x-(y/(z+(x**2/4)))))
b = x-(x**2/31)+(x**51)
print("a: ", a)
print("b: ", b)
"""

""" --8
x = int(input("side of an equilateral triangle: "))
print("area of this triangle: ", (x**2 * math.sqrt(3))/4 )
"""