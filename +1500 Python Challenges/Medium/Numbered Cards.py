"""
Numbered Cards

You have a pack of 5 randomly numbered cards, which can range from 0-9. You can win if you can produce a higher two-digit number from your cards, than your opponent. Return True if your cards win that round.

Worked Example
win_round([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]) ➞ True
# Your cards can make the number 96
# Your opponent can make the number 73
# You win the round since 96 > 73
Examples
win_round([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]) ➞ True

win_round([1, 2, 3, 4, 5], [9, 8, 7, 6, 5]) ➞ False

win_round([4, 3, 4, 4, 5], [3, 2, 5, 4, 1]) ➞ False

Notes
Return False if you and your opponent reach the same maximum number (see example #3).
"""




################################################################
"""
Solution 1
"""


def win_round(you, opp):
	return sorted(you)[:2:-1] > sorted(opp)[:2:-1]



################################################################
"""
Solution 2
"""


def win_round(you, opp):
	highest = lambda x: int(''.join(map(str, sorted(x, reverse=True)[:2])))
	return highest(you) > highest(opp)


################################################################
"""
Solution 3
"""


def win_round(you, opp):
	you = ''.join(str(i)for i in sorted(you, reverse=True))[:2]
	opp = ''.join(str(i)for i in sorted(opp, reverse=True))[:2]
	return you > opp



#################################################################
"""
Solution 4
"""


def win_round(you, opp):
	you.sort(reverse=True)
	opp.sort(reverse=True)

	your_score = you[0] * 10 + you[1]
	opp_score = opp[0] * 10 + opp[1]

	return your_score > opp_score





