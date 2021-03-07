"""
Sum Fractions

Create a function that takes a list containing nested lists as an argument. Each sublist has 2 elements. The first element is the numerator and the second element is the denominator. Return the sum of the fractions rounded to the nearest whole number.

Examples
sum_fractions([[18, 13], [4, 5]]) ➞ 2

sum_fractions([[36, 4], [22, 60]]) ➞ 9

sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]) ➞ 11

Notes
Your result should be a number not string.
"""



################################################################
"""
Solution 1
"""


def sum_fractions(lst):
	return round(sum(n/d for n, d in lst))





################################################################
"""
Solution 2
"""


def sum_fractions(lst):
	total = 0
	for i in lst: 
		total += i[0] / i[1]
	return round(total, 0)






################################################################
"""
Solution 3
"""


def sum_fractions(lst):
	s = 0
	for i in lst:
			s = s+(i[0]/i[1])
	return round(s)





#################################################################
"""
Solution 4
"""


def sum_fractions(lst):
	nlst = []
	for i in lst:
		add = []
		for j in i:
			add.append(j)
		dvd = add[0] / add[1]
		nlst.append(dvd)
	return round(sum(nlst))



