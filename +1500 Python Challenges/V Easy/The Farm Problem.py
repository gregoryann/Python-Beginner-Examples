"""


The Farm Problem
In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:

chickens = 2 legs
cows = 4 legs
pigs = 4 legs
The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.

Examples
animals(2, 3, 5) ➞ 36

animals(1, 2, 3) ➞ 22

animals(5, 2, 8) ➞ 50
Notes
Don't forget to return the result.
The order of animals passed is animals(chickens, cows, pigs).
Remember that the farmer wants to know the total number of legs and not the total number of animals.

"""






"""
Solution 1
"""


def animals(chicken,cow,pig):
  return chicken * 2 + (cow + pig) * 4




"""
Solution 2
"""

def animals(chickens, cows, pigs):
		chickens  = 	chickens * 2
		cows      =		cows * 4
		pigs      =		pigs * 4
		total_number_of_legs = chickens + cows + pigs
		return total_number_of_legs



"""
Solution 3
"""

animals = lambda c, m, p: c * 2 + m * 4 + p * 4



"""
Solution 4
"""






