"""
Frequency Distribution

Create a function that returns the frequency distribution of a list. This function should return an object, where the keys are the unique elements and the values are the frequency in which those elements occur.

Examples
get_frequencies(["A", "B", "A", "A", "A"]) ➞ { "A" : 4, "B" : 1 }

get_frequencies([1, 2, 3, 3, 2]) ➞ { 1: 1, 2: 2, 3: 2 }

get_frequencies([True, False, True, False, False]) ➞ { True: 2, False: 3 }

get_frequencies([]) ➞ {}

Notes
If given an empty list, return an empty object (see example #4).
The object should be in the same order as in the input list.
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def get_frequencies(lst):
	return {x:lst.count(x) for x in lst}

"""
Solution 2
"""

def get_frequencies(lst):
	d = {}
	for i in set(lst):
		d[i] = lst.count(i)
	return d

"""
Solution 3
"""

def get_frequencies(lst):
	hashmap = {}
	for i in lst:
		hashmap.setdefault(i, 0)
		hashmap[i] += 1
	return hashmap

"""
Solution 4
"""

def get_frequencies(lst):
	setLst = {}
	for x in set(lst):
		setLst[x] = lst.count(x)
	return(setLst)




