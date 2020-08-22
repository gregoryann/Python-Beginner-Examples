"""
Find the Amount of Potatoes
Create a function to return the amount of potatoes there are in a string.

Examples
potatoes("potato") ➞ 1

potatoes("potatopotato") ➞ 2

potatoes("potatoapple") ➞ 1

"""






"""
Solution 1
"""

def potatoes(potato):
  return potato.count('potato')

"""
Solution 2
"""

potatoes=lambda p:p.count('p')

"""
Solution 3
"""

def potatoes(potato):
	return len(potato.split('potato')) - 1

"""
Solution 4
"""






