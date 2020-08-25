"""
Multiply Every List Item by Two
Create a function that takes a list with numbers and return a list with the elements multiplied by two.

Examples
get_multiplied_list([2, 5, 3]) ➞ [4, 10, 6]

get_multiplied_list([1, 86, -5]) ➞ [2, 172, -10]

get_multiplied_list([5, 382, 0]) ➞ [10, 764, 0]
Notes

"""


"""
Solution 1
"""

def get_multiplied_list(lst):
	return [i*2 for i in lst]


"""
Solution 2
"""

def get_multiplied_list(lst):
	newLst=[]
	a=len(lst)
	for i in range(0,a):
		newLst.append(lst[i]*2)
	return newLst
    
"""
Solution 3
"""

get_multiplied_list = lambda l: [x*2 for x in l]

"""
Solution 4
"""

def get_multiplied_list(lst):
	y = []
	for x in lst:
		y.append(x*2)
	return y


"""
Solution 5
"""


def get_multiplied_list(lst):
		new_list = []
		for i in lst:
			i = i * 2
			new_list.append(i)
		return new_list
