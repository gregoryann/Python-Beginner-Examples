"""
Smaller String Number
Create a function that returns the smaller number.

Examples
smaller_num("21", "44") ➞ "21"
smaller_num("1500", "1") ➞ "1"
smaller_num("5", "5") ➞ "5"

Notes
Numbers will be represented as strings, and your output should also be a string.
If both numbers tie, return either number.
Numbers will be positive.
Bonus: See if you can do this without converting to integers.

"""

#############################################################


"""
Solution 1
"""

def smaller_num(n1, n2):
	return min(n1, n2, key=int)

"""
Solution 2
"""

# with Bonus (no integer conversion)
def smaller_num(n1, n2):
	a, b = sorted((n1, n2), key=len)
	return sorted((a.rjust(len(b), '0'), b))[0].lstrip('0')

"""
Solution 3
"""

def smaller_num(n1, n2):
	x = [n1, n2]
	x.sort(key=int)
	return x[0]

"""
Solution 4
"""

def smaller_num(n1, n2):
	lista_str = [n1, n2]
	lista = list(map(int, lista_str))
	return str(min(lista))




