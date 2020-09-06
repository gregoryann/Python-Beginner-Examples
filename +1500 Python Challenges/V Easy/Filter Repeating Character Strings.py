"""
Filter Repeating Character Strings
Create a function that keeps only strings with repeating identical characters (in other words, it has a set size of 1).

Examples
identical_filter(["aaaaaa", "bc", "d", "eeee", "xyz"])
➞ ["aaaaaa", "d", "eeee"]

identical_filter(["88", "999", "22", "545", "133"])
➞ ["88", "999", "22"]

identical_filter(["xxxxo", "oxo", "xox", "ooxxoo", "oxo"])
➞ []

Notes
A string with a single character is trivially counted as a string with repeating identical characters.
If there are no strings with repeating identical characters, return an empty array (see example #3).

"""

"""
Solution 1
"""

def identical_filter(lst):
	return [i for i in lst if len(set(i)) == 1]

"""
Solution 2
"""

def identical_filter(lst):
    return [x for x in lst if x.count(x[0]) == len(x)]

"""
Solution 3
"""

def identical_filter(lst):
	result = []
	for i in lst:
		if len(set(i)) == 1:
			result.append(i)
	return result


"""
Solution 4
"""

def identical_filter(lst):
	a = []
	for i in lst:
		if sorted(i) == sorted(i,reverse=True):
			a.append(i)
	return a


"""
Solution 5
"""

def identical_filter(lst):
	return [x for x in lst if len(x) == 1 or all(i == x[0] for i in x)]

