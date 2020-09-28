"""
Basic Calculator
Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers.

Examples
calculator(2, "+", 2) ➞ 4

calculator(2, "*", 2) ➞ 4

calculator(4, "/", 2) ➞ 2

Notes
If the input tries to divide by 0, return: "Can't divide by 0!"
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def calculator(n1, operator, n2):
	try: 
		return eval(str(n1)+operator+str(n2))
	except ZeroDivisionError:
		return "Can't divide by 0!"

"""
Solution 2
"""

def calculator(num1, operator, num2):
	if operator == '/' and num2 == 0:
		return "Can't divide by 0!"
	return eval('num1' + operator + 'num2')

"""
Solution 3
"""

def calculator(num1, operator, num2):
	try:
		return eval("{}{}{}".format(num1, operator, num2))
	except ZeroDivisionError:
		return "Can't divide by 0!"

"""
Solution 4
"""

def calculator(num1, operator, num2):
    try:
        return eval("%s %s %s" % (str(num1),str(operator), str(num2)))
    except ZeroDivisionError:
        return "Can't divide by 0!"






