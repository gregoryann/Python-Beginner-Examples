"""
Name Classes

Write a class called Name and create the following attributes given a first name and last name (as fname and lname):

An attribute called fullname which returns the first and last names.
A attribute called initials which returns the first letters of the first and last name. Put a . between the two letters.
Remember to allow the attributes fname and lname to be accessed individually as well.

Examples
a1 = Name("john", "SMITH")
a1.fname ➞ "John"

a1.lname ➞ "Smith"

a1.fullname ➞ "John Smith"

a1.initials ➞ "J.S"

Notes
Make sure only the first letter of each name is capitalised.
Check the Resources tab for some helpful tutorials on Python classes.
"""



################################################################
"""
Solution 1
"""


class Name:
    
    def __init__(self, fname, lname):
        self.fname = fname.title()
        self.lname = lname.title()
        self.fullname = '{} {}'.format(self.fname, self.lname)
        self.initials = '{}.{}'.format(self.fname[0], self.lname[0])



################################################################
"""
Solution 2
"""


class Name:

	def __init__(self, f, l):
		f = f[0].upper() + f[1:].lower()
		l = l[0].upper() + l[1:].lower()
		self.fname = f
		self.lname = l
		self.fullname = f + ' ' + l
		self.initials = f[0] + '.' + l[0]








