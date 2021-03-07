"""
Find the Odd Integer

Create a function that takes a list and finds the integer which appears an odd number of times.

Examples
find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1

find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5

find_odd([10]) ➞ 10

Notes
There will always only be one integer that appears an odd number of times.
"""




#############################################################
#                        MY SOLUTIONS                       #
#############################################################


"""
Solution 1
"""

def find_odd(lst):
  for num in lst:
    if lst.count(num) % 2:
      return num


"""
Solution 2
"""

def find_odd(lst):
  for i in set(lst):
    if lst.count(i) % 2 == 1:
      return i

"""
Solution 3
"""
def find_odd(lst):
	"""
	>>> find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])
	-1
	>>> find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5])
	5
	"""
	veces = {}
	for e in lst:
		if e in veces:
			veces[e] += 1
		else:
			veces[e] = 1
	for k, v in veces.items():
		if v % 2 != 0:
			return k

"""
Solution 4
"""

from collections import Counter

def find_odd(lst):
	counted_list = Counter(lst)
	for the_key, the_value in counted_list.items():
		if the_value % 2 != 0:
			return the_key




