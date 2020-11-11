"""
The Fifth Argument
Create a function (named fifth) that takes some arguments and returns the type of the fifth argument. In case the arguments were less than 5, return "Not enough arguments".

Examples
fifth(1, 2, 3, 4, 5) ➞ int

fifth("a", 2, 3, [1, 2, 3], "five") ➞ str

fifth() ➞ "Not enough arguments"

Notes
Don't get confused between zero-indexing and one-indexing.
If you get stuck check the Resources tab.
"""




################################################################
"""
Solution 1
"""


def fifth(*args):
	myans = []
	for i in args:
		myans.append(i)
	if len(myans) < 5:
		return 'Not enough arguments'
	return type(myans[4])



################################################################
"""
Solution 2
"""


def fifth(*args):
	return type(args[4]) if len(args)>=5 else "Not enough arguments"







