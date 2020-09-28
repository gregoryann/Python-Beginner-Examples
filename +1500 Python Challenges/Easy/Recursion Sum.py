"""
Recursion: Sum

Write a function that finds the sum of the first n natural numbers. Make your function recursive.

Examples
sum_numbers(5) ➞ 15
# 1 + 2 + 3 + 4 + 5 = 15

sum_numbers(1) ➞ 1

sum_numbers(12) ➞ 78

Notes
Assume the input number is always positive.
Check the Resources tab for info on recursion.
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################


"""
Solution 1
"""

def sum_numbers(n):
	return n + sum_numbers(n-1) if n else 0

"""
Solution 2
"""

sum_numbers=lambda n:0if n<1else n+sum_numbers(n-1)

"""
Solution 3
"""

def sum_numbers(n):
	if n==0:
		return 0
	return n+sum_numbers(n-1)








