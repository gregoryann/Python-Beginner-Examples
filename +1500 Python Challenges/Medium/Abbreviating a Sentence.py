"""
Abbreviating a Sentence

Create a function which takes a sentence and returns its abbreviation. Get all of the words over or equal to n characters in length and return the first letter of each, capitalised and overall returned as a single string.

Examples
abbreviate("do it yourself") ➞ "Y"

abbreviate("do it yourself", 2) ➞ "DIY"
# "do" and "it" are included because the second parameter specified that word lengths 2 are allowed.

abbreviate("attention AND deficit OR hyperactivity THE disorder") ➞ "ADHD"
# Words below the default 4 characters are not included in the abbreviation.

abbreviate("the acronym of long word lengths", 5) ➞ "AL"
# "acronym" and "lengths" have 5 or more characters.

Notes
There may not be an argument given for n so set the default to 4.
"""



################################################################
"""
Solution 1
"""


abbreviate=lambda s,n=4:"".join(e[0].upper()*(len(e)>=n)for e in s.split())



################################################################
"""
Solution 2
"""


def abbreviate(sentence, n=4):
	return ''.join(i[0] for i in sentence.split() if len(i) >= n).upper()



################################################################
"""
Solution 3
"""


def abbreviate(sentence, n=4):
    t1 = sentence.split(' ')
    myans = ''
    
    for i in range(len(t1)):
        if len(t1[i]) >= n:
            myans += t1[i][0].upper()
    
    return myans



#################################################################
"""
Solution 4
"""


def abbreviate(sentence, n=4):
    ans = ""
    for word in sentence.split():
        if len([c for c in word if c.isalpha()]) >= n:
            ans += word[0].upper()
    return ans



