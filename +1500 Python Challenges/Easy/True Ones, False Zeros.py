"""
True Ones, False Zeros

Create a function which returns a list of booleans, from a given number. Iterating through the number one digit at a time, append True if the digit is 1 and False if it is 0.

Examples
integer_boolean("100101") ➞ [True, False, False, True, False, True]

integer_boolean("10") ➞ [True, False]

integer_boolean("001") ➞ [False, False, True]

Notes
Expect numbers with 0 and 1 only.
"""


##########################################################################



"""
Solution 1
"""

def integer_boolean(n):
	return [i == '1' for i in str(n)]

"""
Solution 2
"""

def integer_boolean(n):
	return [bool(int(i)) for i in n]

"""
Solution 3
"""

def integer_boolean(n):
	list = []
	
	for i in n:
		if i == '1':
			list.append(True)
			
		elif i == '0':
			list.append(False)
		
	return list

"""
Solution 4
"""

integer_boolean = lambda n: [bool(int(x)) for x in str(n)]




