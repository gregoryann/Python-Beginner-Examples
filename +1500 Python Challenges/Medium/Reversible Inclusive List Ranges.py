"""
Reversible Inclusive List Ranges

Write a function that, given the start_of_range and end_of_range values, returns an array containing all the numbers inclusive to that range. See examples below.

Examples
reversible_inclusive_list(1, 5) ➞ [1, 2, 3, 4, 5]

reversible_inclusive_list(2, 8) ➞ [2, 3, 4, 5, 6, 7, 8]

reversible_inclusive_list(10, 20) ➞ [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

reversible_inclusive_list(24, 17) ➞ [24, 23, 22, 21, 20, 19, 18, 17]

Notes
The sort order of the resulting array is dependent of the input values.
All inputs provided in the test scenarios are valid.
If start_of_range is greater than end_of_range, return a descendingly sorted array, otherwise, ascendingly sorted.
A recursive version of this challenge can be found via this link.
"""



################################################################
"""
Solution 1
"""


def reversible_inclusive_list(n, m):
	s = -1 if n > m else 1
	return list(range(n, m+s, s))



################################################################
"""
Solution 2
"""


def reversible_inclusive_list(start_of_range, end_of_range):
    res =[]
    if start_of_range>end_of_range:
        for i in range(start_of_range,end_of_range-1,-1):res.append(i)
    else:
        for i in range(start_of_range,end_of_range+1):res.append(i)
    return res



################################################################
"""
Solution 3
"""


reversible_inclusive_list=lambda s,e:list(range(s,*((e+1,),(e-1,-1))[s>e]))



#################################################################
"""
Solution 4
"""


def reversible_inclusive_list(beg, end):
    if beg > end:
        return list(range(beg, end-1, -1))
    return list(range(beg, end+1))




