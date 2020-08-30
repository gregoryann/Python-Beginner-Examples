"""
Fix The Bug: Simple List Manipulation
Help fix all the bugs in the function increment_items! It is intended to add 1 to every element in the list!

Examples
increment_items([0, 1, 2, 3]) ➞ [1, 2, 3, 4]

increment_items([2, 4, 6, 8]) ➞ [3, 5, 7, 9]

increment_items([-1, -2, -3, -4]) ➞ [0, -1, -2, -3]
Notes
Make sure to read every line carefully.

"""


"""
Solution 1
"""

def increment_items(lst):
	
	return [i+1 for i in lst]

"""
Solution 2
"""

def increment_items(lst):
	for i in range(len(lst)):
		lst[i] += 1
	return lst

"""
Solution 3
"""

increment_items = lambda l:[i+1 for i in l]

"""
Solution 4
"""

def increment_items(lst):
    j=[]
    for i in lst:
        i += 1
        j.append(i)
    return j





