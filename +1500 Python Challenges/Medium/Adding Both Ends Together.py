"""
Adding Both Ends Together

Given a list of numbers, of any length, create a function which counts how many of those numbers pass the following criterea:

The first and last digits of a number must add to 10.
Examples
ends_add_to_10([19, 46, 2098]) ➞ 3

ends_add_to_10([33, 44, -55]) ➞ 1

ends_add_to_10([]) ➞ 0


Notes
All items in the list will be numbers.
Ignore negative signs (see example #2).
If given an empty list, return 0.
"""



################################################################
"""
Solution 1
"""


def ends_add_to_10(nums):
	return sum(int(str(abs(i))[0]) + int(str(abs(i))[-1]) == 10 for i in nums)



################################################################
"""
Solution 2
"""


ends_add_to_10=lambda n:sum([int(x[0])+int(x[-1])==10for x in map(lambda z:str(z).replace('-',''),n)])



################################################################
"""
Solution 3
"""


def ends_add_to_10(nums):
	count = 0
	for num in nums:
		string = str(num).strip('-')
		if int(string[0]) + int(string[-1]) == 10:
			count += 1
	return count



#################################################################
"""
Solution 4
"""


def ends_add_to_10(nums):
	def to_10(x):
		x = str(abs(x))
		return int(x[0]) + int(x[-1]) == 10
	return sum(map(to_10, nums))




