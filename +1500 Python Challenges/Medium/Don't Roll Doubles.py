"""
Don't Roll Doubles!

John is playing a dice game. The rules are as follows.

Roll two dice.
Add the numbers on the dice together.
Add the total to your overall score.
Repeat this for three rounds.
But if you roll DOUBLES, your score is instantly wiped to 0 and your game ends immediately!

Create a function that takes in a list of tuples as input, and return John's score after his game has ended.

Examples
dice_game([(1, 2), (3, 4), (5, 6)]) ➞ 21

dice_game([(1, 1), (5, 6), (6, 4)]) ➞ 0

dice_game([(4, 5), (4, 5), (4, 5)]) ➞ 27

Notes
Ignore all other tuples in the list if a throw happens to be doubles and go straight to returning 0.
John only has two dice and will always give you outcomes for three rounds.
"""




################################################################
"""
Solution 1
"""


def dice_game(lst):
	return sum(a+b for a, b in lst) if not any(a==b for a, b in lst) else 0



################################################################
"""
Solution 2
"""

def dice_game(lst):
    myScore = 0
    for i in range(len(lst)):
        if lst[i][0] == lst[i][1]:
            myScore = 0
            break
        else:
            myScore += lst[i][0] + lst[i][1]
    return myScore



################################################################
"""
Solution 3
"""


def dice_game(lst):
	a = []
	for i in lst:
		for j in range(len(i)):
			if i[j]!=i[j-1]:
				a.append(i[j])
	return sum(a) if len(a)/2 == len(lst) else 0



#################################################################
"""
Solution 4
"""



def dice_game(lst):
	total=0
	for x in lst:
		
		# print(x)
		dice_1=x[0]
		dice_2=x[1]

		if dice_1==dice_2:

			return 0
		else:
			# break
			total_dice=dice_1+dice_2
			total+=total_dice
	return total
print(diceGame([(1,2),(3,4),(5,5)]))



