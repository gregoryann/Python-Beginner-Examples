"""
Count the Towers

Create a function that counts the number of towers.

Examples
count_towers([
  ["     ##         "],
  ["##   ##        ##"],
  ["##   ##   ##   ##"],
  ["##   ##   ##   ##"]
]) ➞ 4

count_towers([
  ["                         ##"],
  ["##             ##   ##   ##"],
  ["##        ##   ##   ##   ##"],
  ["##   ##   ##   ##   ##   ##"]
]) ➞ 6

count_towers([
  ["##"],
  ["##"]
]) ➞ 1


Notes
You are given a 2D matrix.
Towers are two characters in length.
Towers are made only of the character #.
Some tests have no towers, return 0.
"""





################################################################
"""
Solution 1
"""

def count_towers(towers):
  return towers[-1][0].count('##')




################################################################
"""
Solution 2
"""

def count_towers(towers):
	return [i for i in towers][-1][0].count('##')





################################################################
"""
Solution 3
"""

def count_towers(towers):
	if towers[0][0] == '':
		return 0
	row = towers[len(towers)-1]
	return len(row[0].split("  "))





###############################################################
"""
Solution 4
"""

def count_towers(towers):
		return len(''.join(towers[-1]).replace(' ',''))//2 if towers[-1] else 0





###############################################################
"""
Solution 5
"""


def count_towers(towers):
	tower_count =0
	for tower in towers:
		if len(tower[0].replace(' ', '')) >= tower_count:
			tower_count = len(tower[0].replace(' ', ''))
		if tower_count != 0:
			tower_count = tower_count/2

	return tower_count





###############################################################
"""
Solution 6
"""



    def count_towers(towers):
    lst = []
    if towers == []:
        return 0
    for i in towers[-1][0]:
        if i == "#":
            lst.append(i)
    return int(len(lst)/2)