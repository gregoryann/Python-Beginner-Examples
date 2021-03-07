"""
Book Shelf

Create a Book class that has two attributes:

.title
.author
and two methods:

A method named .get_title() that returns: "Title: " + the instance title.
A method named .get_author() that returns: "Author: " + the instance author.
and instantiate this class by creating 3 new books:

Pride and Prejudice - Jane Austen (PP)
Hamlet - William Shakespeare (H)
War and Peace - Leo Tolstoy (WP)
Name the new instances should be PP, H, and WP, respectively.

For instance, if I instantiated the following book using this Book class:

Harry Potter - J.K. Rowling (HP)
I would get the following attributes and methods:

Examples
HP.title ➞ "Harry Potter"
HP.author ➞ "J.K. Rowling"
HP.get_title() ➞ "Title: Harry Potter"
HP.get_author() ➞ "Author: J.K. Rowling"


Notes
Read more about Python classes in Resources.
Remember, after you've finished writing the class and its methods, you must instantiate it through the creation of new objects.
"""




################################################################
"""
Solution 1
"""


class Book:

	def __init__(self, title, author):
		self.title = title
		self.author = author
		
	def get_title(self):
		return 'Title: ' + self.title
		
	def get_author(self):
		return 'Author: ' + self.author


PP = Book('Pride and Prejudice', 'Jane Austen')
H = Book('Hamlet', 'William Shakespeare')
WP = Book('War and Peace', 'Leo Tolstoy')




################################################################
"""
Solution 2
"""


class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author
	
	def get_title(self):
		return "Title: {}".format(self.title)
		
	def get_author(self):
		return "Author: {}".format(self.author)

PP = Book("Pride and Prejudice", "Jane Austen")
H = Book("Hamlet", "William Shakespeare")
WP = Book("War and Peace", "Leo Tolstoy")



################################################################
"""
Solution 3
"""


class Book:
	def __init__(self, title, author):
		self.author = author
		self.title = title
	def get_title(self):
		return "Title: {}".format(self.title)
	def get_author(self):
		return "Author: {}".format(self.author)

PP = Book("Pride and Prejudice", "Jane Austen")
H = Book("Hamlet", "William Shakespeare")
WP = Book("War and Peace", "Leo Tolstoy")

print(PP.title)
print(PP.author)
print(PP.get_title())
print(PP.get_author())

print(H.title)
print(H.author)
print(H.get_title())
print(H.get_author())

print(WP.title)
print(WP.author)
print(WP.get_title())
print(WP.get_author())





