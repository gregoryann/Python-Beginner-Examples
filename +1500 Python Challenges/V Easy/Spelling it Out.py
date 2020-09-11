"""
Spelling it Out

Create a function which takes in a word and spells it out, by consecutively adding letters until the full word is completed.

Examples
spelling("bee") ➞ ["b", "be", "bee"]

spelling("happy") ➞ ["h", "ha", "hap", "happ", "happy"]

spelling("eagerly") ➞ ["e", "ea", "eag", "eage", "eager", "eagerl", "eagerly"]

"""


"""
Solution 1
"""

def spelling(txt):
	return [txt[:i + 1] for i in range(len(txt))]

"""
Solution 2
"""

def spelling(str):
	a = []
	for i in range(len(str)):
		a.append(str[0:i+1])
	return a

"""
Solution 3
"""

def spelling(txt):
	result = []
	temp = ''
	for i in range(len(txt)):
		temp += txt[i]
		result.append(temp)
	return result

"""
Solution 4
"""

def spelling(txt):
	output = ''
	return [''.join(txt[:x+1]) for x in range(len(txt))]





