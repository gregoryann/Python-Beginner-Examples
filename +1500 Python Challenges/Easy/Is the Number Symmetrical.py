"""
Is the Number Symmetrical?

Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse.

Examples
is_symmetrical(7227) ➞ True

is_symmetrical(12567) ➞ False

is_symmetrical(44444444) ➞ True

is_symmetrical(9939) ➞ False

is_symmetrical(1112111) ➞ True
"""


"""
Solution 1
"""

def is_symmetrical(num):
	return str(num) == str(num)[::-1]

"""
Solution 2
"""

def is_symmetrical(n): return str(n) == str(n)[::-1]

"""
Solution 3
"""

def is_symmetrical(num):
    x = list(str(num))
    y = list(reversed(str(num)))
    if x != y:
        return False
    else:
        return True

"""
Solution 4
"""

is_symmetrical=lambda n:str(n)==str(n)[::-1]





