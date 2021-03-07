"""
Strange Pair

A pair of strings form a strange pair if both of the following are true:

The 1st string's first letter = 2nd string's last letter.
The 1st string's last letter = 2nd string's first letter.
Create a function that returns True if a pair of strings constitutes a strange pair, and False otherwise.

Examples
is_strange_pair("ratio", "orator") ➞ True
# "ratio" ends with "o" and "orator" starts with "o".
# "ratio" starts with "r" and "orator" ends with "r".

is_strange_pair("sparkling", "groups") ➞ True

is_strange_pair("bush", "hubris") ➞ False

is_strange_pair("", "") ➞ True

Notes
It should work on a pair of empty strings (they trivially share nothing).
"""





################################################################
"""
Solution 1
"""

def is_strange_pair(txt1, txt2):
	return txt1[0:1] == txt2[-1:] and txt1[-1:] == txt2[0:1]




################################################################
"""
Solution 2
"""

is_strange_pair=lambda a,b:(a[0]==b[-1]and a[-1]==b[0])if(a and b)else 0if(a or b)else 1



################################################################
"""
Solution 3
"""

def is_strange_pair(txt1, txt2):
  return True if txt1=='' and txt2=='' else False if txt1=='' or txt2=='' else txt1[0]==txt2[-1] and txt1[-1]==txt2[0]






#################################################################
"""
Solution 4
"""

def is_strange_pair(txt1, txt2):
	if txt1==txt2:
		return True
	elif (txt1=="" and txt2!="") or (txt1!="" and txt2==""):
		return False
	elif txt1[0]==txt2[::-1][0] and txt1[::-1][0]==txt2[0]:
		return True
	else:
		return False




