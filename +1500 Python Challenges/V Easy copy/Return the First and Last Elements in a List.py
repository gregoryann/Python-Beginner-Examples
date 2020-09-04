"""

Return the First and Last Elements in a List
Create a function that takes a list of elements and return the first and last elements as a new list.

Examples
first_last([5, 10, 15, 20, 25]) ➞ [5, 25]

first_last(["edabit", 13, None, False, True]) ➞ ["edabit", True]

first_last([None, 4, "6", "hello", None]) ➞ [None, None]
Notes
Test input will always contain a minimum of two elements within the list.
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""






"""
Solution 1
"""

def first_last(lst):
	return [lst[0], lst[-1]]





"""
Solution 2
"""


def first_last(lst):
	del lst[1:-1]
	return lst


"""
Solution 3
"""


def first_last(lst):
	result = [lst[0], lst.pop()]
	return result


"""
Solution 4
"""

def first_last(lst):
	retnList=[]
	retnList.append(lst[0])
	retnList.append(lst[-1])
	return retnList



def first_last(lst):
	x = lst[0]
	y = lst[-1]
	lst2 = [x,y]
	return lst2








