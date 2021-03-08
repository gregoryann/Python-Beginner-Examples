"""

Even Odd Partition

Write a function that partitions the list into two sublists: one with all even integers, and the other with all odd integers. Return your result in the following format:

[[evens], [odds]]

Examples
even_odd_partition([5, 8, 9, 2, 0]) ➞ [[8, 2, 0], [5, 9]]

even_odd_partition([1, 0, 1, 0, 1, 0]) ➞ [[0, 0, 0], [1, 1, 1]]

even_odd_partition([1, 3, 5, 7, 9]) ➞ [[], [1, 3, 5, 7, 9]]

even_odd_partition([]) ➞ [[], []]

Notes
Return two empty sublists if the input is an empty list.
Keep the same relative ordering as the original list.

"""


"""
Solution 1
"""

def even_odd_partition(lst):
  return [[i for i in lst if not i%2], [i for i in lst if i%2]]


"""
Solution 2
"""

def even_odd_partition(lst):
	evens, odds = [], []
	for i in lst:
		odds.append(i) if i%2 else evens.append(i)
	return [evens, odds]



"""
Solution 3
"""

def even_odd_partition(lst):
	if lst == []: return [[],[]]
	return [[i for i in lst if i % 2 == 0], [i for i in lst if i % 2 != 0]]



"""
Solution 4
"""






