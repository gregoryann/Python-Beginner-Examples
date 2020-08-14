"""

Flip the Boolean
Due to a programming concept known as truthiness, certain values can be evaluated to (i.e. take the place of) booleans. For example, 1 (or any number other than 0) is often equivalent to True, and 0 is often equivalent to False.

Create a function that returns the opposite of the given boolean, as a number.

Examples
flip_bool(True) ➞ 0

flip_bool(False) ➞ 1

flip_bool(1) ➞ 0

flip_bool(0) ➞ 1
Notes


"""






"""
Solution 1
"""

def flip_bool(b):
	return not b





"""
Solution 2
"""

flip_bool=lambda b:not b



"""
Solution 3
"""

def long_burp(num):
    return "Bu"+(num * "r")+"p"



"""
Solution 4
"""

def flip_bool(b):
    if b:
		    return 0
    return 1




def flip_bool(b):
	return b == False





def flip_bool(b):
	if b == True:
	 return 0
	else:
	 return 1



def flip_bool(b):
	return 1 if b == (False or 0) else 0