"""
Bound Sort
Create a function that returns True if an input array can be completely sorted by only sorting within the bounds [0, n] (inclusive), where n is smaller than or equal to the array's length, and False otherwise.

Examples
bound_sort([1, 6, 5, 3, 8, 9], [0, 3]) ➞ True
# If [1, 6, 5, 3] is sorted to [1, 3, 5, 6], the array is completely sorted.

bound_sort([1, 6, 5, 3, 8, 9], [0, 2]) ➞ False
# Even if [1, 6, 5] is sorted to [1, 5, 6], the array is still not completely sorted.

bound_sort([1, 9, 2, 5, 7], [0, 4]) ➞ True

bound_sort([1, 9, 2, 5, 7], [0, 3]) ➞ False
# Sorting from [0, 3] gives us [1, 2, 5, 9, 7], array still not completely sorted.

Notes
Numbers in array will be unique.
The lower index of the bound will always be 0.
"""




################################################################
"""
Solution 1
"""


def bound_sort(lst, bounds):
	return sorted(lst[:bounds[1]+1]) + lst[bounds[1]+1:] == sorted(lst)



################################################################
"""
Solution 2
"""


def bound_sort(lst, bounds):
	a = lst[bounds[0]:bounds[1]+1]
	b = lst[bounds[1]+1:]
	a = sorted(a)
	c = a+b
	if c == sorted(lst):
		return True
	else:
		return False


################################################################
"""
Solution 3
"""


def bound_sort(lst, bounds):
	sort_sub = sorted(lst[bounds[0]: bounds[1] + 1])
	print ("".join(map(str, sort_sub)))
	mapstr = ''.join(map(str, sort_sub)) in ''.join(map(str, sorted(lst)))
	print(mapstr)
	return mapstr



#################################################################
"""
Solution 4
"""


def bound_sort(lst, bounds):
	lst_2 = [x for x in lst]
	lst_2.sort()
	bound = lst[bounds[0]: bounds[1]+1]
	rest = lst[bounds[1]+1: ]
	bound.sort()
	return lst_2 == (bound +rest)



