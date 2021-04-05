"""
Basic Arithmetic Operations on a String Number
Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.

eval() is not allowed. In case of division, whenever the second number equals "0" return -1.

For example:
"15 // 0"  ➞ -1


Examples
arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24

arithmetic_operation("12 - 12") ➞ 24 // 12 - 12 = 0

arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144

arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1


Notes
All the inputs are only integers.
The operators are * - + and //.
Hint: Think about the single space that appears before and after the arithmetic operator.
"""




################################################################
"""
Solution 1
"""


OP = {'+':int.__add__, '-':int.__sub__, '*':int.__mul__,
      '//': lambda a,b: a//b if b else -1 }

def arithmetic_operation(n):
    a, o, b = n.split()
    return OP[o](int(a), int(b))




################################################################
"""
Solution 2
"""


import operator
def arithmetic_operation(n):
    a = int(n.split()[0])
    b = n.split()[1]
    c = int(n.split()[2])
   
    ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '//': operator.floordiv 
}
    try:
        return ops[b](a,c)
    except ZeroDivisionError :
        return -1




################################################################
"""
Solution 3
"""


def arithmetic_operation(n):
    op = {'+': lambda x, y: x + y,'-': lambda x, y: x - y,'*': lambda x, y: x * y,'//': lambda x, y: x // y,}
    container=n.split()
    if container[1] == "//" and container[-1]=="0":
        return -1

    return op[container[1]](int(container[0]),int(container[-1]))



################################################################
"""
Solution 4
"""

import operator

def arithmetic_operation(n):
    exp = n.split()
    a, op, b = int(exp[0]), exp[1], int(exp[2])
    try:
        ops = {'+': operator.add(a, b),
              '-' : operator.sub(a, b),
               '*': operator.mul(a,b),
               '//' : operator.floordiv(a, b)
              }
    except ZeroDivisionError:
        return -1
    return ops[op]



################################################################
"""
Solution 5
"""


import re

def arithmetic_operation(n):
	op = re.search(r'(?<= ).*(?= )', n).group()
	a, b = map(int, n.split(" " + op + " "))
	if op == '+': return a + b
	if op == '-': return a - b
	if op == '*': return a * b
	if op == '//': return a // b if b else -1



################################################################
"""
Solution 6
"""



    import operator

def arithmetic_operation(n):
    exp = n.split()
    a, op, b = int(exp[0]), exp[1], int(exp[2])
    try:
        ops = {'+': operator.add(a, b),
              '-' : operator.sub(a, b),
               '*': operator.mul(a,b),
               '//' : operator.floordiv(a, b)
              }
    except ZeroDivisionError:
        return -1
    return ops[op]