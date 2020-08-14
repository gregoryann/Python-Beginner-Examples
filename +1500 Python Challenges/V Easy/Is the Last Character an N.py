"""

s the Last Character an N?
Create a function that takes a string (a random name). If the last character of the name is an "n", return True, otherwise return False.

Examples
is_last_character_n("Aiden") ➞ True

is_last_character_n("Piet") ➞ False

is_last_character_n("Bert") ➞ False

is_last_character_n("Dean") ➞ True
Notes
The function must return a boolean value ( i.e. True or False).


"""






"""
Solution 1
"""



def is_last_character_n(word):
	return word.endswith('n')



"""
Solution 2
"""

def is_last_character_n(word):
	return word[-1] == 'n'



"""
Solution 3
"""


def is_last_character_n(word):
	return True if word[-1] == "n" else False


"""
Solution 4
"""


def is_last_character_n(word):
    return True if word[-1] == "n" else False


print(is_last_character_n("Aiden"))





