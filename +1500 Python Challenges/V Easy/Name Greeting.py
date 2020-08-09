"""

Name Greeting!
Create a function that takes a name and returns a greeting in the form of a string.

Examples
hello_name("Gerald") ➞ "Hello Gerald!"

hello_name("Tiffany") ➞ "Hello Tiffany!"

hello_name("Ed") ➞ "Hello Ed!"
Notes
The input is always a name (as string).
Don't forget the exclamation mark!
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.


"""






"""
Solution 1
"""


def hello_name(name):
	return "Hello {}!".format(name)




"""
Solution 2
"""


def hello_name(name):
	return "Hello {}!".format(name)


"""
Solution 3
"""


def hello_name(name):
	return "Hello " + name +"!"


"""
Solution 4
"""

def hello_name(name):
	return ("Hello %s!") %name




