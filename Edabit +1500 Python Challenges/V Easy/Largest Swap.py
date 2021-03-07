"""
Largest Swap

Write a function that takes a two-digit number and determines if it's the largest of two possible digit swaps.

To illustrate:

largest_swap(27) ➞ False

largest_swap(43) ➞ True
If 27 is our input, we should return False because swapping the digits gives us 72, and 72 > 27. On the other hand, swapping 43 gives us 34, and 43 > 34.

Examples
largest_swap(14) ➞ False

largest_swap(53) ➞ True

largest_swap(99) ➞ True

Notes
Numbers with two identical digits (third example) should yield True (you can't do better).

"""


"""
Solution 1
"""

def largest_swap(num):
	return num//10 >= num%10

"""
Solution 2
"""

def largest_swap(num):
	return num >= int(str(num)[::-1])

"""
Solution 3
"""

def largest_swap(num):
	new = [str(num)[1], str(num)[0]]
	return num >= int("".join(new))

"""
Solution 4
"""

def largest_swap(num):
		if str(num)[0]==str(num)[1]:
				return True
		else:
				return num > int(str(num)[::-1])


"""
Solution 5
"""

def largest_swap(num):
	return int(str(num)[::-1]) < num if str(num)[0] != str(num)[1] else True

