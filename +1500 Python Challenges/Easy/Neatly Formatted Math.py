"""

Neatly Formatted Math

Given a simple math expression as a string, neatly format it as an equation.

Examples
format_math("3 + 4") ➞ "3 + 4 = 7"

format_math("3 - 2") ➞ "3 - 2 = 1"

format_math("4 x 5") ➞ "4 x 5 = 20"

format_math("6 / 3") ➞ "6 / 3 = 2"

Notes
You will need to deal with addition, subtraction, multiplication and division.
Division will have whole number answers (and will obviously not involve 0).
"""





################################################################
"""
Solution 1
"""

def format_math(expr):
	v = eval(expr.replace('x','*').replace('/','//'))
	return '{} = {}'.format(expr, v)





################################################################
"""
Solution 2
"""

def format_math(expr):
    try:
        z = eval(expr)
        return expr + " = " + str(int(z))
    except:
        s=expr.split(" ")
        x= int(s[0]) * int(s[2])
        return expr + " = " + str(int(x))







################################################################
"""
Solution 3
"""


def format_math(expr):
	lst = expr.split()
	if lst[1] == "+":
		fin =  int(lst[0]) + int(lst[2])
	if lst[1] == "-":
		fin = int(lst[0]) - int(lst[2])
	if lst[1] == "x":
		fin = int(lst[0]) * int(lst[2])
	if lst[1] == "/":
		fin = int(lst[0]) // int(lst[2])
	return "{0} {1} {2} = {3}".format(lst[0],lst[1],lst[2],fin)








#################################################################
"""
Solution 4
"""

def format_math(expr):
    answer = eval(expr.replace("x", "*"))
    if answer % 1 == 0:
        answer = int(answer)

    return expr + " = " + str(answer)




