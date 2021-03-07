"""
Stuttering Function

Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.

Examples
stutter("incredible") ➞ "in... in... incredible?"

stutter("enthusiastic") ➞ "en... en... enthusiastic?"

stutter("outstanding") ➞ "ou... ou... outstanding?"

Notes
Assume all input is in lower case and at least two characters long.
"""


"""
Solution 1
"""

def stutter(word):
		return '{0}... {0}... {1}?'.format(word[:2], word)

"""
Solution 2
"""

def stutter(word):
	return (2*(word[:2]+'... '))+word+'?'

"""
Solution 3
"""

stutter = lambda w: '{}... {}... {}?'.format(w[:2], w[:2], w)

"""
Solution 4
"""

def stutter(word):
    osszes =""
    for i in word:
        osszes+=i
    return osszes[0:2]+"... "+osszes[0:2]+"... "+osszes+"?"




