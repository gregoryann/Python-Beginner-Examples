"""
Applying Discounts
Create a function that applies a discount d to every number in the list.

Examples
get_discounts([2, 4, 6, 11], "50%") ➞ [1, 2, 3, 5.5]

get_discounts([10, 20, 40, 80], "75%") ➞ [7.5, 15, 30, 60]

get_discounts([100], "45%") ➞ [45]

Notes
The discount is the percentage of the original price (i.e the discount of "75%" to 12 would be 9 as opposed to taking off 75% (making 3)).
There won't be any awkward decimal numbers, only 0.5 to deal with.
"""




#############################################################
#                        MY SOLUTIONS                       #
#############################################################





"""
Solution 1
"""

def get_discounts(nums, d):
	return [int(d.strip('%')) * n / 100 for n in nums]

"""
Solution 2
"""

def get_discounts(nums, d):
	mult = int(d[:-1])/100
	return [i*mult for i in nums]

"""
Solution 3
"""

def get_discounts(nums, d):
	discount = float(d.split('%')[0]) / 100
	return [num * discount for num in nums]

"""
Solution 4
"""

def get_discounts(nums, d):
	nw = []
	for n in nums:
		nw.append(n * float(d[:len(d)-1])/100)
	return nw





