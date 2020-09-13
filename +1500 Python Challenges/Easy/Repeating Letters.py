"""
Repeating Letters

Create a function that takes a string and returns a string in which each character is repeated once.

Examples
double_char("String") ➞ "SSttrriinngg"

double_char("Hello World!") ➞ "HHeelllloo  WWoorrlldd!!"

double_char("1234!_ ") ➞ "11223344!!__  "

Notes
All test cases contain valid strings. Don't worry about spaces, special characters or numbers. They're all considered valid characters.
"""



"""
Solution 1
"""

def double_char(txt):
    return ''.join([c * 2 for c in txt])

"""
Solution 2
"""

def double_char(txt):
	result = ''
  
	for t in txt:
		result += t*2
	return result

"""
Solution 3
"""

def double_char(txt):
    return ''.join(x*2 for x in txt)

"""
Solution 4
"""

def double_char(txt):
    a = []
    for x in txt:
      a.append(x*2)
    return "".join(a)

"""
Solution 5
"""

double_char=lambda x:''.join(i*2for i in x)

"""
Solution 6
"""

def double_char(txt):
	arr = []
	for x in txt:
		arr.append(x+x)
	return ''.join(arr)