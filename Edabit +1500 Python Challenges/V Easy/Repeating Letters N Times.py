"""
Repeating Letters N Times

Create a function that repeats each character in a string n times.

Examples
repeat("mice", 5) ➞ "mmmmmiiiiiccccceeeee"
repeat("hello", 3) ➞ "hhheeellllllooo"
repeat("stop", 1) ➞ "stop"

"""


"""
Solution 1
"""

def repeat(txt, n):
	return ''.join(s*n for s in txt)

"""
Solution 2
"""

def repeat(txt, n):
	lst = []
	for i in txt:
		lst.append(i * n)
	newLst = "".join(lst)
	return newLst

"""
Solution 3
"""

def repeat(txt, n):
	return "".join(list(map(lambda s: s*n, txt)))





