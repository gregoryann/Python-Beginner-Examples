"""
Reverse Titling
The normal title() function in Python capitalises the first letter of every word in a given sentence, leaving all the other letters as lowercase.

The goal of this challenge is to create a reverse_title() function, which achieves the complete opposite! Make the first letter of every word lowercase, and the rest uppercase!

Examples
reverse_title("this is a title") ➞ "tHIS iS a tITLE"

reverse_title("BOLD AND BRASH!") ➞ "bOLD aND bRASH!"

reverse_title("Elephants dance about bravely in Thailand") ➞ "eLEPHANTS dANCE aBOUT bRAVELY iN tHAILAND"

"""



"""
Solution 1
"""

def reverse_title(txt):
	return txt.title().swapcase()

"""
Solution 2
"""

reverse_title = lambda t:t.title().swapcase()

"""
Solution 3
"""

def reverse_title(txt):
	return ' '.join(w[0].lower() + w[1:].upper() for w in txt.split())

"""
Solution 4
"""

def reverse_title(txt):
	words = txt.split()
	for i in range(len(words)):
		word = words[i][0].lower() + words[i][1:].upper()
		words[i] = word
	return ' '.join(words)





