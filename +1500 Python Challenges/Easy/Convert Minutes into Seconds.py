"""

Convert Minutes into Seconds
Write a function that takes an integer minutes and converts it to seconds.

Examples
convert(5) ➞ 300

convert(3) ➞ 180

convert(2) ➞ 120
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.


"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""


def convert(minutes):
	seconds = minutes * 60
	return seconds




"""
Solution 2
"""


def convert(minutes):
	return minutes * 60


"""
Solution 3
"""


def convert(minutes):
    seconds = minutes * 60
    return seconds

ex1 = 5
ex2 = 3
ex3 = 2

print(convert(ex1))
print(convert(ex2))
print(convert(ex3))


"""
Solution 4
"""

def convert(minutes):

	con = minutes * 60
	
	return con




