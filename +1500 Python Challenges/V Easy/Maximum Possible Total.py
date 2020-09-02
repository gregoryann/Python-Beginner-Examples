"""
Maximum Possible Total
Given a list of 10 numbers, return the maximum possible total made by summing just 5 of the 10 numbers.

Examples
max_total([1, 1, 0, 1, 3, 10, 10, 10, 10, 1]) ➞ 43

max_total([0, 0, 0, 0, 0, 0, 0, 0, 0, 100]) ➞ 100

max_total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 40

"""


"""
Solution 1
"""

def max_total(nums):
	return sum(sorted(nums)[-5:])

"""
Solution 2
"""

def max_total(n):
	a=[]
	for i in range(5):
		a.append(max(n))
		n.remove(max(n))
	return sum(a)


"""
Solution 3
"""

def max_total(nums):
	sortednums = sorted(nums, reverse = True)
	return sum(i for i in sortednums[0:5])

"""
Solution 4
"""

def max_total(nums):
	result = 0
	nums.sort()
	for i in range(5):
		result += nums.pop(-1)
	return result


"""
Solution 5
"""

def max_total(nums):
  nums.sort()
  return nums[-1] + nums[-2] + nums[-3] + nums[-4] + nums[-5]