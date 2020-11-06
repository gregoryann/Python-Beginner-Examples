"""
Accumulating List

Create a function that takes in a list and returns a list of the accumulating sum.

Examples
accumulating_list([1, 2, 3, 4]) ➞ [1, 3, 6, 10]
# [1, 3, 6, 10] can be written as  [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4]

accumulating_list([1, 5, 7]) ➞ [1, 6, 13]

accumulating_list([1, 0, 1, 0, 1]) ➞ [1, 1, 2, 2, 3]

accumulating_list([]) ➞ []

Notes
An empty list input [] should return an empty list [].
"""



################################################################
"""
Solution 1
"""


def accumulating_list(list1):
    return [sum(list1[:i+1]) for i in range(len(list1))]



################################################################
"""
Solution 2
"""


from itertools import accumulate
def accumulating_list(lst):
	return list(accumulate(lst))



################################################################
"""
Solution 3
"""


def accumulating_list(lst):
	result = []

	for i in range(len(lst)):
		if i == 0:
			result.append(lst[i])
		else:
			result.append(result[i-1]+lst[i])

	return result




#################################################################
"""
Solution 4
"""


def accumulating_list(elements):
    lngth = len(elements) # 3
    lst = [] # Add into this list
    counter = 0

    for e in elements:
        if len(lst) == 0:
            lst.append(e)
        elif(len(lst) <= lngth):
            lst.append(lst[counter]+e)
            counter += 1

    return lst

accumulating_list([1,2,3,4,5,6,7])






