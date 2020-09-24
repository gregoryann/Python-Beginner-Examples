"""
Automorphic Numbers

A number n is automorphic if n^2 ends in n.

For example: n=5, n^2=25

Create a function that takes a number and returns True if the number is automorphic, False if it isn't.

Examples
is_automorphic(5) ➞ True

is_automorphic(8) ➞ False

is_automorphic(76) ➞ True
"""


"""
Solution 1
"""

def is_automorphic(n):
	return str(n**2).endswith(str(n))

"""
Solution 2
"""

def is_automorphic(n):
	return str(n**2)[-len(str(n)):] == str(n)

"""
Solution 3
"""

def is_automorphic(n):
	print(n)
	print(n**2)
	return str(n)[-len(str(n))] == str(n**2)[-len(str(n))]

"""
Solution 4
"""

def is_automorphic(n):
	if n == 0: return True
	return str(n**2)[-len(str(n)):] == str(n)





