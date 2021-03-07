"""
House of Cards

The image below shows a sequence of larger and larger houses of cards, with the total number of cards included for each:

House of Cards

Given the tower height n, return the number of cards needed to construct a full house of cards.

Examples
cards_needed(3) ➞ 15

cards_needed(4) ➞ 26

cards_needed(0) ➞ 0

Notes
The height should always be equal or greater than 0. Return "invalid" if the value given doesn't abide by this rule.
"""




################################################################
"""
Solution 1
"""


def cards_needed(n):
	return n*(3*n + 1)/2 if n >= 0 else 'invalid'




################################################################
"""
Solution 2
"""


cards_needed=lambda n:"invalid"*(n<0)or 3*n*n+n>>1



################################################################
"""
Solution 3
"""


needed = {0: 0, 1: 2}
diff = 2
for h in range(2, 101):
    diff += 3
    needed[h] = needed[h-1] + diff
   
def cards_needed(n):
    if n < 0:
        return 'invalid'
    return needed[n]




#################################################################
"""
Solution 4
"""


def cards_needed(n):
	if n < 0:
		return 'invalid' 
	else:
		num_cards = n * 2 # bottom level
		for i in range(1, n):
				num_cards += i * 3 # add other levels
		return num_cards




