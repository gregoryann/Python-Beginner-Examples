"""
Combinations

Create a function that takes a variable number of arguments, each argument representing the number of items in a group, and returns the number of permutations (combinations) of items that you could get by taking one item from each group.

Examples
combinations(2, 3) ➞ 6

combinations(3, 7, 4) ➞ 84

combinations(2, 3, 4, 5) ➞ 120

Notes
Don't overthink this one.
Input may include the number zero.
"""




################################################################
"""
Solution 1
"""


from numpy import prod
def combinations(*a):
	return prod([x for x in a if x>0])



################################################################
"""
Solution 2
"""


import numpy
def combinations(*items):
    result = filter(lambda x: x>0, items) 
    return numpy.prod(list(result))



################################################################
"""
Solution 3
"""

def combinations(*items):
	if isinstance(items,int):return items
	l=list(items)
	if 0 in l:l.remove(0)
	return eval(str(l).replace(",","*"))[0]



#################################################################
"""
Solution 4
"""


from functools import reduce
def combinations(*items):
	items = filter(lambda a: a != 0, items)
	return reduce(lambda x,y: x * y,items)




