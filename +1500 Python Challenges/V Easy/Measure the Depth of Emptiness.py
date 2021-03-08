"""
Measure the Depth of Emptiness
In this challenge you will receive an input of the form:

[[[[[[[[[[[]]]]]]]]]]]
In other words, a list containing a list containing a list containing... a list containing nothing.

Your goal is to measure the depth of this list, where [] has a depth 1, [[]] has depth of 2, [[[]]] has depth 3, etc.

Examples
measure_the_depth([]) ➞ 1

measure_the_depth([[]]) ➞ 2

measure_the_depth([[[]]]) ➞ 3

measure_the_depth([[[[[[[[[[[]]]]]]]]]]]) ➞ 11
Notes
One way to solve this is with recursion; but maybe there's a way to "count the brackets"?

"""


"""
Solution 1
"""

def measure_the_depth(lst):
	return str(lst).count("[")

"""
Solution 2
"""

def measure_the_depth(lst):
	if not lst:
		return 1
	else:
		return measure_the_depth(lst[0]) + 1

"""
Solution 3
"""

def measure_the_depth(lst):
    cnt = 1
    while len(lst) > 0 and type(lst) == list:
        cnt += 1
        lst = lst[0]
    return cnt

"""
Solution 4
"""

measure_the_depth = lambda l:str(l).count('[')




