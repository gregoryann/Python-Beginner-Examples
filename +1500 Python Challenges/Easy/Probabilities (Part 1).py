"""
Probabilities (Part 1)
Given a list of numbers and a value n, write a function that returns the probability of choosing a number greater than or equal to n from the list. The probability should be expressed as a percentage, rounded to one decimal place.

Examples
probability([5, 1, 8, 9], 6) ➞ 50.0

probability([7, 4, 17, 14, 12, 3], 16) ➞ 16.7

probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6) ➞ 70.0

Notes
Precent probability of event = 100 * (num of favourable outcomes) / (total num of possible outcomes)
"""


"""
Solution 1
"""

def probability(lst, n):
	return round(sum(1 for x in lst if x >= n) / len(lst) * 100, 1)

"""
Solution 2
"""

probability=lambda x,n:round(sum(i>=n for i in x)*100/len(x),1)





