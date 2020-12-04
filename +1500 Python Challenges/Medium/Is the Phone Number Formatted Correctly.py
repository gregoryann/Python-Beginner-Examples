"""
Is the Phone Number Formatted Correctly?

Create a function that accepts a string and returns True if it's in the format of a proper phone number and False if it's not. Assume any number between 0-9 (in the appropriate spots) will produce a valid phone number.

This is what a valid phone number looks like:

(123) 456-7890
Examples
is_valid_phone_number("(123) 456-7890") ➞ True

is_valid_phone_number("1111)555 2345") ➞ False

is_valid_phone_number("098) 123 4567") ➞ False

Notes
Don't forget the space after the closing parentheses.
"""




################################################################
"""
Solution 1
"""


import re
def is_valid_phone_number(txt):
	return bool(re.match('^\(\d{3}\) \d{3}-\d{4}$', txt))



################################################################
"""
Solution 2
"""


import re
is_valid_phone_number=lambda t:bool(re.match("^\(\d{3}\) \d{3}-\d{4}$",t))



################################################################
"""
Solution 3
"""


import re
def is_valid_phone_number(txt):
	return bool(re.search('\(\d{3}\) \d{3}-\d{4}',txt)) and len(txt)==14


#################################################################
"""
Solution 4
"""


import re
def is_valid_phone_number(txt):
	return bool(re.search("^\(\d{3}\)\s\d{3}-\d{4}$",txt))



