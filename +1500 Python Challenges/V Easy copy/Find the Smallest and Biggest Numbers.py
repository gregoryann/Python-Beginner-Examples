"""

Find the Smallest and Biggest Numbers
Create a function that accepts a list of numbers and return both the minimum and maximum numbers, in that order (as a list).

Examples
min_max([1, 2, 3, 4, 5]) ➞ [1, 5]

min_max([2334454, 5]) ➞ [5, 2334454]

min_max([1]) ➞ [1, 1]
Notes
All test lists will have at least one element and are valid.


"""






"""
Solution 1
"""

def min_max(nums):
  out = []
  out.append(min(nums))
  out.append(max(nums))
  return out




"""
Solution 2
"""

def min_max(nums):
  sorted_nums = sorted(nums)
  return [sorted_nums[0], sorted_nums[-1]]



"""
Solution 3
"""

def min_max(nums):
  return [min(nums), max(nums)]


"""
Solution 4
"""


def min_max(nums):
  minmax_list = []
  minmax_list.append(min(nums))
  minmax_list.append(max(nums))
  return minmax_list






