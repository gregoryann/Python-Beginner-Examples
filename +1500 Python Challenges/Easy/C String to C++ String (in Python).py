"""
C String to C++ String (in Python)

This is a list of single characters with an unwanted character at the end:

["H", "e", "l", "l", "o", "!", "\0"]
You could also just type "Hello!" when initializing a variable, creating the string "Hello!"

Create a function that will return a string by combining the given character list, not including the unwanted final character.

Examples
cpp_txt(["H", "i", "!", "\0"]) ➞ "Hi!"

cpp_txt(["H", "e", "l", "l", "o", "!", "\0"]) ➞ "Hello!"

cpp_txt(["J", "A", "V", "a", "\0"]) ➞ "JAVa"

Notes
This is a translation of a C++ challenge and is trivial in Python, but perhaps it will be helpful to someone out there. (No challenge is trivial until you know how to solve it :)
"""



################################################################
"""
Solution 1
"""


def cpp_txt(lst):
	return "".join(lst[:-1])
#or return "".join(lst).replace("\0","")
#or lst.remove("\0")
#	return "".join(lst)
#or	lst.pop()
#	return "".join(lst)





################################################################
"""
Solution 2
"""


def cpp_txt(l):
  del l[-1]
  return ''.join(l)






################################################################
"""
Solution 3
"""


cpp_txt = lambda l:''.join(l[:-1])







#################################################################
"""
Solution 4
"""


def cpp_txt(lst):
	lst.pop()
	a="".join(lst)
	return a






#################################################################
"""
Solution 5
"""


def cpp_txt(lst):
    return ''.join((i) for i in lst if i.isalpha() or i != '\0')







    
#################################################################
"""
Solution 6
"""

def cpp_txt(lst):
	lst.remove('\0')
	s = ''.join(lst)
	return s