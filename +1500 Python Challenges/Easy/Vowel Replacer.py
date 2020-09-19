"""
Vowel Replacer

Create a function that replaces all the vowels in a string with a specified character.

Examples
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"

replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"

replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"

Notes
All characters will be in lower case.
"""


"""
Solution 1
"""

def replace_vowels(txt, ch):
	return ''.join([i if i not in 'aeoui' else ch for i in txt])

"""
Solution 2
"""

import re
def replace_vowels(txt, ch):
	return re.sub(r'[aeiouAEIOU]', ch, txt)

"""
Solution 3
"""

def replace_vowels(txt, ch):
    
    for char in txt:
        
        if char in "aeiou":
            
            txt = txt.replace(char,ch)
            
    return txt

"""
Solution 4
"""

def replace_vowels(txt, ch):
	vowels = "aeiou"
	new = [ ch if x in vowels else x for x in txt  ]
	return ''.join(new)

"""
Solution 5
"""

def replace_vowels(txt, ch):
	replace_str = ''
	for i in txt:
		if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
			replace_str += ch
		else:
			replace_str += i
	return replace_str

"""
Solution 6
"""

def replace_vowels(txt, ch):
	vows = ('a', 'e', 'i', 'o', 'u')
	return ''.join([ch if l in vows else l for l in txt])