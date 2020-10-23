"""
Longest Word

Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word. Characters such as apostophe, comma, period (and the like) count as part of the word (e.g. O'Connor is 8 characters long).

Examples
longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"

longest_word("A thing of beauty is a joy forever.") ➞ "forever."
  
longest_word("Forgetfulness is by all means powerless!") ➞ "Forgetfulness"

Notes
A similar version of this challenge, which is to be implemented recursively, can be found in here.
"""



################################################################
"""
Solution 1
"""

def longest_word(s):
	return max(s.split(), key=len)




################################################################
"""
Solution 2
"""


longest_word=lambda s:max(s.split(),key=len)



################################################################
"""
Solution 3
"""


def longest_word(s):
    ans = s.split()
    l = [(x,len(x)) for x in ans]
    return sorted(l,key=lambda tup: tup[1],reverse=True)[0][0]




#################################################################
"""
Solution 4
"""


def longest_word(s):
	return sorted(s.split(), key=lambda w: (len(w), -s.index(w)))[-1]



#################################################################
"""
Solution 5
"""

def longest_word(a):
	a=a.split(" ")
	b=[len(i) for i in a]
	c=b.index(max(b))
	return a[c]