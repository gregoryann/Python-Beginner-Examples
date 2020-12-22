"""
The Karaca's Encryption Algorithm

Make a function that encrypts a given input with these steps:

Input: "apple"

Step 1: Reverse the input: "elppa"

Step 2: Replace all vowels using the following chart:

a => 0
e => 1
i => 2
o => 2
u => 3

# "1lpp0"
Step 3: Add "aca" to the end of the word: "1lpp0aca"

Output: "1lpp0aca"

Examples
encrypt("banana") ➞ "0n0n0baca"

encrypt("karaca") ➞ "0c0r0kaca"

encrypt("burak") ➞ "k0r3baca"

encrypt("alpaca") ➞ "0c0pl0aca"


Notes
All inputs are strings, no uppercases and all output must be strings.
"""



################################################################
"""
Solution 1
"""


def encrypt(word):
	return word[::-1].translate(str.maketrans('aeou', '0123')) + 'aca'



################################################################
"""
Solution 2
"""


def encrypt(word):
  v= {'a':'0','e':'1','o':'2','u':'3'}
  return ''.join(v[i] if i in v else i for i in word[::-1]) +'aca'



################################################################
"""
Solution 3
"""


def encrypt(word):
	word = word[::-1]
	for r in (("a", "0"), ("e", "1"), ("o", "2"), ("u", "3")):
		word = word.replace(*r)
		
	return word+'aca'



################################################################
"""
Solution 4
"""


encrypt=lambda w:w[::-1].translate({97:48,101:49,111:50,117:51})+"aca"



