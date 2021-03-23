"""
Hashtag Generator

Create a function that is a Hashtag Generator by using the following rules:

The output must start with a hashtag (#).
Each word in the string must have its first letter capitalized.
If the final result, a single string, is longer than 140 characters, the function should return false.
If either the input (str) or the result is an empty string, the function should return false.
Examples
generate_hashtag("    Hello     World   " ) ➞ "#HelloWorld"

generate_hashtag("") ➞ false, "Expected an empty string to return false"

generate_hashtag("Edabit Is Great") ➞ "#EdabitIsGreat", "Should
"""



################################################################
"""
Solution 1
"""


def generate_hashtag(txt):
	txt = txt.title().replace(" ", "")
	return '#' + txt if 0 < len(txt) < 140 else False



################################################################
"""
Solution 2
"""


def generate_hashtag(txt):
	res = '#'
	for i in txt.split():
		res+=i[0].upper()+i[1:]
	return res if 1<len(res)<=140 else False



################################################################
"""
Solution 3
"""


def generate_hashtag(txt: str):
	result = ''.join(map(str.capitalize, txt.split()))
	if len(result) == 0 or len(result) >= 140:
		return False
	return '#' + result



################################################################
"""
Solution 4
"""


import re
def generate_hashtag(txt):
	if txt:
		A=re.findall(r'(?i)[a-z]+', txt)
		if A:
			res=''.join([x.capitalize() for x in A])
			return '#'+res if len(res)<140 else False
		else:
			return False
	else:
		return False





