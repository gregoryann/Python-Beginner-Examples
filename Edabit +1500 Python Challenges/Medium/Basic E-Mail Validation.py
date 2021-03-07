"""
Basic E-Mail Validation

Create a function that accepts a string, checks if it's a valid email address and returns either True or False, depending on the evaluation.

The string must contain an @ character.
The string must contain a . character.
The @ must have at least one character in front of it.
e.g. "e@edabit.com" is valid while "@edabit.com" is invalid.
The . and the @ must be in the appropriate places.
e.g. "hello.email@com" is invalid while "john.smith@email.com" is valid.
If the string passes these tests, it's considered a valid email address.

Examples
validate_email("@gmail.com") ➞ False

validate_email("hello.gmail@com") ➞ False

validate_email("gmail") ➞ False

validate_email("hello@gmail") ➞ False

validate_email("hello@edabit.com") ➞ True


Notes
Check the Tests tab to see exactly what's being evaluated.
You can solve this challenge with RegEx, but it's intended to be solved with logic.
Solutions using RegEx will be accepted but frowned upon :(
"""




################################################################
"""
Solution 1
"""


def validate_email(string):
  return True if ((string.find("@")>1) and (string.rfind(".")>string.find("@"))) else False



################################################################
"""
Solution 2
"""


import re

def validate_email(string):
  return bool(re.search(r'.+\@.+\.', string))



################################################################
"""
Solution 3
"""


def validate_email(txt):
	return txt.count('@') == 1 and txt[0] !='@' and txt.count('.')>= 1 and \
	txt[txt.index('@') + 1:].count('.') >= 1



#################################################################
"""
Solution 4
"""


import re
def validate_email(txt):
	return re.match(r'^.+@.+\.com$', txt) is not None




#################################################################
"""
Solution 5
"""


def validate_email(txt):
	if '@' in txt and len(txt) > 0:
		if txt.index('@') > 0 and txt.count('@') == 1:
			if '.' in txt and txt.endswith('.com'):
				return True
				exit()
	return False




    
#################################################################
"""
Solution 6
"""


import re

def validate_email(txt):
	if (re.match('[a-zA-Z0-9]+.?[a-zA-Z0-9]+[@][a-zA-Z0-9]+[.][a-zA-Z]{2,}',txt)):
		return True
	else: 
		return False






#################################################################
"""
Solution 7
"""


def validate_email(txt):

    if "@" in txt:

        if "." in txt:

            if txt.index("@") != 0:

                if txt.rindex(".") > txt.index("@"):

                    if txt.rindex(".") < txt.index("com"):

                        return True

    return False