"""
Omnipresent Value

A value is omnipresent if it exists in every sublist inside the main list.

To illustrate:

[[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
# 3 exists in every element inside this list, so is omnipresent.
Create a function that determines whether an input value is omnipresent for a given list.

Examples
is_omnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) ➞ True

is_omnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6) ➞ False

is_omnipresent([[5], [5], [5], [6, 5]], 5) ➞ True

is_omnipresent([[5], [5], [5], [6, 5]], 6) ➞ False

Notes
Sub-lists can be any length.

"""


"""
Solution 1
"""

def is_omnipresent(lst, val):
	return all([val in l for l in lst])


"""
Solution 2
"""

def is_omnipresent(lst, val):
	x=0
	for i in lst:
		if val in i:
			x+=1
	return x==len(lst)

"""
Solution 3
"""

def is_omnipresent(lst, val):
	arr = []
	for n in lst:
		if val in n:
			arr.append(True)
		else:
			arr.append(False)
	return all(arr)

"""
Solution 4
"""

def is_omnipresent(lst, val):
	result = [0 for x in range(10)]

	for i in range(10):
		for group in lst:
			if i in group:
				result[i] += 1
	
	return result[val] == len(lst)




