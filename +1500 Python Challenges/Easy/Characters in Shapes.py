"""
Characters in Shapes

Create a function that counts how many characters make up a rectangular shape. You will be given a list of strings.

Examples
count_characters([
  "###",
  "###",
  "###"
]) ➞ 9

count_characters([
  "22222222",
  "22222222",
]) ➞ 16

count_characters([
  "------------------"
]) ➞ 18

count_characters([]) ➞ 0

count_characters(["", ""]) ➞ 0

Notes
Return 0 if given an empty list.
"""


"""
Solution 1
"""

def count_characters(lst):
  return sum(len(i) for i in lst)

"""
Solution 2
"""

def count_characters(lst):
	return len(''.join(lst))

"""
Solution 3
"""

def count_characters(lst):
	return 0 if not lst else len(lst[0]) * len(lst)

"""
Solution 4
"""

def count_characters(lst):
	if len(lst) == 0:
		return 0
	return len(lst) * len(lst[0])

