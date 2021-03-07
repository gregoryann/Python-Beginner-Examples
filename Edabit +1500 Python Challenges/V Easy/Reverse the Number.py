"""
Reverse the Number
Create a function that takes an integer n and reverses it.

Examples
rev(5121) ➞ "1215"

rev(69) ➞ "96"

rev(-122157) ➞ "751221"
Notes
This challenge is about using two operators that are related to division.
If the number is negative, treat it like it's positive.

"""


"""
Solution 1
"""

def rev(n):
	return str(abs(n))[::-1]

"""
Solution 2
"""

def rev(n):
	return str(n)[::-1].strip('-')

"""
Solution 3
"""

def rev(n):
    num = [i for i in str(abs(n))]
    return "".join(num[::-1])

"""
Solution 4
"""

def rev(n):
	if n<0:
		return str(n)[:0:-1]
	else:
		return str(n)[::-1]





