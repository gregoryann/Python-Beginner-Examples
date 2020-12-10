"""
Swimming Pool

Suppose a swimming pool blueprint can be represented as a 2D list, where 1s represent the pool and 0s represent the rest of the backyard.

[[0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 0],
[0, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]]
# Legitimate
Suppose a pool is considered legitimate if it does not touch any of the four borders in this 2D list.

[[1, 1, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]]
# Illegitimate! 
# The 1s are touching both the left "fence" and the upper "fence".
Create a function that returns True if the pool plan is legitimate, and False otherwise.

Examples
is_legitimate([
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0, 0],
  [0, 1, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0]
]) ➞ True

is_legitimate([
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0, 0],
  [0, 1, 1, 1, 1, 1, 0, 0],
  [0, 0, 1, 1, 1, 0, 0, 0]
]) ➞ False

is_legitimate([
  [0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 0, 0]
]) ➞ True

"""



################################################################
"""
Solution 1
"""


def is_legitimate(lst):
	if 1 in lst[0] or 1 in lst[-1]: return False
	for i in lst:
		if i[0]==1 or i[-1]==1: return False
	return True



################################################################
"""
Solution 2
"""


is_legitimate=lambda l:sum(l[0]+l[-1]+[l[i][0]+l[i][-1]for i in range(len(l))])<1



################################################################
"""
Solution 3
"""


def is_legitimate(lst):
  if lst[0].count(1) == 0 and lst[-1].count(1) == 0:
    for i in lst:
      if 1 == i[0] or i[-1]:
        return False
    return True
  return False



#################################################################
"""
Solution 4
"""


def is_legitimate(lst):
	def all_zeroes(l):
		for i in l:
			if i != 0:
				return False
		return True
	rotated_lst = list(zip(*lst))
	return all_zeroes(lst[0]) and all_zeroes(lst[-1]) and all_zeroes(rotated_lst[0]) and all_zeroes(rotated_lst[-1])



