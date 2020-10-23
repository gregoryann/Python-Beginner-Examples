"""
Change Every Letter to the Next Letter

Write a function that changes every letter to the next letter:

"a" becomes "b"
"b" becomes "c"
"d" becomes "e"
and so on ...
Examples
move("hello") ➞ "ifmmp"

move("bye") ➞ "czf"

move("welcome") ➞ "xfmdpnf"

Notes
There will be no z's in the tests.
"""



################################################################
"""
Solution 1
"""


def move(word):
	return ''.join(chr(ord(i) + 1) for i in word)



################################################################
"""
Solution 2
"""


def move(word):
	woord = ""
	for i in range(len(word)):
		woord += chr(ord(word[i])+1)
	return woord




################################################################
"""
Solution 3
"""


import string

def move(word):
    alphy = string.ascii_lowercase
    
    new = ""
    for i in word:
        if i in alphy:
            new = new + alphy[alphy.index(i)+1]
    return new



#################################################################
"""
Solution 4
"""


def move(word):
	alpha='abcdefghijklmnopqrstuvwxyz'
	new_word=''
	for i in word:
		new_word+=alpha[alpha.index(i)+1]
	return new_word





