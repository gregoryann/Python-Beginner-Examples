"""
Check if a String is a Mathematical Expression

Create a function that takes an input (e.g. "5 + 4") and returns True if it's a mathematical expression or False if not.

Examples
math_expr("4 + 5") ➞ True

math_expr("4*6") ➞ True

math_expr("4*no") ➞ False

Notes
Should only work with the following operations: +, -, *, /, %
You don't need to test for floats.
int1 and int2 will only be from 0-9.
"""



################################################################
"""
Solution 1
"""


import re
def math_expr(expr):
	expr = expr.replace(' ', '')
	return bool(re.match(r'\d+[\+-/\*%]\d+', expr))



################################################################
"""
Solution 2
"""


import re;
def math_expr(expr):
   return len(re.sub(r"\d\s*[%+-/*]\s*\d","",expr)) == 0;



################################################################
"""
Solution 3
"""


import re
def math_expr(expr):
	x= (re.findall(r'\d\s?\W\s?\d',expr))
	if x: return (True)
	return False




#################################################################
"""
Solution 4
"""


import re
def math_expr(expr):
    pattern=r'[0-9\+\-\*\/\%]'
    matches=re.findall(pattern,expr)
    return (len(matches)==len([x for x in expr if x!=' ']))




