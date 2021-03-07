"""
Drunken Python

Python got drunk and the built-in functions str() and int() are acting odd:

str(4) ➞ 4

str("4") ➞ 4

int("4") ➞ "4"

int(4) ➞ "4"
You need to create two functions to substitute str() and int(). A function called int_to_str() that converts integers into strings and a function called str_to_int() that converts strings into integers.

Examples:
int_to_str(4) ➞ "4"

str_to_int("4") ➞ 4

int_to_str(29348) ➞ "29348"

Notes
This is meant to illustrate the dangers of using already-existing function names.
Extra points if you can de-drunk Python.
"""





################################################################
"""
Solution 1
"""


def int_to_str(num):
	return '{}'.format(num)

def str_to_int(num):
	return round(float(num))



################################################################
"""
Solution 2
"""


def int_to_str(num):
	z = str(num)
	print(z)
	return int(z)

def str_to_int(num):
	s = int(num)
	return str(s)
    
