"""
Check if One Array can be Nested in Another
Create a function that returns True if the first list can be nested inside the second.

list1 can be nested inside list2 if:

list1's min is greater than list2's min.
list1's max is less than list2's max.
Examples
can_nest([1, 2, 3, 4], [0, 6]) ➞ True

can_nest([3, 1], [4, 0]) ➞ True

can_nest([9, 9, 8], [8, 9]) ➞ False

can_nest([1, 2, 3, 4], [2, 3]) ➞ False
Notes
Note the strict inequality (see example #3).

"""






"""
Solution 1
"""

def can_nest(list1, list2):
	return min(list1) > min(list2) and max(list1) < max(list2)


"""
Solution 2
"""

def can_nest(list1, list2):
	a = max(list1)
	b = min(list1)
	c = max(list2)
	d = min(list2)
	if b > d and a < c:
		return True
	else:
		return False


"""
Solution 3
"""

def can_nest(list1, list2):
	if min(list1) > min(list2) and max(list1) < max(list2):
		my_bool = True
	else:
		my_bool = False
	return my_bool

"""
Solution 4
"""

def can_nest(list1, list2):
  if min(list1) > min(list2):
    if max(list1) < max(list2):
      return True
  return False






