"""
Lowercase, Uppercase or Mixed?
Create a function which returns "upper" if all the letters in a word are uppercase, "lower" if lowercase and "mixed" for any mix of the two.

Examples
get_case("whisper...") ➞ "lower"

get_case("SHOUT!") ➞ "upper"

get_case("Indoor Voice") ➞ "mixed"
Notes
Ignore punctuation, spaces and numbers.

"""




"""
Solution 1
"""

def get_case(txt):
	return 'upper' if txt.isupper() else 'lower' if txt.islower() else 'mixed'

"""
Solution 2
"""

def get_case(txt):
	if txt.islower(): return 'lower'
	if txt.isupper(): return 'upper'
	return 'mixed'

"""
Solution 3
"""

def get_case(txt):
	if txt == txt.upper():
		return "upper"
	elif txt == txt.lower():
		return "lower"
	else:
		return "mixed"

"""
Solution 4
"""

def get_case(txt):
	a = [ord(x) for x in txt if ord(x)>=65]
	if min(a) > 97:
		return 'lower'
	elif max(a) < 91:
		return 'upper'
	else:
		return 'mixed'




