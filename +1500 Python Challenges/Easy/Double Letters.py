"""
Double Letters
Create a function that takes a word and returns True if the word has two consecutive identical letters.

Examples
double_letters("loop") ➞ True

double_letters("yummy") ➞ True

double_letters("orange") ➞ False

double_letters("munchkin") ➞ False
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def double_letters(word):
	return any(i*2 in word for i in word)

"""
Solution 2
"""

def double_letters(word):
	for i in range(len(word)-1):
		if word[i] == word[i+1]:
			return True
	return False

"""
Solution 3
"""

def double_letters(word):
  import re
  return len((re.compile(r'(\w)\1')).findall(word)) >= 1

"""
Solution 4
"""

double_letters = lambda w: any(x*2 in w for x in w)




