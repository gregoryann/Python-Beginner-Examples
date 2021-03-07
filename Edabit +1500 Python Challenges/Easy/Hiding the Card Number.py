"""
Hiding the Card Number

Write a function that takes a credit card number and only displays the last four characters. The rest of the card number must be replaced by ************.

Examples
card_hide("1234123456785678") ➞ "************5678"

card_hide("8754456321113213") ➞ "************3213"

card_hide("35123413355523") ➞ "**********5523"

Examples
Ensure you return a string.
The length of the string must remain the same as the input.
"""




#############################################################
#                        MY SOLUTIONS                       #
#############################################################





"""
Solution 1
"""

def card_hide(card):
	return '*'*len(card[:-4])+card[-4:]

"""
Solution 2
"""

card_hide = lambda c: c[-4:].rjust(len(c), '*')


"""
Solution 3
"""

def card_hide(card):
	return ''.join(['*' if len(card) - 4 > x else card[x] for x in range(len(card))])

"""
Solution 4
"""

def card_hide(card):
	last_four_nums = card[-4:]
	asterisks = ""
	for num in range(0, len(card) - 4):
		asterisks += "*"
	return asterisks + last_four_nums




