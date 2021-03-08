"""

List from Comma-Delimited String
Write a function that turns a comma-delimited list into an array of strings.

Examples
to_array("watermelon, raspberry, orange")
➞ ["watermelon", "raspberry", "orange"]
to_array("x1, x2, x3, x4, x5")
➞ ["x1", "x2", "x3", "x4", "x5"]
to_array("a, b, c, d")
➞ ["a", "b", "c", "d"]
to_array("")
➞ []

Notes
Return an empty list for an empty string.

"""


"""
Solution 1
"""

def to_array(txt):
	return txt.split(', ') if txt else []

"""
Solution 2
"""

def to_array(txt):
	if len(txt) < 1:
		return []
	return txt.replace(" ","").split(",")

"""
Solution 3
"""

to_array=lambda t:t.split(', ')if t.split(', ')!=[''] else[]

"""
Solution 4
"""

def to_array(txt):
	return [] if txt == '' else txt.split(', ')








