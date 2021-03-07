"""
Adding Numbers in a String
Given a string of numbers separated by a comma and space, return the total of all the numbers.

Examples
add_nums("2, 5, 1, 8, 4") ➞ 20

add_nums("1, 2, 3, 4, 5, 6, 7") ➞ 28

add_nums("10") ➞ 10
Notes
Numbers will always be separated by a comma and space.
Your function should accept negative numbers.

"""


"""
Solution 1
"""

def add_nums(nums):
	return eval(nums.replace(", ", "+"))

"""
Solution 2
"""

def add_nums(nums):
	return sum(int(i) for i in nums.split(', '))

"""
Solution 3
"""

def add_nums(nums):
	numlist= [int(s) for s in nums.split(',')]
	return (sum (numlist))

"""
Solution 4
"""

def add_nums(nums):
	x = nums.split(", ")
	new_list = [float(i) for i in x]
	
	total = 0 
	
	for i in new_list : 
		total += i
		
	return total





