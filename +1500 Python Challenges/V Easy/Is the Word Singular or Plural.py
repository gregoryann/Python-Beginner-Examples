"""

Is the Word Singular or Plural?
Create a function that takes in a word and determines whether or not it is plural. A plural word is one that ends in "s".

Examples
is_plural("changes") ➞ True

is_plural("change") ➞ False

is_plural("dudes") ➞ True

is_plural("magic") ➞ False
Notes
Don't forget to return the result.
Remember that return True (boolean) is not the same as return "True" (string).
This is an oversimplification of the English language. We are ignoring edge cases like "goose" and "geese", "fungus" and "fungi", etc.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.


"""






"""
Solution 1
"""



def is_plural(word):
	return word.endswith('s')



"""
Solution 2
"""

def is_plural(word):
	return word[-1] == 's'



"""
Solution 3
"""

def is_plural(word):
	return word[-1].lower() == "s"



"""
Solution 4
"""



def is_plural(word):
	if(word[-1]=="s"):
		return True
	return False



def is_plural(word):
	if word.endswith('s'):
		return True
	else:
		return False