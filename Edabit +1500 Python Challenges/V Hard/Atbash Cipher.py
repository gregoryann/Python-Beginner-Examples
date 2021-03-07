"""
Atbash Cipher

The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.

Create a function that takes a string and applies the Atbash cipher to it.

Examples
atbash("apple") ➞ "zkkov"

atbash("Hello world!") ➞ "Svool dliow!"

atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"


Notes
Capitalisation should be retained.
Non-alphabetic characters should not be altered.
"""



"""
Solution 1
"""


from string import ascii_letters as alpha

def atbash(txt):
	return txt.translate(str.maketrans(alpha, alpha[::-1].swapcase()))




"""
Solution 2
"""


def atbash(txt):
	a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
	z = 'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'
	s = ''
	for i in txt:
		if i in a:
			s += z[a.index(i)]
		else:
			s += i
	return s




"""
Solution 3
"""


from string import ascii_letters as alpha
def atbash(txt):
	return txt.translate(str.maketrans(alpha,alpha[::-1].swapcase()))



"""
Solution 4
"""


def atbash(txt):
	uc,lc = list(range(ord('A'), ord('Z')+1)), list(range(ord('a'), ord('z')+1))
	normal = [chr(i) for i in uc]+[chr(i) for i in lc]
	cipher = [chr(i) for i in uc[::-1]]+[chr(i) for i in lc[::-1]]
	return ''.join(cipher[normal.index(i)] if i.isalpha() else i for i in txt)



"""
Solution 5
"""


def atbash(txt):
	numbers = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
	letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	
	ans = ""
	for char in txt:
		if char.upper() in letters:
			if char.isupper():
				ans += letters[25-numbers[char]]
			else:
				ans += letters[25-numbers[char.upper()]].lower()
		else:
			ans += char
	
	return ans