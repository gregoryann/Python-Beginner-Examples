"""
Maskify the String
Usually when you sign up for an account to buy something, your credit card number, phone number or answer to a secret question is partially obscured in some way. Since someone could look over your shoulder, you don't want that shown on your screen. Hence, the website masks these strings.

Your task is to create a function that takes a string, transforms all but the last four characters into "#" and returns the new masked string.

Examples
maskify("4556364607935616") ➞ "############5616"

maskify("64607935616") ➞ "#######5616"

maskify("1") ➞ "1"

maskify("") ➞ ""

Notes
The maskify function must accept a string of any length.
An empty string should return an empty string (fourth example above).
"""


########################################################################




"""
Solution 1
"""

def maskify(txt):
  return '#'*(len(txt)-4) + txt[-4:]

"""
Solution 2
"""

def maskify(txt):
  return '{}{}'.format('#' * (len(txt) - 4), txt[-4:])

"""
Solution 3
"""

def maskify(txt):
  txt=str(txt)
  if len(txt)<=4:
    return txt
  for i in range(len(txt)-4):
    txt=txt.replace(txt[i],'#',1)
  return txt

"""
Solution 4
"""

def maskify(txt):
  if len(txt) < 4:
    return txt
  else:
    return '{}{}'.format('#' * (len(txt) - 4),
                        txt[len(txt)-4:])




