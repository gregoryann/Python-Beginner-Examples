"""
Poker Deck

Create a function that generates a poker deck.

A poker deck contains 52 cards in total, 13 cards for each of the four suits (♦ diamonds, ♠ clubs, ♥ hearts and ♣ spades) ranked 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A.

Your function should return a list (deck) containing each card as a tuple in the following format:

(rank, suit)
Where rank is a number from 2 to 14 (11, 12, 13 & 14 being J, Q, K & A respectively) and suit is a string with the first letter of the the card's suit ("d", "c", "h" & "s" for diamonds, clubs, hearts & spades respectively).

Examples
Five of hearts ➞ (5, "h")

Queen of Spades ➞ (12, "s")

Ace of Clubs ➞ (14, "c")

Notes
Extra points for shuffling the deck.
"""



################################################################
"""
Solution 1
"""


from random import shuffle

def gen_deck():
    cards = [(rank, suit) for rank in range(2, 15) for suit in 'dchs']
    shuffle(cards)
    return cards



################################################################
"""
Solution 2
"""


def gen_deck():
	return [(r,s) for r in range(2,15) for s in "dchs"]



################################################################
"""
Solution 3
"""


from random import shuffle

def gen_deck():
	result_card = []
	card_type = ("d", "c", "h", "s")
	
	for card in card_type:
		for index in range(2, 15):
			result_card.append((index, card))
			
	shuffle(result_card)
	return result_card



#################################################################
"""
Solution 4
"""


import random


def gen_deck():
	deck = []
	for rank in range(2, 15):
		for color in ('c', 'h', 's', 'd'):
			deck.append((rank,color))
	random.shuffle(deck)
	return deck





