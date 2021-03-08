"""
Say "Hello" Say "Bye"
Write a function that takes a string name and a number num (either 0 or 1) and return "Hello" + name if num is 1, otherwise return "Bye" + name.

Examples
say_hello_bye("alon", 1) ➞ "Hello Alon"

say_hello_bye("Tomi", 0) ➞ "Bye Tomi"

say_hello_bye("jose", 0) ➞ "Bye Jose"
Notes
The name you return must be capitalized.

"""


"""
Solution 1
"""

def say_hello_bye(name, num):
	return '{} {}'.format({0: 'Bye', 1: 'Hello'}[num], name.title())

"""
Solution 2
"""

def say_hello_bye(name, num):
	return 'Hello '+name.capitalize() if num == 1 else 'Bye '+name.capitalize()

"""
Solution 3
"""

def say_hello_bye(name, num):
    byhlo = ['Bye', 'Hello']
    return ('%s %s' % (byhlo[num], name.title()))

"""
Solution 4
"""

def say_hello_bye(name, num):
	n = name.capitalize()
	if num == 1:
		return "Hello " + n
	else:
		return "Bye " + n

"""
Solution 5
"""


def say_hello_bye(name, num):
	if (num == 1):
		return ("Hello " + name.title())
	elif (num == 0):
		return ("Bye " + name.title())

print(say_hello_bye("alon", 1))


