"""
Index Multiplier

Return the sum of all items in a list, where each item is multiplied by its index (zero-based). For empty lists, return 0.

Examples
index_multiplier([1, 2, 3, 4, 5]) ➞ 40
# (1*0 + 2*1 + 3*2 + 4*3 + 5*4)

index_multiplier([-3, 0, 8, -6]) ➞ -2
# (-3*0 + 0*1 + 8*2 + -6*3)

Notes
All items in the list will be integers.
"""




#############################################################
#                        MY SOLUTIONS                       #
#############################################################





"""
Solution 1
"""

def index_multiplier(lst):
	return sum(j*i for i, j in enumerate(lst))


"""
Solution 2
"""

def index_multiplier(lst):
	sum = 0
	for i in range (len(lst)):
		sum += i*lst[i]
	return sum

"""
Solution 3
"""

def index_multiplier(lst, c=0):
	if len(lst) == 0:
		return 0
	if c == len(lst)-1:
		return lst[c] * c
	return (lst[c]*c) + index_multiplier(lst,c+1)

"""
Solution 4
"""

def index_multiplier(lst):
	i = 0
	result = 0
	
	for n in lst:
		result += n * i
		i += 1
	
	return result




