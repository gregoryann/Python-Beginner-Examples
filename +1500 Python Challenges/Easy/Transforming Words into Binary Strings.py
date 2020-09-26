"""
Transforming Words into Binary Strings

Write a function that transforms all letters from [a, m] to 0 and letters from [n, z] to 1 in a string.

Examples
convert_binary("house") ➞ "01110"

convert_binary("excLAIM") ➞ "0100000"

convert_binary("moon") ➞ "0111"

Notes
Conversion should be case insensitive (see example #2).
"""


"""
Solution 1
"""

def convert_binary(string):
	return ''.join(str(int(x > 'm')) for x in string.lower())

"""
Solution 2
"""

import re
def convert_binary(string):
	return re.sub("[n-zN-Z]", "1", re.sub("[a-mA-M]", "0", string))

"""
Solution 3
"""

def convert_binary(string):
	ret_str = ""
	for c in string.lower():
		if c in "abcdefghijklm":
			ret_str += "0"
		else:
			ret_str += "1"
	return ret_str

"""
Solution 4
"""

def convert_binary(string):
	return ''.join(['0' if 'a' <= l.lower() <= 'm' else '1' for l in string])


"""
Solution 5
"""

def convert_binary(string):
	atom ='abcdefghijklmABCDEFGHIJKLM'
	ans = []
	for x in string:
		if x in atom:
			ans.append('0')
		else:
			ans.append('1')
	return ''.join(ans)

