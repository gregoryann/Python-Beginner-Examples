"""
Something in the Box?
Create a function that returns True if an asterisk * is inside a box.

Examples
in_box([
  "###",
  "#*#",
  "###"
]) ➞ True


in_box([
  "####",
  "#* #",
  "#  #",
  "####"
]) ➞ True


in_box([
  "*####",
  "# #",
  "#  #*",
  "####"
]) ➞ false


in_box([
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#####"
]) ➞ False

Notes
The asterisk may be in the array, however, it must be inside the box, if it exists.
"""


"""
Solution 1
"""

def in_box(lst):
	for i in range(1,len(lst)-1):
		for j in range(1,len(lst[i])-1):
			if lst[i][j] == '*':
				return True
	return False


"""
Solution 2
"""

def in_box(lst):
	return "#*#" in [x.replace(' ', '') for x in lst]

"""
Solution 3
"""

def in_box(lst):
	for line in lst:		
		if 0 < line.find('*') < len(line) - 1: return True
	return False


"""
Solution 4
"""

def in_box(lst):
	for r in lst:
		if r.count('*')==1: return True
	return False



