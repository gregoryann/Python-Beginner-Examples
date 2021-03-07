"""
Position in the Alphabet

Given a number between 1-26, return what letter is at that position in the alphabet. Return "invalid" if the number given is not within that range, or isn't an integer.

Examples
letter_at_position(1) ➞ "a"

letter_at_position(26.0) ➞ "z"

letter_at_position(0) ➞ "invalid"

letter_at_position(4.5) ➞ "invalid"

Notes
Return a lowercase letter.
Numbers that end with ".0" are valid.
"""





################################################################
"""
Solution 1
"""

def letter_at_position(n):
	return chr(int(n) + 96) if n == int(n) and n != 0 else 'invalid'






################################################################
"""
Solution 2
"""

def letter_at_position(n):
	try:
		n1= int(float(n) *10)
		n= int(n)
		print(n)
		if (n*10) == n1 and  n >= 1 and n <=26:
			return(chr(ord('a') - 1 + n))
		else:
			return('invalid')
	except:
 		return('invalid')








################################################################
"""
Solution 3
"""


def letter_at_position(n):
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	if int(n) != n:
		return 'invalid'
	elif int(n) < int(1) or int(n) > int(26):
		return 'invalid'
	else:
		return str(alphabet[int(n)-1])








#################################################################
"""
Solution 4
"""


def letter_at_position(n):
  letters = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'};
  return letters.get(n,'invalid');








#################################################################
"""
Solution 5
"""

def letter_at_position(n):
	alphabet = {
	1 : 'a',
	2 : 'b',
	3 : 'c',
	4 : 'd',
	5 : 'e',
	6 : 'f',
	7 : 'g',
	8 : 'h',
	9 : 'i',
	10 : 'j',
	11 : 'k',
	12 : 'l',
	13 : 'm',
	14 : 'n',
	15 : 'o',
	16 : 'p',
	17 : 'q',
	18 : 'r',
	19 : 's',
	20 : 't',
	21 : 'u',
	22 : 'v',
	23 : 'w',
	24 : 'x',
	25 : 'y',
	26 : 'z',
	}
	if n in alphabet:
		return alphabet.get(n)
	else:
		return "invalid"





#################################################################
"""
Solution 6
"""


def letter_at_position(n):
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	if int(n) != n:
		return 'invalid'
	elif int(n) < int(1) or int(n) > int(26):
		return 'invalid'
	else:
		return str(alphabet[int(n)-1])