"""
List of Multiples

Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num until the list length reaches length.

Examples
list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]

list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]

Notes
Notice that num is also included in the returned list.
"""




################################################################
"""
Solution 1
"""


def list_of_multiples (num, length):
	return [i*num for i in range(1,length+1)]



################################################################
"""
Solution 2
"""


def list_of_multiples (num, length):
	lst = []
	for i in range(length):
		lst.append(num+i*num)
	return lst





################################################################
"""
Solution 3
"""


def list_of_multiples (num, length):
	count = 0
	lst = []
	while count < length:
		count += 1
		lst.append(num*count)
	return lst




#################################################################
"""
Solution 4
"""


list_of_multiples=lambda n,l:list(range(n,n*l+1,n))




