"""
Box Completely Filled?

Create a function that checks if the box is completely filled with the asterisk symbol *.

Examples
completely_filled([
  "#####",
  "#***#",
  "#***#",
  "#***#",
  "#####"
]) ➞ True

completely_filled([
  "#####",
  "#* *#",
  "#***#",
  "#***#",
  "#####"
]) ➞ False

completely_filled([
  "###",
  "#*#",
  "###"
]) ➞ True

completely_filled([
  "##",
  "##"
]) ➞ True

Notes
Boxes of size n <= 2 are considered automatically filled (see example #4).
"""



################################################################
"""
Solution 1
"""


def completely_filled(lst):
	return not any(' ' in i for i in lst)


################################################################
"""
Solution 2
"""


completely_filled=lambda x:' 'not in''.join(x)


################################################################
"""
Solution 3
"""


def completely_filled(lst):
	value = True
	if len(lst) > 2:
		for item in lst[1:-1]:
			for alpha in item[1:-1]:
				if not alpha == "*":
					value = False
		return value
	else:
		return value



#################################################################
"""
Solution 4
"""


def completely_filled(lst):
    
    needed_things = (len(lst) - 2) ** 2 if len(lst) > 1 else 0
    present_things = sum(row.count('*') for row in lst)

    return needed_things == present_things



