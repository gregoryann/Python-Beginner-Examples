"""
Simple OOP Calculator

Create methods for the Calculator class that can do the following:

Add two numbers.
Subtract two numbers.
Multiply two numbers.
Divide two numbers.
Examples
calculator = Calculator()

calculator.add(10, 5) ➞ 15

calculator.subtract(10, 5) ➞ 5

calculator.multiply(10, 5) ➞ 50

calculator.divide(10, 5) ➞ 2

Notes
The methods should return the result of the calculation.
Don't worry about needing to handle division by zero errors.
See the Resources tab for some helpful tutorials on Python classes.
"""




################################################################
"""
Solution 1
"""


class Calculator:
	@staticmethod	
	def add(n1,n2):
		return n1 + n2
	@staticmethod
	def subtract(n1,n2):
		return n1 - n2
	@staticmethod
	def divide(n1,n2):
		if n2 != 0:
			return n1 / n2
	@staticmethod
	def multiply(n1,n2):
		return n1 * n2




################################################################
"""
Solution 2
"""


from operator import*
class Calculator:add=add;subtract=sub;multiply=mul;divide=truediv




################################################################
"""
Solution 3
"""


class Calculator:
	# Write methods to add(), subtract(), multiply() and divide()
	def add(self, a, b):
		return a + b
	
	def subtract(self, a, b):
		return a - b
	
	def multiply(self, a, b):
		return a*b
	
	def divide(self, a, b):
		return a/b






#################################################################
"""
Solution 4
"""



class Calculator:
	for x,y in {'add':'+','subtract':'-','multiply':'*','divide':'/'}.items():
		exec('def ' + x + '(self, x, y): return x' + y + 'y')


