"""
Add, Subtract, Multiply or Divide?
Write a function that takes two numbers and returns if they should be added, subtracted, multiplied or divided to get 24. If none of the operations can give 24, return None.

Examples
operation(15, 9) ➞ "added"

operation(26, 2) ➞ "subtracted"

operation(11, 11) ➞ None
Notes
Only integers are used as test input.
Numbers should be added, subtracted, divided or multiplied in the order they appear in the parameters.
The function should return either "added", "subtracted", "divided", "multiplied" or None.
"""




"""
Solution 1
"""

def operation(a, b):
	return {a+b: "added", a-b: "subtracted", a*b: "multiplied", a/b: "divided"}.get(24)


"""
Solution 2
"""

def operation(num1, num2):
	dd = {(num1+num2): 'added', (num1-num2): 'subtracted', (num1*num2): 'multiplied', (num1/num2): 'divided'}
	if 24 in dd.keys():
		return dd[24]
	else:
		return None

"""
Solution 3
"""

def operation(num1, num2):
	if num1 + num2 == 24:
		return 'added'
	elif num1 - num2 == 24 or num2 - num1 == 24:
		return "subtracted"
	elif num1 / num2 == 24 or num2 / num1 == 24:
		return 'divided'
	elif num1 * num2 == 24:
		return 'multiplied'
	else:
		return None


"""
Solution 4
"""

def operation(num1, num2):
		if num1  + num2 == 24: return "added"
		if num1  - num2 == 24: return "subtracted"
		if num1  * num2 == 24: return "multiplied"
		if num1  / num2 == 24: return "divided"
		return


"""
Solution 5
"""


def operation(num1, num2):
	l={'added':(num1+num2),'subtracted':(num1-num2),'multiplied':(num1*num2),'divided':(num1//num2)}
	if any(i==24 for i in l.values()) :
		keys = [key  for (key, value) in l.items() if value == 24]
		return keys[0]


