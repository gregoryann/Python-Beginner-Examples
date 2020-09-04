"""
Smash Factor
Smash factor is a term in golf that relates to the amount of energy transferred from the club head to the golf ball. The formula for calculating smash factor is ball speed divided by club speed.

Create a function that takes ball speed bs and club speed cs as arguments and returns the smash factor to the nearest hundredth.

Examples
smash_factor(139.4, 93.8) ➞ 1.49

smash_factor(181.2, 124.5) ➞ 1.46

smash_factor(154.7, 104.3) ➞ 1.48
Notes
Remember to round to the nearest hundredth.
All values will be valid (so no dividing by zero).


"""






"""
Solution 1
"""

smash_factor=lambda a,b:round(a/b,2)





"""
Solution 2
"""

def smash_factor(bs, cs):
	return round(bs/cs,2)



"""
Solution 3
"""


smash_factor = lambda b, c: round(b/c, 2)


"""
Solution 4
"""






