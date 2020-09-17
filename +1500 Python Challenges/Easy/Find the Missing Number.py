"""

Find the Missing Number

Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.

Examples
missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5

missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10

missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7

Notes
The list of numbers will be unsorted (not in order).
Only one number will be missing.
"""


"""
Solution 1
"""

def missing_num(lst):
  return 55 - sum(lst)

"""
Solution 2
"""
def missing_num(lst):
  for n in range(1,11):
    if n not in lst:
      return(n)

"""
Solution 3
"""

def missing_num(lst):
  return list(set(range(1,11)) - set(lst))[0]

"""
Solution 4
"""

def missing_num(lst):
  return [x for x in [1,2,3,4,5,6,7,8,9,10] if x not in lst][0]



