"""
Add the Index

Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...

Examples
add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]

add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]

add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]

Notes
You'll only get numbers in the list.
"""




#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def add_indexes(lst):
	return [i+j for i, j in enumerate(lst)]

"""
Solution 2
"""

add_indexes = lambda l: [x+y for (x,y) in enumerate(l)]

"""
Solution 3
"""

def add_indexes(lst):
	index = 0
	new_list = []
	for i in lst:
		new_list.append(i + index)
		index += 1
	return new_list

"""
Solution 4
"""

def add_indexes(lst):
    new_lst = []
    for index, number in enumerate(lst):
        new_lst.append(index + number)
    return new_lst

"""
Solution 5
"""

def add_indexes(lst):
	a = []
	for index,value in enumerate(lst):
		a.append(index+value)
	return a
