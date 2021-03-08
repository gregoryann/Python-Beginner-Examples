"""
One, Two, Skip a Few

Create a function which calculates how many numbers are missing from an ordered number line. This number line starts at the first value of the list, and increases by 1 to the end of the number line, ending at the last value of the list.

how_many_missing([1, 2, 3, 8, 9]) ➞ 4

# The number line starts at 1 and ends at 9 (so the numbers 0 and 10 aren't missing from it).
# The numbers missing from this line are 4, 5, 6, and 7.
# 4 numbers are missing.
Examples
how_many_missing([1, 3]) ➞ 1

how_many_missing([7, 10, 11, 12]) ➞ 2

how_many_missing([1, 3, 5, 7, 9, 11]) ➞ 5

how_many_missing([5, 6, 7, 8]) ➞ 0

Notes
If the number line is complete, or the list is empty, return 0.
"""





################################################################
"""
Solution 1
"""

def how_many_missing(lst):
	return len(lst) and lst[-1] - lst[0] - len(lst) + 1





################################################################
"""
Solution 2
"""

def how_many_missing(lst):
	def missing(lst):
		try:
			start = min(lst)
			end = max(lst) + 1
		
			missed = []
		
			for n in range(start, end):
				if n not in lst:
					missed.append(n)
		except ValueError:
			missed = []
		return missed
	
	missed = missing(lst)
	
	return len(missed)






################################################################
"""
Solution 3
"""

def how_many_missing(lst):
	lst = sorted(lst)
	if len(lst) <= 1:
		return 0
	else:
		a = []
		for k in range(int(lst[0]), int(lst[-1])+1):
			a.append(k)
		return len(a) - len(lst)







#################################################################
"""
Solution 4
"""

def how_many_missing(lst):
	if len(lst) == 0:
		return 0
	else:
# last one - (first one + (len - 1))
		ans = lst[len(lst) - 1] - (lst[0] + (len(lst) -1))
		return ans




