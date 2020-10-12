"""
Operations

Write a function that does the following things: adding, subtracting, dividing, or multiplying values. It is simply referred to as variable operation variable. Of course, the variables have to be defined, but in this challenge, the variable will be defined for you. All you have to do is look at the variable, do some string to integer conversions use some if conditionals, and combine them based on the operation.

The numbers and operation will be given as a string, and you should return the value as a string as well.

Examples
operation("1", "2", "add" ) ➞ "3"

operation("4", "5", "subtract") ➞ "-1"

operation("6", "3", "divide") ➞ "2"

Notes
The numbers and operation will be given as a string, and you should also return the value as a string.
If the answer is "undefined", return "undefined" (e.g. dividing by zero).
For divide go ahead and round down to an integer.
"""



################################################################
"""
Solution 1
"""


def operation(a,b,o):
	try:return str(round(eval(a+{'a':'+','s':'-','d':'/','m':'*'}[o[0]]+b)))
	except:return'undefined'





################################################################
"""
Solution 2
"""


def operation(a, b, op) :
	ops = {'add':'+', 'subtract':'-', 'multiply':'*', 'divide':'/'}
	try:
		return str(round(eval(a + ops[op] + b)))
	except ZeroDivisionError:
		return 'undefined'






################################################################
"""
Solution 3
"""


def operation(a, b, op) :
	try: return str(eval('{}{}{}'.format(a, {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '//'}[op], b)))
	except: return 'undefined'





#################################################################
"""
Solution 4
"""


def operation(a, b, op):
  if b == "0" and op == "divide":
    return "undefined"
  sign = {
		"add": '+',
		"subtract": '-',
		"multiply": '*',
		"divide": '/',
		}
  return str(round(eval("".join([a, sign[op], b]))))





