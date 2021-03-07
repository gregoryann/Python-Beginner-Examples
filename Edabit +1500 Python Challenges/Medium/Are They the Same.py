"""
Are They the Same?

Create a function that takes three arguments (first dictionary, second dictionary, key) in order to:

Return the boolean True if both dictionaries have the same values for the same keys.
If the dictionaries don't match, return the string "Not the same", or the string "One's empty" if only one of the dictionaries contains the given key.
Examples
dict_first = { "sky": "temple", "horde": "orcs", "people": 12, "story": "fine", "sun": "bright" }
dict_second = { "people": 12, "sun": "star", "book": "bad" }

check(dict_first, dict_second, "horde") ➞ "One's empty"

check(dict_first, dict_second, "people") ➞ True

check(dict_first, dict_second, "sun") ➞ "Not the same"


Notes
Dictionaries are an unordered data type.
Double quotes may be helpful.
KeyError can occur when trying to access a dictionary key that doesn't exist.
"""




################################################################
"""
Solution 1
"""


def check(d1, d2, k):
    v1, v2, msg1, msg2 = (d1.get(k), d2.get(k), "One's empty", "Not the same")
    return msg1 if None in (v1, v2) else msg2 if v1 != v2 else True



################################################################
"""
Solution 2
"""


def check(d1, d2, k):
 a = (list(d1.keys())+list(d2.keys())).count(k)
 #try:
 if a==1:
   return "One's empty"
 #except: pass
 #try:
 if d1[k]==d2[k]:
   return True
 #except : pass
 #try:
 if d1[k]!=d2[k]:
   return "Not the same"
 #except : pass



################################################################
"""
Solution 3
"""


def check(d1, d2, k):
	if not d1.get(k) or not d2.get(k):
		return "One's empty"
	return True if d1.get(k) == d2.get(k) else "Not the same"



#################################################################
"""
Solution 4
"""


def check(d1, d2, k):
	if k in d1 and k in d2:
		if d1.get(k) == d2.get(k):
			return True
		return 'Not the same'
	return "One's empty"




