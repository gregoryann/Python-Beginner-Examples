"""
Minimal I: If Boolean Then Boolean
In this series we're going to see common redundancies and superfluities that make our code unnecessarily complicated and less readable, and we're going to learn how to avoid them.

In line with the spirit of the series, we can summarize the general rules of minimalist code in two simple principles:

Keep your code clean and readable.
While not violating the first principle: get rid of everything superfluous.
In order to achieve this you should:

Deepen your knowledge of logics.
Deepen your understanding of the particular language you're coding with.
I would also add: observe and learn from the pros. Make a habit of checking the Solutions tab after solving a challenge on Edabit. There is absolutely nothing wrong in assimilating features of someone else's coding style, especially if yours is not yet fully developed.

Goal
In the Code tab you will find a code that is missing a single character in order to pass the tests. However, YOUR GOAL is to submit a function as minimalist as possible. Use the tips in the Tips section down below.

Write a function that returns True if the given integer is even, and False if it's odd.

Tips
Using an if statement in order to return boolean or to set a variable to a boolean is redundant.

A function that returns True if a person's age is 18 or greater and False otherwise, could be written as:

def legal_age(age):
    if age >= 18:
        return True
    else:
        return False
Notice that age >= 18 will already give us a boolean (True or False). This means that the function can be written in a much simpler and cleaner way:

def legal_age(age):
    return age >= 18
Notes
This is an open series: there isn't a definite list of features for the challenges. Please, do not hesitate to leave your suggestions in the Comment tab.
Readability is indeed a subjective concept. Let's discuss it! Feel free to leave your opinion in the Comments tab.
You can find all the exercises in this series over here.

"""



"""
Solution 1
"""

def is_even(n):
	return not n % 2

"""
Solution 2
"""

def is_even(n):
	return n % 2 == 0





