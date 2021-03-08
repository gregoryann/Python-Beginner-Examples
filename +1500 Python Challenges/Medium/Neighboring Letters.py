"""
Neighboring Letters

Create a function that takes a string and checks if every single character is preceded and followed by a character based on the english alphabet. Example: "c" should be preceded by "b" and followed by "d" (bcd === True).

Examples
neighboring("aba") ➞ True

neighboring("abcdedcba") ➞ True

neighboring("efghihfe") ➞ False

neighboring("abc") ➞ True

neighboring("qrstuv") ➞ True

neighboring("mnopqrtstrqpomn") ➞ True

Notes
All test cases will be in lower case.
"""



################################################################
"""
Solution 1
"""


def neighboring(txt):
	
	Code = "abcdefghijklmnopqrstuvwxyz"
	
	First = 0
	Second = 1
	Length = len(txt)
	
	while (Second < Length):
		
		Item_A = txt[First]
		Item_B = txt[Second]
		
		Place_A = Code.index(Item_A)
		Place_B = Code.index(Item_B)
		
		Span = abs(Place_A - Place_B)
		
		if (Span == 1):
			First += 1
			Second += 1
		else:
			return False
			
	return True



################################################################
"""
Solution 2
"""


def neighboring(txt, i=0):
	if i == len(txt) - 1:
		return True
	a = 'abcdefghijklmnopqrstuvwxyz'
	try:
		if txt[i+1] == a[a.index(txt[i]) + 1] or txt[i+1] == a[a.index(txt[i]) - 1]:
			return neighboring(txt, i+1)
		else:
			return False
	except IndexError:
		return True



################################################################
"""
Solution 3
"""


def neighboring(txt):
	for i in range(0,len(txt) - 1):
		if ord(txt[i]) + 1 != ord(txt[i+1]) and ord(txt[i]) - 1 != ord(txt[i+1]):
			return False
	return True


#################################################################
"""
Solution 4
"""


def neighboring(txt):
	return all(abs(ord(txt[i]) - ord(txt[i-1]))==1 and abs(ord(txt[i]) - ord(txt[i+1]))==1 for i in range(1,len(txt)-1))



