"""


Get the Sum of All List Elements
Create a function that takes a list and returns the sum of all numbers in the list.

Examples
get_sum_of_elements([2, 7, 4]) ➞ 13

get_sum_of_elements([45, 3, 0]) ➞ 48

get_sum_of_elements([-2, 84, 23]) ➞ 105
Notes

"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""



get_sum_of_elements=sum



"""
Solution 2
"""

def get_sum_of_elements(lst):
    return sum(lst)



"""
Solution 3
"""


def get_sum_of_elements(lst):
	a = 0
	for i in lst:
		a += i
	return a


"""
Solution 4
"""



get_sum_of_elements=lambda l:sum(i for i in l)



def get_sum_of_elements(l):
		return sum(l)



def get_sum_of_elements(lst):
	for i in range(len(lst)):
		return sum(lst)


 def get_sum_of_elements(lst):
	sum = 0
	for i in lst:
	 sum = sum + i
	return sum