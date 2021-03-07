"""
Poker Full House

Create a function that determines whether or not a player is holding a Full House in their hand. A hand is represented as a list of 5 cards. A full house is defined as a pair of cards and a three-of-a-kind.

To illustrate: ["A", "A", "A", "K", "K"] would be a Full House, since the player holds 3 aces and 2 kings.

Examples
is_full_house(["A", "A", "A", "K", "K"]) ➞ True

is_full_house(["3", "J", "J", "3", "3"]) ➞ True

is_full_house(["10", "J", "10", "10", "10"]) ➞ False

is_full_house(["7", "J", "3", "4", "2"]) ➞ False
"""



################################################################
"""
Solution 1
"""


def is_full_house(hand):
	return all(hand.count(i) >= 2 for i in hand)



################################################################
"""
Solution 2
"""


def is_full_house(hand):
	counts = [hand.count(i) for i in set(hand)]
	if 3 in counts and 2 in counts:
		return True
	else: return False



################################################################
"""
Solution 3
"""


is_full_house=lambda h:len(set(h))<3and h.count(h[0])in[2,3]


#################################################################
"""
Solution 4
"""


def is_full_house(hand):
	counts = {}
	for card in hand:
		counts[card] = counts.get(card, 0) + 1
	threes = sum([1 for cnt in counts.values() if cnt == 3])
	twos = sum([1 for cnt in counts.values() if cnt == 2])
	return threes == 1 and twos == 1



