"""
Same ASCII?

Return True if the sum of ASCII values of the first string is same as the sum of ASCII values of the second string, otherwise return False.

Examples
same_ascii("a", "a") ➞ True

same_ascii("AA", "B@") ➞ True

same_ascii("EdAbIt", "EDABIT") ➞ False

Notes
If you need some help with ASCII codes, check the Resources tab for an image of all ASCII codes used in this challenge.
"""



################################################################
"""
Solution 1
"""

def same_ascii(a, b):
	return sum([ord(x) for x in a]) == sum([ord(x) for x in b])





################################################################
"""
Solution 2
"""

import functools as ft

def same_ascii(a,b):
    sum_first = ft.reduce(lambda x,y: x+ord(y), a, 0)
    sum_second = ft.reduce(lambda x,y: x+ord(y), b, 0)
    return sum_first == sum_second






################################################################
"""
Solution 3
"""

def same_ascii(a, b):
	arr_1 = sorted(a)
	arr_2 = sorted(b)
	
	asci_a = [ord(i) for i in arr_1]
	asci_b = [ord(d) for d in arr_2]
	
	return sum(asci_a) == sum(asci_b)








#################################################################
"""
Solution 4
"""

def same_ascii(a, b):
	a_sum, b_sum = 0, 0
	for i in range(len(a)):
		a_sum += ord(a[i:i+1])
	for j in range(len(b)):
		b_sum += ord(b[j:j+1])
	return True if a_sum==b_sum else False




