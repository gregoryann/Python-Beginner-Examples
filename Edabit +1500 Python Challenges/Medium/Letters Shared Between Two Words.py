"""
Letters Shared Between Two Words

Create a function that returns the number of characters shared between two words.

Examples
shared_letters("apple", "meaty") ➞ 2
# Since "ea" is shared between "apple" and "meaty".

shared_letters("fan", "forsook") ➞ 1

shared_letters("spout", "shout") ➞ 4
"""



################################################################
"""
Solution 1
"""


def shared_letters(str1, str2):
	return len(set(str1) & set(str2))



################################################################
"""
Solution 2
"""


shared_letters = lambda x,y: sum(k in y for k in set(x))




################################################################
"""
Solution 3
"""


def shared_letters(txt1, txt2):
	count=0
	for c in txt1:
		if c in txt2:
			count+=1
			txt2=txt2.replace(c,'',1)
	return count




#################################################################
"""
Solution 4
"""


def shared_letters(txt1, txt2):
	s = 0
	for i in set(txt1):
	   if i in txt2:
		    s += 1
	return s



