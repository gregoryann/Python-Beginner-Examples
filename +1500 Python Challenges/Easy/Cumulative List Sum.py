"""
Cumulative List Sum

Create a function that takes a list of numbers and returns a list where each number is the sum of itself + all previous numbers in the list.

Examples
cumulative_sum([1, 2, 3]) ➞ [1, 3, 6]

cumulative_sum([1, -2, 3]) ➞ [1, -1, 2]

cumulative_sum([3, 3, -2, 408, 3, 3]) ➞ [3, 6, 4, 412, 415, 418]

Notes
Return an empty list if the input is an empty list.
"""



########################################################################


"""
Solution 1
"""

def cumulative_sum(lst):
  return [sum(lst[:i+1]) for i in range(len(lst))]

"""
Solution 2
"""

def cumulative_sum(lst):
  total = 0
  lst2 = []
  for number in lst:
    total += number
    lst2.append(total) 
  return lst2

"""
Solution 3
"""

import itertools
def cumulative_sum(lst):
  return [n for n in itertools.accumulate(lst)]

"""
Solution 4
"""

from itertools import accumulate
def cumulative_sum(lst):
	return list(accumulate(lst))




