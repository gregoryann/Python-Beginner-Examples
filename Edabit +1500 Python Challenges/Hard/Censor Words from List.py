"""
Censor Words from List
Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char.

Examples
censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"

censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")

censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"
"""



################################################################
"""
Solution 1
"""


def censor_string(txt, lst, character):
    for word in lst:
        txt = txt.replace(word, character*len(word))
    return txt




################################################################
"""
Solution 2
"""


def censor_string(txt, lst, char):
	return ' '.join(char*len(word) if word in lst else word for word in txt.split())





################################################################
"""
Solution 3
"""


def censor_string(txt, lst, char):
    txtLst = txt.split()
    returnStr = ''
    for word in txtLst:
        if word in lst:
            word = char * len(word)
        returnStr = returnStr + " " + word  
    return returnStr.strip()




################################################################
"""
Solution 4
"""


def censor_string(txt, lst, char):
	words, res = txt.split(), []
	for word in words:
		if word in lst: res.append(char*len(word))
		else: res.append(word)
	return " ".join(res)

