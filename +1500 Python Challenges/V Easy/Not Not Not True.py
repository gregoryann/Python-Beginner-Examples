"""
Not Not Not True
Something which is not true is false, but something which is not not true is true! Create a function where given n number of "not", evaluate whether it's True or False.

Examples
not_not_not(1, True) ➞ False
# Not True.

not_not_not(2, False) ➞ False
# Not not False.

not_not_not(6, True) ➞ True
# Not not not not not not True.
Notes
Even though this challenge can be easily solved through the use of an if | else block, you might want to solve it through the use of a Boolean Logic Operator or a Bitwise Operator, taking the opportunity to become acquainted with these methods (check the Resources tab to find specific links).

"""



"""
Solution 1
"""

def not_not_not(n, b):
	return not b if n%2 else b

"""
Solution 2
"""

def not_not_not(n, b):
	return b if n % 2 == 0 else not b

"""
Solution 3
"""

def not_not_not(n, b):
    if((n%2 == 0 and b == True) or (n%2 != 0 and b == False)):
       return(True)
    else:
       return(False)

"""
Solution 4
"""

def not_not_not(n, b):
	if b == True:
		return True if n % 2 == 0 else False
	elif b == False:
		return True if n % 2 != 0 else False






