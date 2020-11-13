"""
Remove Repeated Characters

Create a function that will remove any repeated charcter(s) in a word passed to the function. Not just consecutive characters, but characters repeating anywhere in the input.

Examples
unrepeated("hello") ➞ "helo"

unrepeated("aaaaa") ➞ "a"

unrepeated("WWE!!!") ➞ "WE!"

unrepeated("call 911") ➞ "cal 91"

Notes
No more than two words will be passed in the tests.
Input includes special characters and numbers.
"""


################################################################
"""
Solution 1
"""


def unrepeated(s):
  return ''.join(sorted(set(s), key=s.index))



################################################################
"""
Solution 2
"""


def unrepeated(txt):
    nl = []
    for letter in txt:
        if letter not in nl:
            nl.append(letter)
    return ''.join(nl)



################################################################
"""
Solution 3
"""


def unrepeated(txt):
	text = []
	chars = set()
	for char in txt:
		if char not in chars:
			chars.add(char)
			text.append(char)
	return "".join(text)



#################################################################
"""
Solution 4
"""


def unrepeated(txt):
	seen = set()
	result = []
	for letter in txt:
		if letter not in seen:
			result.append(letter)
			seen.add(letter)
	return ''.join(result)


