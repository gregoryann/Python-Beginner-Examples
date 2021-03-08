"""
Count the Number of Duplicate Characters

Create a function that returns the amount of duplicate characters in a string. It will be case sensitive and spaces are included. If there are no duplicates, return 0.

Examples
duplicates("Hello World!") ➞ 3
# "o" = 2, "l" = 3.
# "o" is duplicated 1 extra time and "l" is duplicated 2 extra times.
# Hence 1 + 2 = 3

duplicates("foobar") ➞ 1

duplicates("helicopter") ➞ 1

duplicates("birthday") ➞ 0
# If there are no duplicates, return 0

Notes
Make sure to only start counting the second time a character appears.
"""



################################################################
"""
Solution 1
"""


def duplicates(txt):
	return len(txt) - len(set(txt))



################################################################
"""
Solution 2
"""


duplicates=lambda s:len(s)-len(set(s))


################################################################
"""
Solution 3
"""


def duplicates(txt):
	dup_num = 0
	set_of_chars = set()
	for char in txt:
		if char in set_of_chars:
		  dup_num += 1
		set_of_chars.add(char)
		
	return dup_num


#################################################################
"""
Solution 4
"""


def duplicates(txt):
	count = 0
	duplicates = []
	for char in txt:
		if txt.count(char) > 1 and char not in duplicates:
			duplicates.append(char)
			count += txt.count(char) - 1
	return count



