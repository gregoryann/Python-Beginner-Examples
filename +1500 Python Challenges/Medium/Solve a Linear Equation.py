"""
Solve a Linear Equation

Create a function that returns the value of x (the "unknown" in the equation). Each equation will be formatted like this:

x + 6 = 12
Examples
solve("x + 43 = 50") ➞ 7

solve("x - 9 = 10") ➞ 19

solve("x + 300 = 100") ➞ -200


Notes
"x" will always be in the same place (you will not find an equation like 6 + x = 12).
Every equation will include either subtraction (-) or addition (+).
"x" may be negative.
"""



################################################################
"""
Solution 1
"""


def solve(eq):
	return -eval(eq[1:].replace("=", "-"))



################################################################
"""
Solution 2
"""


def solve(eq):
	pieces = eq.split()
	a,b = int(pieces[4]), int(pieces[2])
	if pieces[1] == '+': return a-b
	else: return a+b


################################################################
"""
Solution 3
"""


import re
def solve(e):
	l=re.search(r'[+-]*\d+ = [+-]*\d+',e).group(0).split('=')
	return eval(l[1]+'-'+l[0]if'+'in e else l[1]+'+'+l[0])




#################################################################
"""
Solution 4
"""


def solve(eq):
	a = eq.strip("x").replace("=","").split()
	return int(a[2])-int(a[0]+a[1]) if int(a[1]) > 0 else int(a[2])-int(a[1])




