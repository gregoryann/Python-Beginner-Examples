"""
Check If All Values Are True

Create a function that returns True if all parameters are truthy, and False otherwise.

Examples
all_truthy(True, True, True) ➞ True

all_truthy(True, False, True) ➞ False

all_truthy(5, 4, 3, 2, 1, 0) ➞ False

Notes
Truthy values include non-empty sequences, numbers (except 0 in every numeric type), and basically every value that is not falsy.
You can check if an item is truthy by using an if statement on that item.
You will always be supplied with at least one parameter.
"""



################################################################
"""
Solution 1
"""

def all_truthy(*args):
    result = 1
    for i in args:
        if type(i) != str:
            result *= bool(i)
        else:
            break
    return result >= 1








