"""
From A to Z

Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

Examples
gimme_the_letters("a-z") ➞ "abcdefghijklmnopqrstuvwxyz"

gimme_the_letters("h-o") ➞ "hijklmno"

gimme_the_letters("Q-Z") ➞ "QRSTUVWXYZ"

gimme_the_letters("J-J") ➞ J"

Notes
A hyphen will separate the two letters in the string.
You don't need to worry about error handling in this one (i.e. both letters will be the same case and the second letter will always be after the first alphabetically).
"""




################################################################
"""
Solution 1
"""

def gimme_the_letters(sp):
	return "".join(chr(n) for n in range(ord(sp[0]),ord(sp[-1])+1))




################################################################
"""
Solution 2
"""

def gimme_the_letters(spectrum):
	a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	x,y=spectrum.split('-')
	return a[a.index(x):a.index(y)+1]


################################################################
"""
Solution 3
"""

def gimme_the_letters(spectrum):
    left, right = spectrum.split('-')
    return ''.join(chr(i) for i in range(ord(left), ord(right) + 1))


#################################################################
"""
Solution 4
"""

def gimme_the_letters(sp):
  a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  if sp[0].islower():
    return a.lower()[a.lower().index(sp[0]):a.lower().index(sp[-1])+1]
  else: return a[a.index(sp[0]):a.index(sp[-1])+1]



