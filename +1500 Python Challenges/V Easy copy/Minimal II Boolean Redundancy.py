"""
Minimal II: Boolean Redundancy
Check the principles of minimalist code in the intro to the first challenge.

In the Code tab you will find a code that is missing a single character in order to pass the tests. However, your goal is to submit a function as minimalist as possible. Use the tips in the tips section down below.

Write a function that returns the string "even" if the given integer is even, and the string "odd" if it's odd.

Tips
Converting a boolean, or something that will ultimately be interpreted as a boolean, into a boolean is redundant.

For example, the code:

boolean = bool(x < 4)
return boolean == True
Is equivalent to simply:

return x < 4
A comparison with <, <=, ==, !=, >=, > will always result in a boolean, therefore using the function bool() is totally unnecessary.
boolean == True is redundant, as it will always return boolean.
To obtain the opposite of boolean we could use boolean == False. However, a much cleaner way of doing this is simply not boolean.
While preserving readability, avoid declaring unnecessary variables.
Notes
This is an open series: there isn't a definite list of features for the challenges. Please, do not hesitate to leave your suggestions in Comments.
Readability is indeed a subjective concept. Let's discuss it! Feel free to leave your opinion in Comments.
You can find all the exercises in this series over here.

"""


"""
Solution 1
"""

def parity(n):
	return ('even', 'odd')[n % 2]

"""
Solution 2
"""

def parity(n):
	return 'odd' if n % 2 else 'even'

"""
Solution 3
"""

def parity(n):
		return 'even' if n % 2 == 0 else 'odd'

"""
Solution 4
"""

parity=lambda a:'eovdedn'[a%2::2]



def parity(n):
	if not n % 2:
	  return "even"
	else:
	  return "odd"




def parity(n):
	remander = bool(n % 2)
	if remander == True:
		return 'odd'
	return 'even'