"""
Pythagoras Calculator

Create a function that will find the hypotenuse in a right angle triangle.

The pythagoras equation: a²+b²=c²

Examples
pythagoras(4, 3) ➞ 5  // 4²+3²=25, √25=5

pythagoras(5, 12) ➞ 13

Notes
Don't forget to use return. Use the math libary
"""



################################################################
"""
Solution 1
"""


#from math import sqrt
#sqrt()
def pythagoras(a, b):
	return (a ** 2 + b ** 2) ** (1 / 2)







################################################################
"""
Solution 2
"""

from math import sqrt
# sqrt()
def pythagoras(a, b):
	return sqrt(a*a + b*b)





################################################################
"""
Solution 3
"""

pythagoras=lambda a,b:(a*a+b*b)**0.5






