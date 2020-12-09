"""
Rock, Paper, Scissors

Create a function which takes two strings (p1 and p2 ⁠— which represent player 1 and 2) as arguments and returns a string stating the winner in a game of Rock, Paper, Scissors.

Each argument will contain a single string: "Rock", "Paper", or "Scissors". Return the winner according to the following rules:

Rock beats Scissors
Scissors beats Paper
Paper beats Rock
If p1 wins, return the string "The winner is p1". If p2 wins, return the string "The winner is p2" and if p1 and p2 are the same, return "It's a draw".

Examples
rps("Rock", "Paper") ➞ "The winner is p2"

rps("Scissors", "Paper") ➞ "The winner is p1"

rps("Paper", "Paper") ➞ "It's a draw"

Notes
All inputs will be valid strings.
"""


################################################################
"""
Solution 1
"""


def rps(p1,p2):
	v = {'Rock':1, 'Paper':2, 'Scissors':3}
	return ["It's a draw", 'The winner is p1', 'The winner is p2'][v[p1]-v[p2]]


################################################################
"""
Solution 2
"""


def rps(p1, p2):
    wins = {('Rock', 'Scissors'), ('Paper', 'Rock'), ('Scissors', 'Paper')}
    if p1 == p2:
        return "It's a draw"
    return 'The winner is {}'.format('p1' if (p1, p2) in wins else 'p2')


################################################################
"""
Solution 3
"""


def rps(p1, p2):
    d = {'Rock': 1, 'Scissors': 2, 'Paper': 3}
    a = d.get(p1)
    b = d.get(p2)
    dif = a - b
    if dif in [-1, 2]:
        return 'The winner is p1'
    elif dif in [-2, 1]:
        return 'The winner is p2'
    else:
        return "It's a draw"




#################################################################
"""
Solution 4
"""


rps=lambda a,b:["The winner is p"+"12"[a[0]+b[0]in"RPSR"],"It's a draw"][a==b]



