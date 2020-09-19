"""
Multi-division

Create a function, that will for a given a, b, c, do the following:

Add a to itself b times.
Check if the result is divisible by c.
Examples
abcmath(42, 5, 10) ➞ False
# 42+42 = 84,84+84 = 168,168+168 = 336,336+336 = 672, 672+672 = 1344
# 1344 is not divisible by 10

abcmath(5, 2, 1) ➞ True

abcmath(1, 2, 3) ➞ False

Notes
In the first step of the function, a doesn't always refer to the original a.
"if the result is divisible by c", means that if you divide the result and c, you will get an integer (5, and not 4.5314).
The second test is correct.
"""


"""
Solution 1
"""

def abcmath(a, b, c):
	for i in range(b):
		a+= a
	return a % c == 0

"""
Solution 2
"""

def abcmath(a, b, c):
	while b > 0:
		a += a
		b -= b
	return a % c == 0

"""
Solution 3
"""

def abcmath(a, b, c):
	start = a
	for i in range(b):
		start = start * 2
	return True if start % c == 0 else False


"""
Solution 4
"""

def abcmath(a, b, c):
	total = a
	for i in range(1, b + 1):
		total += total
	if total % c == 0:
		return True
	else:
		return False





