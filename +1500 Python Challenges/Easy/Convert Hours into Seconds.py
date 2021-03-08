"""


Convert Hours into Seconds
Write a function that converts hours into seconds.

Examples
how_many_seconds(2) ➞ 7200

how_many_seconds(10) ➞ 36000

how_many_seconds(24) ➞ 86400
Notes
60 seconds in a minute, 60 minutes in an hour
Don't forget to return your answer.

"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""



def how_many_seconds(hours):
	return hours * 3600



"""
Solution 2
"""

how_many_seconds=lambda h:3600*h



"""
Solution 3
"""

def how_many_seconds(hours):
	seconds = hours * 60 * 60
	return seconds



"""
Solution 4
"""

def how_many_seconds(hours):
	seconds = hours * 3600
	return seconds




