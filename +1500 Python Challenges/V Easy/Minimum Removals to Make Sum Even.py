"""
Minimum Removals to Make Sum Even

Create a function that returns the minimum number of elements removed to make the sum of all elements in a list even.

Examples:

minimum_removals([1, 2, 3, 4, 5]) ➞ 1
minimum_removals([5, 7, 9, 11]) ➞ 0
minimum_removals([5, 7, 9, 12]) ➞ 1

Notes
If the sum is already even, return 0 (see example #2).
The output will be either 0 or 1.

"""

"""
Solution 1
"""

def minimum_removals(lst):
	return sum(lst) % 2

"""
Solution 2
"""

def minimum_removals(lst):
	return 1 if sum(lst) % 2 == 1 else 0






