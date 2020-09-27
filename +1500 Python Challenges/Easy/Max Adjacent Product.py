"""
Max Adjacent Product

Given a list of integers, find the pair of adjacent elements that have the largest product and return that product.

Examples
adjacent_product([3, 6, -2, -5, 7, 3] ) ➞ 21

adjacent_product([5, 6, -4, 2, 3, 2, -23]) ➞ 30

adjacent_product([0, -1, 1, 24, 1, -4, 8, 10]) ➞ 80

Notes
Each list has at least two elements.
"""


"""
Solution 1
"""

def adjacent_product(lst):
	return max(a*b for a, b in zip(lst, lst[1:]))

"""
Solution 2
"""

def adjacent_product(l):
	return max([l[i]*l[i+1] for i in range(len(l)-1)])

"""
Solution 3
"""

adjacent_product=lambda l:max(x*y for x,y in zip(l,l[1:]))

"""
Solution 4
"""

def adjacent_product(lst):
	mylist = []
	for i in range (len(lst)-1):	
		mylist.append(lst[i]*lst[i+1])
	return max(mylist)

"""
Solution 5
"""

def adjacent_product(lst):
	va = []
	gg =[]
	for i in lst:
		if len(va)==1:
			gg.append(i*va[0])
			va=[]  
		va.append(i)
	return max(gg)