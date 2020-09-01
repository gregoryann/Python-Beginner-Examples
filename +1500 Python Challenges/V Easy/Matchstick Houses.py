"""
Matchstick Houses
This challenge will help you interpret mathematical relationships both algebraically and geometrically.

Matchstick Houses, Steps 1, 2 and 3

Create a function that takes a number (step) as an argument and returns the number of matchsticks in that step. See step 1, 2 and 3 in the image above.

Examples
match_houses(1) ➞ 6

match_houses(4) ➞ 21

match_houses(87) ➞ 436
Notes
Step 0 returns 0 matchsticks.
The input (step) will always be a non-negative integer.
Think of the input (step) as the total number of houses that have been connected together.

"""



"""
Solution 1
"""

def match_houses(step):
  return step*5+1 if step else 0


"""
Solution 2
"""

def match_houses(step):
	diff = 5
	house = 6
	if step != 0:
		return (house + ((step - 1) * diff))
	else:
		return 0

"""
Solution 3
"""

def match_houses(step):
	return step * 6 - (step-1) if step > 0 else 0

"""
Solution 4
"""

def match_houses(step):
	sticks = [0, 6]
	for i in range(1, 100):
		sticks.append(6+i*5)
	return sticks[step]




