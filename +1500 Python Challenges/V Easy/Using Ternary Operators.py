"""
Using Ternary Operators
The ternary operator (sometimes called Conditional Expressions) in python is an alternative to the if... else... statement.

It is written in the format:

result_if_true if condition else result_if_false
Ternary operators are often more compact than multi-line if statements, and are useful for simple conditional tests.

For example:

is_nice = True

# Using ternary operator.
state = "nice" if is_nice else "not nice"

# Equivalent code using multi-line if statements.
if is_nice:
    state = "nice"
else:
    state = "not nice"
Write a function that uses the ternary operator to return "yeah" if the condition is True, and "nope" otherwise.

Examples
yeah_nope(True) ➞ "yeah"

yeah_nope(False) ➞ "nope"

"""




"""
Solution 1
"""

def yeah_nope(b):
	return ['nope', 'yeah'][b]


"""
Solution 2
"""

def yeah_nope(b):
	return "yeah" if b else "nope"

"""
Solution 3
"""

yeah_nope=lambda b:"nyoepaeh"[b::2]

"""
Solution 4
"""


def yeah_nope(b):
	if b == True:
		return 'yeah'
	else:
		return 'nope'




