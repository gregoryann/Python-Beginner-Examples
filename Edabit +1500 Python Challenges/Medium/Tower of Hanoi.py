"""
Tower of Hanoi

There are three towers. The objective of the game is to move all the disks over to tower #3, but you can't place a larger disk onto a smaller disk. To play the game or learn more about the Tower of Hanoi, check the Resources tab.

Tower of Hanoi

Create a function that takes a number discs as an argument and returns the minimum amount of steps needed to complete the game.

Examples
tower_hanoi(3) ➞ 7

tower_hanoi(5) ➞ 31

tower_hanoi(0) ➞ 0

Notes
The amount of discs is always a positive integer.
1 disc can be changed per move.
"""





################################################################
"""
Solution 1
"""


tower_hanoi=lambda n:2**n-1



################################################################
"""
Solution 2
"""


def tower_hanoi(discs):
	if discs ==0:
		return 0
	else:
		lista = []
		x = 7
		for i in range(discs-2):
			lista.append(x)
			x = x*2+1
		return lista[-1]


################################################################
"""
Solution 3
"""


def tower_hanoi(discs):
	if discs < 3:
		return 0
	min_steps = 7
	for i in range(3, discs):
		min_steps = (min_steps * 2) + 1
	return min_steps


if __name__ == '__main__':
	print(tower_hanoi(5))



#################################################################
"""
Solution 4
"""

def tower_hanoi(discs):
	i = 0
	for _ in range(discs):
		i = (i * 2 + 1)
	return(i)




