"""
Sum of Odd and Even Numbers

Write a function that takes a list of numbers and returns a list with two elements:

The first element should be the sum of all even numbers in the list.
The second element should be the sum of all odd numbers in the list.
Example
sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])

sum_odd_and_even([0, 0]) ➞ [0, 0])

Notes
Count 0 as an even number.
"""



################################################################
"""
Solution 1
"""


def sum_odd_and_even(lst):
	return [sum(e for e in lst if e%2==i) for i in [0,1]]



################################################################
"""
Solution 2
"""


from functools import reduce
def sum_odd_and_even(lst):
	return reduce(lambda s, v: [s[0], s[1]+v] if v%2 else [s[0]+v, s[1]], lst, [0, 0])



################################################################
"""
Solution 3
"""


def sum_odd_and_even(lst):
    evens = sum([x for x in lst if x%2 == 0])
    odds = sum([x for x in lst if x%2 == 1])
    return [evens, odds]


#################################################################
"""
Solution 4
"""


def sum_odd_and_even(lst):
	def is_even(n):
		return abs(n)%2==0
	def is_odd_even(lst):
		odd = []
		even = []
		
		for n in lst:
			if is_even(n) == True:
				even.append(n)
			else:
				odd.append(n)
		
		return [sum(even), sum(odd)]
	
	oe = is_odd_even(lst)
	
	return oe



