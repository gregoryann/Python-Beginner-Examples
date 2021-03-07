"""
Return the Sum of the Two Smallest Numbers

Create a function that takes a list of numbers and returns the sum of the two lowest positive numbers.

Examples
sum_two_smallest_nums([19, 5, 42, 2, 77]) ➞ 7

sum_two_smallest_nums([10, 343445353, 3453445, 3453545353453]) ➞ 3453455

sum_two_smallest_nums([2, 9, 6, -1]) ➞ 8

sum_two_smallest_nums([879, 953, 694, -847, 342, 221, -91, -723, 791, -587]) ➞ 563

sum_two_smallest_nums([3683, 2902, 3951, -475, 1617, -2385]) ➞ 4519

Notes
Don't count negative numbers.
Floats and empty lists will not be used in any of the test cases.
"""


################################################################################




"""
Solution 1
"""

def sum_two_smallest_nums(lst):
	return sum(sorted([x for x in lst if x > 0])[:2])

"""
Solution 2
"""

def sum_two_smallest_nums(lst):
  lst = sorted(x for x in lst if x >= 0)
  return sum(lst[:2])


"""
Solution 3
"""

sum_two_smallest_nums=lambda l:sum(sorted(x for x in l if x>0)[:2])

"""
Solution 4
"""

def sum_two_smallest_nums(lst):
	sorted_list = sorted(lst, reverse = True)
	while sorted_list[-1] < 0:
		sorted_list.pop()
	return sorted_list.pop() + sorted_list.pop()

"""
Solution 5
"""

def sum_two_smallest_nums(lst):
	while min(lst) < 0:
		lst.remove(min(lst))
	a = min(lst)
	lst.remove(a)
	return a + min(lst)