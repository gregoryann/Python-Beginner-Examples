"""
Older Than Me

Create a method in the Person class which returns how another person's age compares. Given the objects p1, p2 and p3, which will be initialised with the attributes name and age, return a sentence in the following format:

{other_person} is {older than / younger than / the same age as} me.

Examples
p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)
p1.compare_age(p2) ➞ "Joel is older than me."

p2.compare_age(p1) ➞ "Samuel is younger than me."

p1.compare_age(p3) ➞ "Lily is the same age as me."

Notes
Check out the Resources tab for some helpful tutorials on Python classes!
If you're really stuck, check out the Solutions tab for answers.
"""


########################################################################



"""
Solution 1
"""

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def compare_age(self, other):
		if other.age < self.age:
			s = 'younger than'
		elif other.age > self.age:
			s = 'older than'
		elif other.age == self.age:
			s = 'the same age as'
		return '{} is {} me.'.format(other.name,s)



"""
Solution 2
"""

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def compare_age(self, other):
		txt = [
			'younger than', 
			'the same age as', 
			'older than'
			][(self.age <= other.age) + (self.age < other.age)]
			
		return '{} is {} me.'.format(other.name, txt)



"""
Solution 3
"""

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def compare_age(self, other):
		if other.age > self.age:
			return other.name + ' is older than me.'
		elif other.age < self.age:
			return other.name + ' is younger than me.'
		else:
			return other.name + ' is the same age as me.'


"""
Solution 4
"""

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def compare_age(self, other):
		if self.age < other.age: return other.name + ' is older than me.'
		if self.age == other.age: return other.name + ' is the same age as me.'
		if self.age > other.age: return other.name + ' is younger than me.'





