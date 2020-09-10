"""
Return the Four Letter Strings

Create a function that takes a list of strings and returns the words that are exactly four letters.

Examples
is_four_letters(["Tomato", "Potato", "Pair"]) ➞ ["Pair"]

is_four_letters(["Kangaroo", "Bear", "Fox"]) ➞ ["Bear"]

is_four_letters(["Ryan", "Kieran", "Jason", "Matt"]) ➞ ["Ryan", "Matt"]

Notes
You can expect valid strings for all test cases.

"""


"""
Solution 1
"""

def is_four_letters(lst):
  return [word for word in lst if len(word) == 4]

"""
Solution 2
"""

def is_four_letters(lst):
	ls = []
	for w in lst:
		if len(w) == 4:
			ls.append(w)
	return ls

"""
Solution 3
"""

def is_four_letters(lst):
  return list(filter(lambda str: len(str)==4, lst))

"""
Solution 4
"""

def is_four_letters(lst):
  newLst = []
  for x in lst :
    if(len(x) == 4): newLst.append(x)
  return newLst

"""
Solution 5
"""

is_four_letters=lambda l:[s for s in l if len(s)==4]


