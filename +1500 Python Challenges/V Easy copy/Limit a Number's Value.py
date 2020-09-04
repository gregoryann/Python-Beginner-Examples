"""
Limit a Number's Value
Create a function that takes three number arguments — one number as an input and two additional numbers representing the endpoints of a closed range — and return the number limited to this range.

If the number falls within the range, the number should be returned.
If the number is less than the lower limit of the range, the lower limit should be returned.
If the number is greater than the upper limit of the range, the upper limit should be returned.
Examples
limit_number(5, 1, 10) ➞ 5

limit_number(-3, 1, 10) ➞ 1

limit_number(14, 1, 10) ➞ 10

limit_number(4.6, 1, 10) ➞ 4.6
Notes
All test inputs will be valid numbers.
All test inputs' range parameters will be in the correct order (i.e. the lower range will be less than or equal to the upper range).

"""



"""
Solution 1
"""

def limit_number(n,l,h):
	a=[n,l,h]
	a.sort()
	return a[1]

"""
Solution 2
"""

def limit_number(n, low, high):
    return high if n > high else low if n < low else n

"""
Solution 3
"""

def limit_number(num, range_low, range_high):
	if num>range_high:
		return range_high
	elif num<range_low:
		return range_low
	else:
		return num

"""
Solution 4
"""

def limit_number(num, x, y):
	return num if x < num < y else x if num < x else y





