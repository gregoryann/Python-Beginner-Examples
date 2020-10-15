"""
All About Lambda Expressions: Adding Suffixes

Write a function that returns a lambda expression, which transforms its input by adding a particular suffix at the end.

Examples
add_ly = add_suffix("ly")

add_ly("hopeless") ➞ "hopelessly"
add_ly("total") ➞"totally"

add_less = add_suffix("less")

add_less("fear") ➞ "fearless"
add_less("ruth") ➞ "ruthless"
"""



################################################################
"""
Solution 1
"""


add_suffix = lambda s: lambda x: x + s




################################################################
"""
Solution 2
"""


def add_suffix(suffix):
  y = lambda x: x + suffix
  return y





################################################################
"""
Solution 3
"""


def add_suffix(suffix):
	def suffix_add(string):
		return string + suffix
	return suffix_add










