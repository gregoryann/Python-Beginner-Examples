"""
Less Than 100 List Remix
Given a list of numbers, return True if the sum of the list is less than 100; otherwise return False.

Examples
list_less_than_100([5, 57]) ➞ True

list_less_than_100([77, 30]) ➞ False

list_less_than_100([0]) ➞ True
"""


"""
Solution 1
"""

def list_less_than_100(lst):
	return sum(lst)<100

"""
Solution 2
"""

def list_less_than_100(lst):
	sum = 0
	for num in lst:
		sum += num
	return sum < 100

"""
Solution 3
"""

def list_less_than_100(lst):
	cur_sum = 0
	for i in lst:
		cur_sum = cur_sum + i
	if cur_sum >= 100:
		return False
	else:
		return True

"""
Solution 4
"""

def list_less_than_100(lst):
    if sum(lst) < 100:
        return True
    else:
        return False
print(list_less_than_100([5, 57]))
print(list_less_than_100([77, 30]))
print(list_less_than_100([0]))




