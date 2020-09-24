"""
Make a Circle with OOP

Your task is to create a Circle constructor that creates a circle with a radius provided by an argument. The circles constructed must have two getters getArea() (PIr^2) and getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference).

For help with this class, I have provided you with a Rectangle constructor which you can use as a base example.

Examples
circy = Circle(11)
circy.getArea()

# Should return 380.132711084365

circy = Circle(4.44)
circy.getPerimeter()

# Should return 27.897342763877365

Notes
Round results up to the nearest integer.
"""


"""
Solution 1
"""

import math
class Rectangle:

	def __init__(self, sideA=0, sideB=0):
		self.sideA = sideA
		self.sideB = sideB

	def getArea(self):
		return self.sideA * self.sideB
  
	def getPerimeter(self):
		return 2 * (self.sideA + self.sideB)

class Circle:
  
  def __init__(self, radius=0):
    self.radius = radius
  
  def getArea(self):
    return math.ceil(self.radius **2 * math.pi)
  
  def getPerimeter(self):
    return math.ceil(2.0 * self.radius * math.pi)


"""
Solution 2
"""

class Rectangle:

	def __init__(self, sideA=0, sideB=0):
		self.sideA = sideA
		self.sideB = sideB

	def getArea(self):
		return self.sideA * self.sideB
  
	def getPerimeter(self):
		return 2 * (self.sideA + self.sideB)

class Circle:
	def __init__(self, radius):
		self.radius = radius
		self.pi = 3.14159265359
		
	def getArea(self):
		'''Test is using int() to "round" the answer so add .5 '''
		return .5 + (self.radius ** 2) * self.pi
	
	def getPerimeter(self):
		'''Test is using int() to "round" the answer so add .5 '''
		return .5 + (self.radius * 2) * self.pi





