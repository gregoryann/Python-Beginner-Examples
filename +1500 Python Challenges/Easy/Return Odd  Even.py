"""
Return Odd > Even

Given a list, return True if there are more odd numbers than even numbers, otherwise return False.

Examples
oddeven([1, 2, 3, 4, 5, 6, 7, 8, 9]) ➞ True

oddeven([1]) ➞ True

oddeven([13452394823795273847528572346]) ➞ False

Notes
All lists will have at least 1 item.
"""



"""
Solution 1
"""

def oddeven(lst):
	return sum(1 if int(i)%2 else -1 for i in lst) > 0

"""
Solution 2
"""

def oddeven(lst):
	odds = [i for i in lst if i % 2]
	evens = [i for i in lst if not i % 2]
	return len(odds) > len(evens)

"""
Solution 3
"""

def oddeven(lst):
	e = []
	o = []
	for i in lst:
		if i%2 == 0:
			e.append(i)
		else:
			o.append(i)
	if len(o) > len(e):
		return True
	return False







