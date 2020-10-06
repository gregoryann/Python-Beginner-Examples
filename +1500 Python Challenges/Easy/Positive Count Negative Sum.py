"""
Positive Count / Negative Sum

Create a function that takes a list of positive and negative numbers. Return a list where the first element is the count of positive numbers and the second element is the sum of negative numbers.

Examples
sum_neg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) ➞ [10, -65]
# There are a total of 10 positive numbers.
# The sum of all negative numbers equals -65.

sum_neg([92, 6, 73, -77, 81, -90, 99, 8, -85, 34]) ➞ [7, -252]

sum_neg([91, -4, 80, -73, -28]) ➞ [2, -105]

sum_neg([]) ➞ []

Notes
If given an empty list, return an empty list: []
0 is not positive.
"""





################################################################
"""
Solution 1
"""

def sum_neg(nums):
	if nums == []:
		return []
	a = len([n for n in nums if n > 0])
	b = sum([n for n in nums if n < 0])
	return [a, b]






################################################################
"""
Solution 2
"""

def sum_neg(nums):
  if(not nums): return []
  pos = [] 
  neg = []
  for x in nums : neg.append(x) if x < 0 else pos.append(x)
  return  [len(pos), sum(neg)]






################################################################
"""
Solution 3
"""

sum_neg=lambda l:[sum(x>0for x in l),sum(x for x in l if x<0)]if l else[]







#################################################################
"""
Solution 4
"""

def sum_neg(nums):
	if nums:
		pos = []
		neg = []
		for n in nums:
			if n > 0:
				pos.append(n)
			else:
				neg.append(n)
		return [len(pos), sum(neg)]
	return []




