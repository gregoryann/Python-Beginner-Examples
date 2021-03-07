"""
Repeat the Same Item Multiple Times
Create a function that takes two arguments (item, times). The first argument (item) is the item that needs repeating while the second argument (times) is the number of times the item is to be repeated. Return the result in a list.

Examples
repeat("edabit", 3) ➞ ["edabit", "edabit", "edabit"]
repeat(13, 5) ➞ [13, 13, 13, 13, 13]
repeat("7", 2) ➞ ["7", "7"]
repeat(0, 0) ➞ []

Notes
item can be either a string or a number.
times will always be a number.

"""


"""
Solution 1
"""

def repeat(item, times):
	return [item] * times

"""
Solution 2
"""

def repeat(item, times):
	return [item for x in range(times)]


"""
Solution 3
"""

def repeat(item, times):
	lst = []
	for i in range(times):
		lst.append(item)
	return lst

"""
Solution 4
"""

repeat = lambda i,t: [i]*t


"""
Solution 5
"""

def repeat(item, times):
	list = []
	
	for i in range(times):
		list.append(item)
		
	return list

