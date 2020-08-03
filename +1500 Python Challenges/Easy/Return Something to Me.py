"""

Return Something to Me!
Write a function that returns the string "something" joined with a space and the given parameter a.

Examples
give_me_something("is better than nothing") ➞ "something is better than nothing"

give_me_something("Bob Jane") ➞ "something Bob Jane"

give_me_something("something") ➞ "something something"
Notes
Assume an input is given.


"""






"""
Solution 1
"""


give_me_something=lambda a:'something '+a




"""
Solution 2
"""

def give_me_something(a):
		return "something " + a



"""
Solution 3
"""


def give_me_something(a):
		return 'something {}'.format(a)


"""
Solution 4
"""


def give_me_something(a):
		return("something" + " " + a)



