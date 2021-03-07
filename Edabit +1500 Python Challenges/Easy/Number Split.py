"""
Number Split

Given a number, return a list containing the two halves of the number. If the number is odd, make the rightmost number higher.

Examples
number_split(4) ➞ [2, 2]

number_split(10) ➞ [5, 5]

number_split(11) ➞ [5, 6]

number_split(-9) ➞ [-5, -4]

Notes
All numbers will be integers.
You can expect negative numbers too.
"""



################################################################
"""
Solution 1
"""

import math
def number_split(n):
 x= []
 x.append(math.floor(n/2))
 x.append(math.ceil(n/2))
 return x




################################################################
"""
Solution 2
"""

def number_split(n):
	if n%2 == 0:
		return [n//2,n//2]
	elif n%2 != 0:
		return [n//2,n//2+1]







################################################################
"""
Solution 3
"""

def number_split(n):
	result = []
	if n % 2 == 0: 
		r = n / 2
		for i in range(0, 2): 
			result.append(r)
		
	else: 
		r = (n - 1) / 2
		result.append(r)
		result.append(r + 1)
	
	return result






#################################################################
"""
Solution 4
"""

def number_split(n):
    if n % 2 == 0:
        return [n/2,n/2]
    if n % 2 == 1:
        return [round(n/2-0.5), round(n/2+0.5)]




