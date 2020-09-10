"""

Valid Zip Code

Zip codes consist of 5 consecutive digits. Given a string, write a function to determine whether the input is a valid zip code. A valid zip code is as follows:

Must only contain numbers (no non-digits allowed).
Must not contain any spaces.
Must not be greater than 5 digits in length.

Examples
is_valid("59001") ➞ True

is_valid("853a7") ➞ False

is_valid("732 32") ➞ False
"""


"""
Solution 1
"""

def is_valid(zip_code):
	return zip_code.isnumeric() and len(zip_code) == 5

"""
Solution 2
"""

def is_valid(zip_code):
	if len(zip_code)==5 and zip_code.isdigit():
		return True
	else:
		return False

"""
Solution 3
"""

def is_valid(zip_code):
	return len(list(zip_code))==5 and str(zip_code).isnumeric()






