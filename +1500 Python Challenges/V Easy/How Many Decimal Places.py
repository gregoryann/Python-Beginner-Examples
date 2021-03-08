"""
How Many Decimal Places?
Create a function that returns the number of decimal places a number has. Any zeros after the decimal point count towards the number of decimal places.

Examples
get_decimal_places("43.20") ➞ 2

get_decimal_places("400") ➞ 0

get_decimal_places("3.1") ➞ 1
Notes
Return 0 if the number doesn't have any decimal places (see example #2).

"""



"""
Solution 1
"""

def get_decimal_places(n):
	return len(n[n.find('.'):]) - 1

"""
Solution 2
"""
def get_decimal_places(n):
	return n[::-1].find('.') if '.' in n else 0

"""
Solution 3
"""
def get_decimal_places(n):
	lst=str(n).split('.')
	del lst[0]
	if lst==[]:
		return 0
	else:
		return len(lst[0])
"""
Solution 4
"""
def get_decimal_places(n):
	string = str(n).split('.')
	if len(string) == 1:
		return 0
	else:
		return len(string[1])




