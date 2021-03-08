"""
Does a Number Exist?

Create a function which validates whether a given number exists, and could represent a real life quantity. Inputs will be given as a string.

Examples
valid_str_number("3.2") ➞ True

valid_str_number("324") ➞ True

valid_str_number("54..4") ➞ False

valid_str_number("number") ➞ False

Notes
Accept numbers such as .5 and 0003.
"""







########################################################################
"""
Solution 1
"""

def valid_str_number(n):
	return n.replace('.','',1).isdigit()





########################################################################
"""
Solution 2
"""

def is_numeric(c):
  if ord(c)>=ord('0') and ord(c)<=ord('9'):
    return True
  return False
  #32..2
  #.3
  #21.22
  #fas223
  #((()))
  #??f322
  #2334.33?
  
def valid_str_number(n):
  c_count=0
  for x in n:
    if x=='.':
      if c_count==0:
        c_count = 1
      else:
        return False
    elif not is_numeric(x):
      return False
  return True





########################################################################
"""
Solution 3
"""

def valid_str_number(n):
	return n.count('.') <= 1 and n.replace('.','').isnumeric()






########################################################################
"""
Solution 4
"""

def valid_str_number(n):
	a='1234567890.'
	x=''
	for i in n:
		if (n.count('.')==1 or n.count('.')==0) and i in a:
			x+=i
	return x==n






########################################################################
"""
Solution 5
"""


def valid_str_number(n):
	return bool(re.findall(r"^\d*\.?\d+$", n))





########################################################################
"""
Solution 6
"""


import re
def valid_str_number(n):
	return re.search(r"^\d*\.?\d+$",n) != None