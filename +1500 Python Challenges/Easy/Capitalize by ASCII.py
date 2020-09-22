"""
Capitalize by ASCII

Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.

Examples
ascii_capitalize("to be or not to be!") ➞ "To Be oR NoT To Be!"

ascii_capitalize("THE LITTLE MERMAID") ➞ "THe LiTTLe meRmaiD"

ascii_capitalize("Oh what a beautiful morning.") ➞ "oH wHaT a BeauTiFuL moRNiNg."
"""

"""
Solution 1
"""

def ascii_capitalize(txt):
	return ''.join(s.lower() if ord(s) % 2 else s.upper() for s in txt)

"""
Solution 2
"""

def ascii_capitalize(txt):
	ans = ''
	for x in txt:
		if ord(x) % 2 == 0:
			ans += x.upper()
		else:
			ans += x.lower()
	return ans

"""
Solution 3
"""

from string import ascii_letters
def ascii_capitalize(txt):
	text = []
	for w in txt:
		if ascii_letters.find(w)%2 == 1:
			text.append(w.upper())
		if ascii_letters.find(w)%2 == 0:
			text.append(w.lower())
	return ''.join(text)

"""
Solution 4
"""

def ascii_capitalize(txt):
	txtArr = [n.upper() if ord(n)%2==0 else n.lower() for n in txt]
	return ''.join(txtArr)




