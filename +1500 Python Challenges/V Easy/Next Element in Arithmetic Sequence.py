"""
Next Element in Arithmetic Sequence
Create a function that returns the next element in an arithmetic sequence. In an arithmetic sequence, each element is formed by adding the same constant to the previous element.

Examples
next_element([3, 5, 7, 9]) ➞ 11

next_element([-5, -6, -7]) ➞ -8

next_element([2, 2, 2, 2, 2]) ➞ 2
Notes
All input arrays will contain integers only.

"""



"""
Solution 1
"""

def next_element(lst):
	return lst[-1] + (lst[1] - lst[0])


"""
Solution 2
"""

def next_element(lst):
	if len(lst) == 1:
		return lst[0]
	return lst[-1] + lst[-1] - lst[-2]


"""
Solution 3
"""

def next_element(lst):
	constant = lst[1] - lst[0]
	lst.append(lst[-1] + constant)
	return lst[-1]

