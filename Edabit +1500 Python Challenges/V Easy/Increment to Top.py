"""
Increment to Top

Create a function that returns the total number of steps it takes to transform each element to the maximal element in the list. Each step consists of incrementing a digit by one.

Examples
increment_to_top([3, 4, 5]) ➞ 3
# 3 increments: 3 -> 4, 4 -> 5; 4 -> 5

increment_to_top([4, 3, 4]) ➞ 1

increment_to_top([3, 3, 3]) ➞ 0

increment_to_top([3, 10, 3]) ➞ 14

Notes
If the list contains only the same digits, return 0 (see example #3).
Bonus: Can you write a solution that achieves this by only traversing the list once? (i.e. without finding the max before hand)

"""


"""
Solution 1
"""

def increment_to_top(lst):
	return (sum([max(lst)-i for i in lst]))

"""
Solution 2
"""

def increment_to_top(lst):
  return sum([abs(sorted(lst,reverse=True)[0]-i) for i in sorted(lst,reverse=True)])

"""
Solution 3
"""

def increment_to_top(lst):
	AA = []
	for x in lst:
		AA.append(max(lst) - x)
	return sum(AA)

"""
Solution 4
"""






