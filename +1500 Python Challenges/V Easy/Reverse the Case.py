"""
Reverse the Case
Given a string, create a function to reverse the case. All lower-cased letters should be upper-cased, and vice versa.

Examples
reverse_case("Happy Birthday") ➞ "hAPPY bIRTHDAY"

reverse_case("MANY THANKS") ➞ "many thanks"

reverse_case("sPoNtAnEoUs") ➞ "SpOnTaNeOuS"

"""




"""
Solution 1
"""

def reverse_case(txt):
	return txt.swapcase()

"""
Solution 2
"""

def reverse_case(txt):
	return ''.join([i.upper() if i.islower() else i.lower() for i in txt])

"""
Solution 3
"""

def reverse_case(txt):
	x=''
	for item in txt:
		if item.isupper()==True:
			x+=item.lower()
		else:
			x+=item.upper()
	return x

"""
Solution 4
"""

import string

def reverse_case(txt):

    upper_letters = string.ascii_uppercase

    transformed_letters = [char.lower() if char in upper_letters
                           else char.upper()
                           for char in txt]

    return ''.join(transformed_letters)




