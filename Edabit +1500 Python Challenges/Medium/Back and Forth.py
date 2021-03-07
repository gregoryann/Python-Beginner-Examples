"""
Back and Forth

In a board game, a player may pick up a card with a number of left or right facing arrows, with the number of arrows indicating the number of tiles to move. The player should move either left or right, depending on the arrow's direction.

Given a list of the arrows contained on a player's cards, return a singular string of arrowheads which are equivalent to all of the arrowheads.

Worked Example
calculate_arrowhead(['>>', '<<', '<<<']) ➞ '<<<'
# >> means to move 2 places right
# << means to move 2 places left (cancelling out >>)
# <<< means to move a further 3 places left
# overall, the movement can be written as <<<
Examples
calculate_arrowhead(['>>>>', '<', '<', '<']) ➞ '>'

calculate_arrowhead(['>', '<', '>>', '<', '<<<']) ➞ '<<'

calculate_arrowhead(['>>>', '<<<']) ➞ ''

Notes
Return an empty string if all the arrowheads cancel out.
"""



################################################################
"""
Solution 1
"""


def calculate_arrowhead(lst):
	diff = sum([-1, 1][i == '>'] for i in ''.join(lst))
	return ['>', '<'][diff < 0] * abs(diff)



################################################################
"""
Solution 2
"""


def calculate_arrowhead(lst):
	string = ''.join(i for i in lst)
	left = string.count('<')
	right = string.count('>')
	return (right - left) * '>' if right > left else (left - right) * '<'



################################################################
"""
Solution 3
"""


def calculate_arrowhead(lst):
  arrows = sum([-arrow.count('<') + arrow.count('>') for arrow in lst])
  return ['<' * abs(arrows), '>' * arrows][arrows > 0]



#################################################################
"""
Solution 4
"""


def calculate_arrowhead(lst):
	s = sum(-1 if i == '<' else 1 for i in ''.join(lst))
	if s < 0:
		return '<'*abs(s)
	else:
		return '>'*s




