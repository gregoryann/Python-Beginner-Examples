"""
Profitable Gamble
Create a function that takes in three arguments (prob, prize, pay) and returns true if prob * prize > pay; otherwise return false.

To illustrate, profitable_gamble(0.2, 50, 9) should yield true, since the net profit is 1 (0.2 * 50 - 9), and 1 > 0.

Examples
profitable_gamble(0.2, 50, 9) ➞ True

profitable_gamble(0.9, 1, 2) ➞ False

profitable_gamble(0.9, 3, 2) ➞ True
Notes
A profitable gamble is a game that yields a positive net profit, where net profit is calculated in the following manner: net_outcome = probability_of_winning * prize - cost_of_playing.

"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""



def profitable_gamble(prob, prize, pay):
	return prob * prize > pay



"""
Solution 2
"""

def profitable_gamble(prob, prize, pay):
	outcome = prob * prize - pay
	if outcome > 0:
		return True
	else:
		return False



"""
Solution 3
"""

def profitable_gamble(prob, prize, pay):
	return  (prob * prize - pay) > 0



"""
Solution 4
"""

ef profitable_gamble(prob, prize, pay):
	return True if prob * prize > pay else False





