"""
Four Passengers and a Driver

A typical car can hold four passengers and one driver, allowing five people to travel around. Given n number of people, return how many cars are needed to seat everyone comfortably.

Examples
cars_needed(5) ➞ 1

cars_needed(11) ➞ 3

cars_needed(0) ➞ 0

Notes
It's likely there will be a few people left over and some cars won't be filled to max capacity.
"""



"""
Solution 1
"""

def cars_needed(n):
  return (n + 4) // 5

"""
Solution 2
"""

from math import ceil

def cars_needed(n):
	return ceil(n/5)

"""
Solution 3
"""

def cars_needed(n):
	x=n/5
	x_int=x.is_integer()
	if(x_int == True):
		return x
	else:
		return (int(x)+1)

"""
Solution 4
"""

import math
cars_needed=lambda n:math.ceil(n/5)




