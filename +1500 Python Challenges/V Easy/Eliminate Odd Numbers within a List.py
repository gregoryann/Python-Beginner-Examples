"""
Eliminate Odd Numbers within a List

Create a function that takes a list of numbers and returns only the even values.

Examples
no_odds([1, 2, 3, 4, 5, 6, 7, 8]) ➞ [2, 4, 6, 8]

no_odds([43, 65, 23, 89, 53, 9, 6]) ➞ [6]

no_odds([718, 991, 449, 644, 380, 440]) ➞ [718, 644, 380, 440]

Notes
Return all even numbers in the order they were given.
All test cases contain valid numbers ranging from 1 to 3000.

"""


"""
Solution 1
"""

def no_odds(lst):
  return [x for x in lst if x % 2 == 0]

"""
Solution 2
"""

def no_odds(lst):
  return list(filter(lambda num: num%2==0, lst))

"""
Solution 3
"""

def no_odds(lst):
	result = []
	for n in lst:
		if n % 2 == 0:
			result.append(n)
	return result




