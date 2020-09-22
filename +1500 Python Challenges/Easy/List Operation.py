"""
List Operation

Create a function that takes three parameters and returns a list with the first parameter x, the second parameter y, and every number in between the first and second parameter in ascending order. Then filter through the list and return the list with numbers that are only divisible by the third parameter n.

Examples
list_operation(1, 10, 3) ➞ [3, 6, 9]

list_operation(7, 9, 2) ➞ [8]

list_operation(15, 20, 7) ➞ []

Notes
The final list should consist of all numbers between x and y inclusive that are divisible by n.
Return an empty list if there are no numbers that are divisible by n.
"""



"""
Solution 1
"""

def list_operation(x, y, n):
	return list(filter(lambda a:a%n==0,range(x,y+1)))

"""
Solution 2
"""

def list_operation(x, y, n):
	c=[]
	for i in range(x,y+1):
		if i%n==0:
			c.append(i)
	return c

"""
Solution 3
"""

def list_operation(x, y, n):
	return sorted([x for x in range(x, y + 1) if x % n == 0])








