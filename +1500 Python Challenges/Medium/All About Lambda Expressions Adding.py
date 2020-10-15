"""
All About Lambda Expressions: Adding

Write a function that returns a lambda expression, which adds n to its input

Examples
adds1 = adds_n(1)

adds1(3) ➞ 4
adds1(5.7) ➞ 6.7

adds10 = adds_n(10)

adds10(44) ➞ 54
adds10(20) ➞ 30
"""





################################################################
"""
Solution 1
"""


adds_n = lambda n: lambda x: x + n


################################################################
"""
Solution 2
"""


def adds_n(n): 
 return lambda a : a + n










