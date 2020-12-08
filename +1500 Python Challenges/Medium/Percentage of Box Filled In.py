"""
Percentage of Box Filled In
Create a function that calculates what percentage of the box is filled in. Give your answer as a string percentage rounded to the nearest integer.

Examples
percent_filled([
  "####",
  "#  #",
  "#o #",
  "####"
]) ➞ "25%"

# One element out of four spaces.

percent_filled([
  "#######",
  "#o oo #",
  "#######"
]) ➞ "60%"

# Three elements out of five spaces.

percent_filled([
  "######",
  "#ooo #",
  "#oo  #",
  "#    #",
  "#    #",
  "######"
]) ➞ "31%"

# Five elements out of sixteen spaces.


Notes
Only "o" will fill the box and also "o" will not be found outside of the box.
Don't focus on how much physical space an element takes up, pretend that each element occupies one whole unit (which you can judge according to the number of "#" on the sides).
"""





################################################################
"""
Solution 1
"""


def percent_filled(box):
    s = ''.join(box)
    filled = s.count('o')
    return '{:.0%}'.format(filled/(filled + s.count(' ')))



################################################################
"""
Solution 2
"""


def percent_filled(box):
	box = ''.join(box)
	o = box.count('o')
	s = box.count(' ')
	return "{0:.0%}".format(o / (o+s))



################################################################
"""
Solution 3
"""


def percent_filled(box):
	filled_space = sum([c == "o" for row in box for c in row])
	total_space = (len(box) - 2) * (len(box[0]) - 2)
	
	return "{}%".format(round(filled_space / total_space * 100))



#################################################################
"""
Solution 4
"""


percent_filled=lambda m:str(round(100*str(m).count("o")/(len(m)-2)/(len(m[0])-2)))+"%"




