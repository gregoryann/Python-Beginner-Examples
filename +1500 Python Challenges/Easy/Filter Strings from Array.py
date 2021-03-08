"""

Filter Strings from Array
Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.

Examples
filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]

filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]

filter_list(["Nothing", "here"]) ➞ []

Notes
Don't overthink this one.
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################


"""
Solution 1
"""

def filter_list(l):
  return [i for i in l if type(i)==int]

"""
Solution 2
"""

def filter_list(l):
	new = []
	for el in l:
		if type(el) == type(1):
			new.append(el)
	return new

"""
Solution 3
"""

filter_list=lambda l:[e for e in l if 0*e==0]

"""
Solution 4
"""

def filter_list(l):
	new = []
	for x in l:
		if str(x).lstrip("-+").isdigit():
			new.append(x)
	return new




