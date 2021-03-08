"""
Free Throw Probability

What's the probability of someone making a certain amount of free throws in a row given their free throw success percentage? If Sally makes 50% of her free shot throws. Then Sally's probability of making 5 in a row would be 3%.

Examples
free_throws("75%", 5) ➞ "24%"

free_throws("25%", 3) ➞ "2%"

free_throws("90%", 30) ➞ "4%"

Notes
The success rate is a string.
The function should return a string with the percent sign.
Round your answer to the nearest whole number.
"""




################################################################
"""
Solution 1
"""


def free_throws(p, k):
	return '{}%'.format(round((int(p[:-1])/100) ** k * 100))



################################################################
"""
Solution 2
"""


def free_throws(success, rows):
	return "{}%".format(round((int(success.replace("%", ""))/100)**rows*100))





################################################################
"""
Solution 3
"""


def free_throws(success, rows):
	# from the Binomial distribution
	p = int(success.split('%')[0]) / 100
	P = 1 * (p**rows) * (1-p)**0 
	return '{}%'.format(round(P*100))





#################################################################
"""
Solution 4
"""


def free_throws(success, rows):
	a = int(''.join([i for i in success if i.isnumeric()]))
	return '{}%'.format(round(a*((a*0.01)**(rows-1))))






#################################################################
"""
Solution 5
"""

from functools import reduce
def free_throws(success_rate, throws):
	p = int(success_rate[:-1])/100
	return '{:.0%}'.format(reduce(lambda x, y: x*y,[p]*throws))