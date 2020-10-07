"""
First N Mid

Create a function that takes a string and returns the first character of every word if the length of the word is even and the middle character if the length of the word is odd.

Examples
stmid("Alexa have to paid") ➞ "ehtp"
# "e" is the middle character of "Alexa"
# "h" is the first character of "have"

stmid("Th3 0n3 4nd 0n1y") ➞ "hnn0"

stmid("who is the winner") ➞ "hihw"
"""



################################################################
"""
Solution 1
"""

def stmid(s):
	return ''.join(w[[0, len(w) // 2][len(w) % 2]] for w in s.split())




################################################################
"""
Solution 2
"""

def stmid(string):
	string = string.split()
	answer = ""
	for word in string:
		if len(word)%2 == 0:
			answer += word[0]
		else:
			answer += word[len(word)//2]
	return answer






################################################################
"""
Solution 3
"""

def stmid(string):
	words = string.split(' ')
	return ''.join([w[0] if len(w) % 2 == 0 else w[int(len(w)/2)] for w in words])







#################################################################
"""
Solution 4
"""

import math
def stmid(string):
	lst = string.split( )
	lst1 = []
	for i in lst:
		if len(i)%2 == 0:
			lst1.append(i[0])
		else:
			lst1.append(i[math.floor(len(i)/2)])
	return ''.join(lst1)





