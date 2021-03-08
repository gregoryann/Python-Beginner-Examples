"""
Stalactites or Stalagmites?

Stalactites hang from the ceiling of a cave while stalagmites grow from the floor.

Create a function that determines whether the input represents "stalactites" or "stalagmites". If it represents both, return "both". Input will be a 2D list, with 1 representing a piece of rock, and 0 representing air space.

Examples
mineral_formation([
  [0, 1, 0, 1],
  [0, 1, 0, 1],
  [0, 0, 0, 1],
  [0, 0, 0, 0]
]) ➞ "stalactites"

mineral_formation([
  [0, 0, 0, 0],
  [0, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]) ➞ "stalagmites"

mineral_formation([
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]) ➞ "both"

Notes
There won't be any examples where both stalactites and stalagmites meet (because those are called pillars).
There won't be any example of neither stalactites or stalagmites.
"""





################################################################
"""
Solution 1
"""


def mineral_formation(cave):
  return ['both', 'stalactites', 'stalagmites'][(1 in cave[0]) - (1 in cave[-1])]



################################################################
"""
Solution 2
"""


def mineral_formation(cave):
	return {
		(1, 1): 'both',
		(1, 0): 'stalactites',
		(0, 1): 'stalagmites'
	}[1 in cave[0], 1 in cave[-1]]




################################################################
"""
Solution 3
"""


def mineral_formation(cave):
    tites = cave[0].count(1)
    mites = cave[-1].count(1)
    if mites and tites:     return 'both'
    if mites:               return 'stalagmites'
    return 'stalactites'



#################################################################
"""
Solution 4
"""



def mineral_formation(cave):
	k = []
	sta = cave[0]
	for index in sta:
		if index == 1:
			k.append("stalactites")
			break
	stal = cave[-1]
	for index in stal:
		if index == 1:
			k.append("stalagmites")
			break
	if len(k) == 2:
		return "both"
	else:
		return k[0]




