"""
Tuck in List

Create a function that takes two lists and insert the second list in the middle of the first list.

Examples
tuck_in([1, 10], [2, 3, 4, 5, 6, 7, 8, 9]) ➞ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tuck_in([15,150], [45, 75, 35]) ➞ [15, 45, 75, 35, 150]

tuck_in([[1, 2], [5, 6]], [[3, 4]]) ➞ [[1, 2], [3, 4], [5, 6]]

Notes
The first list always has two elements.
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################





"""
Solution 1
"""

def tuck_in(lst1, lst2):
    return lst1[:1] + lst2 + lst1[-1:]

"""
Solution 2
"""

def tuck_in(A, B):
	A, C = [[i] for i in A]
	return A + B + C

"""
Solution 3
"""

def tuck_in(lst1, lst2):
	lst1[1:1] = lst2
	return lst1

"""
Solution 4
"""

tuck_in = lambda lst1, lst2 : [lst1[0]] + lst2 + [lst1[-1]]

"""
Solution 5
"""

def tuck_in(lst1, lst2):
	new=[lst1[0]]
	for i in range(len(lst2)):
		new.append(lst2[i])
	new.append(lst1[-1])
	return new