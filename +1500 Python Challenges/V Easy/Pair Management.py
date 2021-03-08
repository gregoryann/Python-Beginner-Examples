"""
Pair Management
Given two arguements, return a list contains these two arguements.

Examples
make_pair(51, 21) ➞[51, 21]

make_pair(512124, 215) ➞[512124, 215]
"""

#######################################################

"""
Solution 1
"""

def make_pair(num1, num2):
	return [num1, num2]

"""
Solution 2
"""

def make_pair(*n ):
  return list(n)

"""
Solution 3
"""

def make_pair(num1, num2):
	list = []
	list.append(num1)
	list.append(num2)
	return list






