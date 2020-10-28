"""
Censor Words Longer Than Four Characters

Create a function that takes a string and censors words over four characters with *.

Examples
censor("The code is fourty") ➞ "The code is ******"

censor("Two plus three is five") ➞ "Two plus ***** is five"

censor("aaaa aaaaa 1234 12345") ➞ "aaaa ***** 1234 *****"

Notes
Don't censor words with exactly four characters.
If all words have four characters or less, return the original string.
The amount of * is the same as the length of the word.
"""




################################################################
"""
Solution 1
"""


def censor(s):
	return ' '.join('*'*len(i) if len(i) > 4 else i for i in s.split())



################################################################
"""
Solution 2
"""



def censor(s):
	words = s.split()
	for i in range(len(words)):
		if len(words[i]) > 4:
			words[i] = "*"*len(words[i])
	return " ".join(words)


################################################################
"""
Solution 3
"""



def censor(s):
	return " ".join( w if len(w) <= 4 else "*" * len(w) for w in s.split() )





censor=lambda s:" ".join([w,"*"*len(w)][len(w)>4]for w in s.split())




#################################################################
"""
Solution 4
"""



def censor(s):
	lst = s.split()
	empty_lst = []
	for i in lst:
		if len(i) > 4:
			i = '*' * len(i)
		empty_lst.append(i)
	return (' ').join(empty_lst)




