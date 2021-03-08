"""

Number of Stickers
Given an n * n * n Rubik's cube, return the number of individual stickers that are needed to cover the whole cube.

Examples
how_many_stickers(1) ➞ 6

how_many_stickers(2) ➞ 24

how_many_stickers(3) ➞ 54

Notes
Keep in mind there are 6 faces to keep track of.
Expect only positive whole numbers.
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""



def how_many_stickers(n):
  bruh = n*6
  return n*bruh



"""
Solution 2
"""

how_many_stickers=lambda n:6*n*n



"""
Solution 3
"""

def how_many_stickers(n):
	return 6 * n ** 2



"""
Solution 4
"""

def how_many_stickers(n):
	y = 6 * (n ** 2)
	return y




