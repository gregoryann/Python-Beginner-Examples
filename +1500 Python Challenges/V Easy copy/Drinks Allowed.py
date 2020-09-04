"""

Drinks Allowed?
A bartender is writing a simple program to determine whether he should serve drinks to someone. He only serves drinks to people 18 and older and when he's not on break.

Given the person's age, and whether break time is in session, create a function which returns whether he should serve drinks.

Examples
should_serve_drinks(17, True) ➞ False

should_serve_drinks(19, False) ➞ True

should_serve_drinks(30, True) ➞ False
Notes
Return True or False.
Some countries have a slightly higher drinking age, but for the purposes of this challenge, it will be 18.

"""



"""
Solution 1
"""

def should_serve_drinks(age, on_break):
	return age >= 18 and not on_break


"""
Solution 2
"""

should_serve_drinks = lambda a,b: a >= 18 and b == False


"""
Solution 3
"""

def should_serve_drinks(age, on_break):
	if age >= 18 and on_break == False:
		return True
	else:
		return False


"""
Solution 4
"""

def should_serve_drinks(age, on_break):
	if age < 18 and on_break == True:
		return False
	if age > 18 and on_break == True:
		return False
	if age < 18 and on_break == False:
		return False
	else:
		return True





