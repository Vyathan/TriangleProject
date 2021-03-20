"""
Program: TriangleProject.py
Programmer: Matt Brundage II
Determine whether or not a triangle is a right triangle.
Output a statement declaring whether or not the triangle is a right triangle.
"""

# Display Program Name and Purpose
print('Triangle Calculator! Determine whether or not your triangle is a right triangle!')

# Explain Pythagoren Theorem
print('For a Triange to be a right triangle the sum of the square root of two sides must equal the square root of the final side (the side opposite the 90 degree andgle, called the hypotenuse).')

import math

# Request the inputs
firstSide = float(input("Enter the length of the longest side: "))
secondSide = float(input("Enter the length of side 2: "))
thirdSide = float(input("Enter the length of side 3: "))

# Compute the triangle
if firstSide * firstSide == secondSide * secondSide + thirdSide * thirdSide:
    print("Triangle is a right triangle")
else:
    print("Triangle is not a right triangle")