"""
Remove the Special Characters from a String

Create a function that takes a string, removes all "special" characters (e.g. !, @, #, $, %, ^, &, \, *, (, )) and returns the new string. The only non-alphanumeric characters allowed are dashes -, underscores _ and spaces.

Examples
remove_special_characters("The quick brown fox!") ➞ "The quick brown fox"

remove_special_characters("%fd76$fd(-)6GvKlO.") ➞ "fd76fd-6GvKlO"

remove_special_characters("D0n$c sed 0di0 du1") ➞ "D0nc sed 0di0 du1"
"""





#############################################################
"""
Solution 1
"""

def remove_special_characters(txt):
  allowed = [' ', '-', '_']
  return ''.join(t for t in txt if t.isalnum() or t in allowed)






#############################################################
"""
Solution 2
"""

import re
def remove_special_characters(txt):
  return re.sub('[^\s\-\w_]', '', txt)





#############################################################
"""
Solution 3
"""

remove_special_characters=lambda t:''.join(x for x in t if x.isalnum()or x in'-_ ')






#############################################################
"""
Solution 4
"""

def remove_special_characters(txt):
  special = set("!@#$%^&\'*().[]{}<>+=~,`|?")
  output = ''
  for char in txt:
    if char not in special:
      output += char
  return output




#############################################################
"""
Solution 5
"""

def remove_special_characters(txt):
	alph = 'a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 - _  '.split()
	newlst = []
	for i in txt:
		if i.lower() in alph:
			newlst.append(i)
		elif i == " ":
			newlst.append(i)
	return("".join(newlst))



#############################################################
"""
Solution 6
"""


def remove_special_characters(txt):
	rez=''
	for c in txt:
		if c.isalnum() or c == '-' or c == '_' or c == ' ':
			rez+=c
	return rez