"""
Uno (Part 1)
This question is inspired by the popular Uno card game.

Write a function that takes in two arguments: (1) a player's current hand and (2) the current face-up card on the table. The function will return True if the player can make a play, or False if the player has to draw from the deck.

A player can make a play if either:

They have a card that is the same color as the face-up card.
They have a card that is the same number as the face-up card.
can_play(["yellow 3", "yellow 7", "blue 8", "red 9", "red 2"], "red 1") ➞ True
# Since the player has two red cards, and the face-up card is red.

can_play(["yellow 3", "yellow 7"], "blue 7") ➞ True
# Since the player has a 7, and the face-up card is a 7.
Examples
can_play(["yellow 3", "yellow 5", "red 8"], "red 2") ➞ True

can_play(["yellow 3", "yellow 5", "red 8"], "blue 5") ➞ True

can_play(["yellow 3", "blue 5", "red 8", "red 9"], "green 4") ➞ False

can_play(["yellow 3", "red 8"], "green 2") ➞ False


Notes
Return False if the player is not holding any cards (an empty list).
There are no special cards or wild cards in this deck.
"""





################################################################
"""
Solution 1
"""


can_play=lambda x,f:any(i in str(x)for i in f.split())



################################################################
"""
Solution 2
"""


def can_play(hand, face):
	Colors = list(map(lambda Card:Card.split(" ")[0],hand))
	Numbers = list(map(lambda Card:Card.split(" ")[1],hand))
	for Col in range(len(Colors)):
		if Colors[Col] == face.split(" ")[0]:
			return True
	for Num in range(len(Numbers)):
		if Numbers[Num] == face.split(" ")[1]:
			return True
	return False



################################################################
"""
Solution 3
"""


def can_play(hand, face):    
    hand = [i.split(' ') for i in hand]
    face = [face.split(' ') for f in range(1)]
    new_list = []
    same = 0
    for i in hand:
        for j in i:
            if j not in new_list:
                new_list.append(j)
          
      
    for f in face:
        for g in f:
            if g in new_list:
                same +=1
            else:
                same += 0
    
    if same >= 1:
        return True
    else :



#################################################################
"""
Solution 4
"""

def can_play(hand, face):
	for x in hand:
		if x.split()[0]==face.split()[0] or x.split()[1]==face.split()[1]:
			return True
	return False



