"""
Fix the Error: Mutating Arrays
Suppose I want to define a function that removes the last element of a list each time I call it, but does not mutate the original list. Fix the code so that the results are no longer mutating the list.

def minus_one(lst):
  arr.pop()
  return arr
Examples
x = [1, 2, 3, 4, 5]
minus_one(x) ➞ [1, 2, 3, 4]  # 1st time function is called.
minus_one(x) ➞ [1, 2, 3]  # 2nd time function is called.
minus_one(x) ➞ [1, 2]  # 3rd time function is called.
minus_one(x) ➞ [1]  # 4th time function is called.

# What I want instead:
minus_one(x) ➞ [1, 2, 3, 4]  # 1st time function is called.
minus_one(x) ➞ [1, 2, 3, 4]  # 2nd time function is called.
minus_one(x) ➞ [1, 2, 3, 4]  # 3rd time function is called.
minus_one(x) ➞ [1, 2, 3, 4]  # 4th time function is called.

"""


"""
Solution 1
"""

def minus_one(lst):
	return lst[:-1]

"""
Solution 2
"""

# Fix this incorrect code, so that all tests pass!
def minus_one(lst):
	arr=lst.copy()
	arr.pop()
	return arr


"""
Solution 3
"""

# Fix this incorrect code, so that all tests pass!
def minus_one(lst):
	arr=lst.copy()
	arr.pop()
	return arr

"""
Solution 4
"""






