"""Logical calculator
https://www.codewars.com/kata/logical-calculator
Your task is to calculate logical value of boolean array. Test arrays are one-dimensional and their size is in the range 1-50.
Links referring to logical operations: [AND](https://en.wikipedia.org/wiki/Logical_conjunction), [OR](https://en.wikipedia.org/wiki/Logical_disjunction) and [XOR](https://en.wikipedia.org/wiki/Exclusive_or).
<b>First Example:
Input: true, true, false, operator: AND
Steps: true AND true -> true, true AND false -> false
Output: false
<b>Second Example:
Input: true, true, false, operator: OR
Steps: true OR true -> true, true OR false -> true
Output: true
<b>Third Example:
Input: true, true, false, operator: XOR
Steps: true XOR true -> false, false XOR false -> false
Output: false
___
Input:
boolean array, string with operator' s name: 'AND', 'OR', 'XOR'.
Output:
calculated boolean
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################


import functools
import operator


OPERATORS = {
    "AND": operator.and_,
    "OR" : operator.or_,
    "XOR": operator.xor
}

def logical_calc(array, op):
    return functools.reduce(OPERATORS[op], array)