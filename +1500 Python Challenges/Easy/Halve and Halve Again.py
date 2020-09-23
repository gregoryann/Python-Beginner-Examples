"""
Halve and Halve Again

Given two integers a and b, return how many times a can be halved while still being greater than b.

Examples
halve_count(1324, 98) ➞ 3
# (1324 -> 662 -> 331 -> 165.5)

halve_count(624, 8) ➞ 6
# (624 -> 312 -> 156 -> 78 -> 39 -> 19.5 -> 9.75)

halve_count(1000, 3) ➞ 8
# (1000 -> 500 -> 250 -> 125 -> 62.5 -> 31.25 -> 15.625 -> 7.8125 -> 3.90625)

Notes
Integer a can be halved at least once.
"""



"""
Solution 1
"""

def halve_count(a, b):
	n = 0
	while(a/2>b):
		n += 1
		a /= 2
	return n

"""
Solution 2
"""

halve_count=lambda a,b:len(bin((a-1)//b))-3

"""
Solution 3
"""

def halve_count(a, b):
	counter = 0
	looper = True
	
	while looper == True:
		a = a / 2
		
		if a > b:
			counter = counter + 1
		else:
			looper = False
	return counter






