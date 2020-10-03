"""
Switcharoo

Create a function that takes a string and returns a new string with its first and last characters swapped, except under three conditions:

If the length of the string is less than two, return "Incompatible.".
If the argument is not a string, return "Incompatible.".
If the first and last characters are the same, return "Two's a pair.".
Examples
flip_end_chars("Cat, dog, and mouse.") ➞ ".at, dog, and mouseC"

flip_end_chars("ada") ➞ "Two's a pair."

flip_end_chars("Ada") ➞ "adA"

flip_end_chars("z") ➞ "Incompatible."

flip_end_chars([1, 2, 3]) ➞ "Incompatible."

Notes
Tests are case sensitive (e.g. "A" and "a" are not the same character).
"""





########################################################################
"""
Solution 1
"""

def flip_end_chars(txt):
  if len(txt) < 2 or type(txt) is not str: 
    return 'Incompatible.'
  if txt[0] is txt[-1]: 
    return 'Two\'s a pair.'
  return txt[-1] + txt[1:-1] + txt[0]





########################################################################
"""
Solution 2
"""

def flip_end_chars(txt):
	if not isinstance(txt, str) or len(txt) < 2:
		return 'Incompatible.'
	a, *b, c = txt
	return "Two's a pair." if a == c else ''.join([c]+b+[a])






########################################################################
"""
Solution 3
"""

def flip_end_chars(txt):
    a = lambda x: x[-1] + x[1:-1] +x[0]

    if len(txt) < 2 or (not isinstance(txt, str)):
        return "Incompatible."
    elif txt == a(txt):
        return "Two's a pair."
    else: return a(txt)







########################################################################
"""
Solution 4
"""


def flip_end_chars(txt):
  a=[]
  if len(txt) < 2 or not isinstance(txt, str):
    return("Incompatible.")
  elif txt[0] == txt[-1]:
    return("Two's a pair.")
  else:
    for n in txt:
      a.append(n)
    temp=a[0]
    a[0]=a[-1]
    a[-1]=temp
    newstring=''.join(a)
    return(newstring)





########################################################################
"""
Solution 5
"""


def flip_end_chars(txt):
  if type(txt) != str:
    return 'Incompatible.'
  txt = list(txt)
  if len(txt) < 2:
    return 'Incompatible.'
  elif txt[0] == txt[-1]:
    return "Two's a pair."
  else:
    txt[0], txt[-1] = txt[-1], txt[0]
  return ''.join(txt)
  	
  
  
  
print(flip_end_chars("Cat, dog, and mouse.")) # ".at, dog, and mouseC"
print(flip_end_chars("ada")) #  "Two's a pair."
print(flip_end_chars("z")) # "Incompatible."