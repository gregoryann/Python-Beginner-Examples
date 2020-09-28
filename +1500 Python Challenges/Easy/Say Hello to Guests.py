"""
Say Hello to Guests

In this exercise you will have to:

Take a list of names.
Add "Hello" to every name.
Make one big string with all greetings.
The solution should be one string with a comma in between every "Hello (Name)".

Examples
greet_people(["Joe"]) ➞ "Hello Joe"

greet_people(["Angela", "Joe"]) ➞ "Hello Angela, Hello Joe"

greet_people(["Frank", "Angela", "Joe"]) ➞ "Hello Frank, Hello Angela, Hello Joe"

Notes
Each greeting has to be separated with a comma and a space.
If you're given an empty list [], return an empty string "".
"""




#############################################################
#                        MY SOLUTIONS                       #
#############################################################






"""
Solution 1
"""

def greet_people(names):
	return ", ".join(["Hello " + n for n in names])

"""
Solution 2
"""

def greet_people(names):
	list_greeting = []
	for n in names:
		list_greeting.append("Hello {0}".format(n))
	greet = ", ".join(list_greeting)
	return greet

"""
Solution 3
"""

def greet_people(names):
	ending = ""
	for nam in names:
		ending += ("Hello "+nam + ", ")
		
	return ending[:-2]

"""
Solution 4
"""

def greet_people(names):
	sn = ""
	if len(names) > 0:
		for i in range(len(names)):
			sn = sn + "Hello " + names[i]
			if i < len(names)-1:
				sn = sn + ", "
	return sn


"""
Solution 5
"""

def greet_people(names):
	if len(names) == 0:
		return ''
	elif len(names) == 1:
		return 'Hello {}'.format(names[0])
	else:
		return 'Hello ' + ', Hello '.join([x for x in names])