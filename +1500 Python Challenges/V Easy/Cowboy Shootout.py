"""
Cowboy Shootout
Wild Roger is tasked with shooting down 6 bottles with 6 shots as fast as possible. Here are the different types of shots he could make:

He could use one pistol to shoot a bottle with a "Bang!" in 0.5 seconds.
Or he could use both pistols at once with a "BangBang!" to shoot two bottles in 0.5 seconds.
Given a list of Bangs and BangBangs return the time (in seconds) it took to shoot down all 6 bottles. Make sure to only count Bangs and BangBangs. Anything else doesn't count.

Examples
roger_shots(["Bang!", "Bang!", "Bang!", "Bang!", "Bang!", "Bang!"]) ➞ 3

roger_shots(["Bang!", "Bang!", "Bang!", "Bang!", "BangBang!"]) ➞ 2.5

roger_shots(["Bang!", "BangBangBang!", "Boom!", "Bang!", "BangBang!", "BangBang!"]) ➞ 2
Notes
All the bottles will be shot down in all the tests.

"""




"""
Solution 1
"""

def roger_shots(lst):
	return sum(i in ('Bang!', 'BangBang!') for i in lst)/2

"""
Solution 2
"""

def roger_shots(lst):
	return lst.count('Bang!') * 0.5 + lst.count('BangBang!') * 0.5

"""
Solution 3
"""
roger_shots = lambda l:(l.count('Bang!') + l.count('BangBang!'))/2

"""
Solution 4
"""

def roger_shots(lst):
	time, bottles = 0, 6
	for i in lst:
		if i == 'Bang!':
			time += .5; bottles -= 1
		elif i == 'BangBang!':
			time += .5; bottles -= 2
		if not bottles:
			return time



