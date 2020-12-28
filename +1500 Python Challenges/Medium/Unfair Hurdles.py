"""
Unfair Hurdles

Unfair hurdles are hurdles which are either too high, or way too close together.

Create a function which takes in a list of strings, representing hurdles, and return whether they are unfair. For the purposes of this challenge, unfair hurdles are:

At least 4 characters tall.
Strictly less than 4 spaces apart.
Examples
# Hurdle are good distance apart but are way too tall.

is_unfair_hurdle([
  "#    #    #    #",
  "#    #    #    #",
  "#    #    #    #",
  "#    #    #    #"
]) ➞ True


# Hurdles are a fine height but are way too close together.

is_unfair_hurdle([
  "#  #  #  #",
  "#  #  #  #",
  "#  #  #  #"
]) ➞ True


# These hurdles are mighty splendid.

is_unfair_hurdle([
  "#      #      #      #",
  "#      #      #      #"
]) ➞ False


Notes
Hurdles will be represented with a hashtag "#".
There will be the same spacing between hurdles.
Hurdles are always as high as the length of the list.
Hurdles are always evenly spaced.
"""




################################################################
"""
Solution 1
"""


def is_unfair_hurdle(hurdles):
	return len(hurdles) > 3 or len(hurdles[0].split('#')[1]) < 4



################################################################
"""
Solution 2
"""


def is_unfair_hurdle(hurdles):
	return len(hurdles)>=4 or int(hurdles[0].count(" ")/(hurdles[0].count("#")-1))<


################################################################
"""
Solution 3
"""


import re


def is_unfair_hurdle(hurdles):
    if len(hurdles) > 3:
        return True
    for hurdle in hurdles:
        unfair = re.findall(r"# {0,3}#", hurdle)
        if unfair:
            return True
    return False



#################################################################
"""
Solution 4
"""


def is_unfair_hurdle(hurdles):
	if len(hurdles) >= 4:
		return True
	else:
		h = hurdles[0].count("#")
		s = 0
		for k in range(0, len(hurdles[0])):
			if hurdles[0][k].isspace():
				s += 1
		if s/(h-1) >= 4:
			return False
		else:
			return True



