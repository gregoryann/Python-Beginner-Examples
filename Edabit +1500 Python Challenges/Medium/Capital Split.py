"""
Capital Split
Create a function which adds spaces before every capital in a word. Uncapitalize the whole string afterwards.

Examples
cap_space("helloWorld") ➞ "hello world"

cap_space("iLoveMyTeapot") ➞ "i love my teapot"

cap_space("stayIndoors") ➞ "stay indoors"

Notes
The first letter will stay uncapitalized.
"""



################################################################
"""
Solution 1
"""


def cap_space(txt):
	return ''.join([ch if ch.islower() else ' ' + ch.lower() for ch in txt])



################################################################
"""
Solution 2
"""


import re

def cap_space(txt):
	return re.sub('([A-Z])', r' \1', txt).lower()


################################################################
"""
Solution 3
"""


def cap_space(txt):
    b=""
    for i in txt:
        if i.isupper():
            b=b+" "+i.lower()
        else:
            b=b+i
    return b



#################################################################
"""
Solution 4
"""


import re
def cap_space(txt):
	res = [s for s in re.split("([A-Z][^A-Z]*)", txt) if s]
	return " ".join(i.lower() for i in res)



