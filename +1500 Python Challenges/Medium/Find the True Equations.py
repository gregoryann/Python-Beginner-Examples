"""
Find the True Equations

In this challenge you will be given a list containing equations, with each equation written as a string. Here's an example:

["1+1=2", "2+2=3", "5*5=10", "3/3=1"]
If you do the math, you'll see that the equations "1+1=2" and "3/3=1" are actually true while "2+2=3" and "5*5=10" are false nonsense.

Write a function which, given a list of equations as above, returns only the true equations. For instance, for the example above the output should be:

["1+1=2", "3/3=1"]
Examples
true_equations(["2*2=4"]) ➞ ["2*2=4"]

true_equations(["1+1=3", "3-1=1"]) ➞ []

true_equations(["1+1=2", "2+2=3", "5*5=10", "3/3=1"]) ➞ ["1+1=2", "3/3=1"]

Notes
If all equations are false, return the empty list [], as in the second example.
The equations will only involve the elementary operations: +, -, *, /
"""



################################################################
"""
Solution 1
"""


def true_equations(lst):
	return [eq for eq in lst if eval(eq.replace("=","=="))]



################################################################
"""
Solution 2
"""


def true_equations(lst):
	ls = []
	for i in lst:
		a, b = i.split('=')
		if eval(a) == int(b):
			ls.append(i)
	return ls


################################################################
"""
Solution 3
"""


def true_equations(lst):
	return [x for x in lst if eval(x.split('=')[0]) == eval(x.split('=')[1])]



#################################################################
"""
Solution 4
"""


def equals(e):
	e = e.replace("=","==")
	return e
def true_equations(lst):
	return list(filter(lambda x: eval(equals(x)),lst))



