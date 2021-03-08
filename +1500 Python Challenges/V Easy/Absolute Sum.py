"""
Absolute Sum

Take a list of integers (positive or negative or both) and return the sum of the absolute value of each element.

Examples
get_abs_sum([2, -1, 4, 8, 10]) ➞ 25

get_abs_sum([-3, -4, -10, -2, -3]) ➞ 22

get_abs_sum([2, 4, 6, 8, 10]) ➞ 30

get_abs_sum([-1]) ➞ 1

Notes
The term "absolute value" means to remove any negative sign in front of a number, and to think of all numbers as positive (or zero).

"""


"""
Solution 1
"""

def get_abs_sum(nums):
  return sum(map(abs, nums))


"""
Solution 2
"""

def get_abs_sum(nums):
  sum = 0
  for nb in nums:
    sum += abs(nb)
  return sum




