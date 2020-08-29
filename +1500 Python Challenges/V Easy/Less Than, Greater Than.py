"""
Less Than, Greater Than
Create a function that takes two numbers num1, num2, and a list lst and returns a list containing all the numbers in lst greater than num1 and less than num2.

Examples
list_between(3, 8, [1, 5, 95, 0, 4, 7]) ➞ [5, 4, 7]

list_between(1, 10, [1, 10, 25, 8, 11, 6]) ➞ [8, 6]

list_between(7, 32, [1, 2, 3, 78]) ➞ []

"""




"""
Solution 1
"""

def list_between(num1, num2, lst):
	return [i for i in lst if i > num1 and i < num2]

"""
Solution 2
"""

def list_between(num1, num2, lst):
	
	Wanted = []
	
	for x in lst:
		if (x > num1) and (x < num2):
			Wanted.append(x)
		
	return Wanted






