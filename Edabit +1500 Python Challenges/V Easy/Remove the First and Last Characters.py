"""
Remove the First and Last Characters
Create a function that removes the first and last characters from a string.

Examples:
remove_first_last("hello") ➞ "ell"
remove_first_last("maybe") ➞ "ayb"
remove_first_last("benefit") ➞ "enefi"
remove_first_last("a") ➞ "a"

Notes
For words with two or fewer letters (including an empty string), return the string itself (see example #4).

"""



"""
Solution 1
"""

def remove_first_last(txt):
	return txt if len(txt) < 3 else txt[1:-1]

"""
Solution 2
"""

def remove_first_last(txt):
		if len(txt)<=2:
			return txt
		else:
			return txt[1:-1]

"""
Solution 3
"""
def remove_first_last(txt):
	if len(txt)>2:return txt[1:-1]
	else: return txt

"""
Solution 4
"""
def remove_first_last(string):
    if len(string) <= 2:
            return string
    return string[1:-1]




