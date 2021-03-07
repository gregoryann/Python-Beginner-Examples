"""
Circular Shift

Write a function that takes two lists (lst1 and lst2) and an int n, and returns True if the second list equals the first list shifted by n positions. Otherwise, return False.

Examples
circular_shift([1, 2, 3, 4], [3, 4, 1, 2], 2) ➞ True

circular_shift([1, 1], [1, 1], 6) ➞ True

circular_shift([0, 1, 2, 3, 4, 5], [3, 4, 5, 2, 1, 0], 3) ➞ False

Notes
The two lists will have the same length.
n can be a negative value.
"""




################################################################
"""
Solution 1
"""



def circular_shift(lst1, lst2, n):
	return lst1 == lst2[n:] + lst2[:n]



################################################################
"""
Solution 2
"""


def circular_shift(lst1, lst2, n):
	return all(e1 == e2 for e1, e2 in zip(lst1[n:] + lst1[:n], lst2))




################################################################
"""
Solution 3
"""


def circular_shift(lst1, lst2, n):
    n = n % len(lst1)
    if n == 0:
        return lst1[:] == lst2[:]
    return lst2[:] == lst1[n:] + lst1[:n]




#################################################################
"""
Solution 4
"""


def circular_shift(lst1, lst2, n):
	double_2 = 2 * lst2
	if n > len(lst1):
		n = int(n/len(lst1))
	for i in range(len(lst1)-1):
		if lst1[i] == double_2[i+n]:
			return True
		else:
			return False



