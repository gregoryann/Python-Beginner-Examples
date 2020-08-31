"""
Recreating a len() Function
Create a function which returns the length of a string, without using len().

Examples
length("Hello World") ➞ 11

length("Edabit") ➞ 6

length("wash your hands!") ➞ 16

"""


"""
Solution 1
"""

def length(s):
	return sum(1 for i in s)

"""
Solution 2
"""

length = lambda x: x.__len__()#lol

"""
Solution 3
"""

length=lambda s:sum(map(bool,s))

"""
Solution 4
"""






