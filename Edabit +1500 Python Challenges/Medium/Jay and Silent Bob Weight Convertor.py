"""
Jay and Silent Bob Weight Convertor

Jay and Silent Bob have been given a fraction of an ounce but they only understand grams. Convert a fraction passed as a string to grams with up to two decimal places. An ounce weighs 28 grams.

Examples
jay_and_bob("half") ➞ "14 grams"

jay_and_bob("quarter") ➞ "7 grams"

jay_and_bob("eighth") ➞ "3.5 grams"

Notes
Add the string "grams" to the end with a space.
"""


################################################################
"""
Solution 1
"""


def jay_and_bob(t):
	n=round(14/{'q':2,'e':4,'s':8}.get(t[0],1),2)
	return'%s grams'%(n%1and n or int(n))



################################################################
"""
Solution 2
"""


def jay_and_bob(txt):
  if txt=="half": return "{} grams".format(28//2)
  elif txt=="quarter": return "{} grams".format(28//4)
  elif txt=="eighth": return "{} grams".format(28/8)
  else: return "{} grams".format(28/16)



################################################################
"""
Solution 3
"""


def jay_and_bob(txt):
  d = {"half": .5, "quarter": .25, "eighth": .125, "sixteenth": .0625}
  num = str(round(28 * d[txt], 2))
  return "{} grams".format(num.split(".")[0] if num.endswith(".0") else num)



#################################################################
"""
Solution 4
"""


frac_dict = {
		'half': 2,
		'quarter': 4,
		'eighth': 8,
		'sixteenth': 16
	}
def jay_and_bob(txt):
	calc = 28 % frac_dict[txt]
	if not calc:
		return str(28 // frac_dict[txt]) + ' grams'
	else:
		return str(28 / frac_dict[txt]) + ' grams'



