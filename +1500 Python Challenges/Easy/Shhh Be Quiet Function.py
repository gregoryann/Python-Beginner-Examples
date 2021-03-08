"""
Shhh Be Quiet Function

Write a function that removes all capitals letters from a sentence except the first letter, put quotation marks around the sentence and add ", whispered Edabit." at the end.

Examples
shhh("HI THERE!") ➞ '"Hi there!", whispered Edabit.'

shhh("tHaT'S Pretty awesOme") ➞ '"That's pretty awesome", whispered Edabit.'

shhh("") ➞ '"", whispered Edabit.'

Notes
Don't forget to surround the original string with double quotation marks "".
"""



########################################################################




"""
Solution 1
"""

def shhh(txt):
	return '"{}", whispered Edabit.'.format(txt.capitalize())

"""
Solution 2
"""

def shhh(txt):
  return '"%s", whispered Edabit.' % txt.capitalize()

"""
Solution 3
"""

def shhh(s):
	s = '"{}", whispered Edabit.'.format(s.lower())
	return s[0] + s[1].upper() + s[2:]

"""
Solution 4
"""

def shhh(txt):
	remove_capitals = txt[1:].lower()
	capitalize = txt[:1].capitalize()
	return '"' + capitalize + remove_capitals + '"' + ', whispered Edabit.'

"""
Solution 5
"""

def shhh(txt):
    lower = txt.lower()
    capitalize = lower.capitalize()
    string = '"{}", whispered Edabit.'.format(capitalize)
    return string


