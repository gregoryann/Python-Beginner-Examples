"""
Valid Variable Names
When creating variables, the variable name must always start with a letter and cannot contain spaces, though numbers and underscores are allowed to be contained in it also.

Create a function which returns True if a given variable name is valid, otherwise return False.

Examples
variable_valid("result") ➞ True

variable_valid("odd_nums") ➞ True

variable_valid("2TimesN") ➞ False
Notes
Inputs are given as strings.
Variable names with spaces are not allowed.
Although this question may seem like otherwise, you can't actually assign words with quotes around them as variables.

"""



"""
Solution 1
"""

def variable_valid(var):
	return var.isidentifier()

"""
Solution 2
"""

def variable_valid(var):
	return ' ' not in var and var[0].isalpha()


"""
Solution 3
"""

def variable_valid(var):
    myans = var[0].isalpha()
    if myans:
        myans = var.count(' ') == 0

    return myans

"""
Solution 4
"""

def variable_valid(var):
    if var[0] in '0123456789':
        return False
    for v in var:
        if v == ' ':
            return False
    return True



