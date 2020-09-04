"""
Sum of Cubes
Create a function that takes a list of numbers and returns the sum of its cubes.

Examples
sum_of_cubes([1, 5, 9]) ➞ 855
# Since 1^3 + 5^3 + 9^3 = 1 + 125 + 729 = 855

sum_of_cubes([3, 4, 5]) ➞ 216

sum_of_cubes([2]) ➞ 8

sum_of_cubes([]) ➞ 0

Notes
If given an empty list, return 0.

"""



"""
Solution 1
"""

def sum_of_cubes(nums):
	return sum(n**3 for n in nums)

"""
Solution 2
"""

def sum_of_cubes(nums):
	new = 0
	for num in nums:
		new += num ** 3
	
	return new

"""
Solution 3
"""

def sum_of_cubes(nums):
	lst = []
	for i in nums:
		x = i ** 3
		lst.append(x)
		
	return sum(lst)

"""
Solution 4
"""






