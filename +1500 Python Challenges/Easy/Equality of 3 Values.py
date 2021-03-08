"""
Equality of 3 Values

Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.

Examples
equal(3, 4, 3) ➞ 2

equal(1, 1, 1) ➞ 3

equal(3, 4, 1) ➞ 0 

Notes
Your function must return 0, 2 or 3.
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""

def equal(a, b, c):
	uniq= set([a,b,c])
	if len(uniq)==3:
		return 0
	else:
		return (4 - len(uniq))

"""
Solution 2
"""

def equal(a, b, c):
	return 3 if a == b == c else 0 if c != a != b != c else 2

"""
Solution 3
"""

def equal(a, b, c):
	lst = [a,b,c]
	answer = max([ lst.count(x) for x in [a,b,c] ])
	return answer if answer != 1 else 0


"""
Solution 4
"""

def equal(a, b, c):
	count = 0
	if a == b or b==c or a==c:
		count += 2
	if a == b == c:
		count += 1
	return count


"""
Solution 5
"""



equal = lambda a, b, c: {3: 3, 1: 2, 0: 0}[(a==b)+(b==c)+(a==c)]