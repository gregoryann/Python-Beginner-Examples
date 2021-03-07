"""

Check if the Same Case
Create a function that returns True if an input string contains only uppercase or only lowercase letters.

Examples
same_case("hello") ➞ True

same_case("HELLO") ➞ True

same_case("Hello") ➞ False

same_case("ketcHUp") ➞ False


"""



"""
Solution 1
"""

def same_case(txt):
	return txt.islower() or txt.isupper()

"""
Solution 2
"""

def same_case(txt):
	return all(i.isupper() for i in txt) or all(i.islower() for i in txt)

"""
Solution 3
"""

def same_case(txt):
	if txt.isupper():
		return True
	elif txt.islower():
		return True
	else:
		return False

"""
Solution 4
"""

def same_case(txt):
	return txt == txt.lower() or txt == txt.upper()




