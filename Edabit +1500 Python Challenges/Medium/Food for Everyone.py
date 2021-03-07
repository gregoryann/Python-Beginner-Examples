"""
Food for Everyone!

Create a Person class which will have three properties:

Name
List of foods they like
List of foods they hate
In this class, create the method taste():

It will take in a food name as a string.
Return {person_name} eats the {food_name}.
If the food is in the person's like list, add 'and loves it!' to the end.
If it is in the person's hate list, add 'and hates it!' to the end.
If it is in neither list, simply add an exclamation mark to the end.
Examples
p1 = Person("Sam", ["ice cream"], ["carrots"])
p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"

p1.taste("cheese") ➞ "Sam eats the cheese!"

p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"

Notes
A person can have an empty list for foods they hate and/or love.
Check the Resources for some helpful tutorials on Python classes.
"""



################################################################
"""
Solution 1
"""


class Person:
	
	def __init__ (self,name,likes,hates):
		self.name = name
		self.likes = likes
		self.hates = hates
		
	def taste(self,food):
		if food in self.likes: add = " and loves it"
		elif food in self.hates: add = " and hates it"
		else: add=""
		return self.name + " eats the " + food + add + "!"



################################################################
"""
Solution 2
"""


class Person:

    def __init__(self, name, like, hate):
        self.name = name
        self.like = like
        self.hate = hate

    def taste(self, food):
        if food in self.like:
            return '{} eats the {} and loves it!'.format(self.name, food)
        if food in self.hate:
            return '{} eats the {} and hates it!'.format(self.name, food)
        return '{} eats the {}!'.format(self.name, food)



################################################################
"""
Solution 3
"""


class Person:
    def __init__(self, name, like, hate):
        self.name = name
        self.like = like
        self.hate = hate

    def taste(self, var):
        a = var in self.like
        b = var in self.hate
        x = {
            (1, 0): " and loves it!",
            (0, 1): " and hates it!",
            (0, 0): "!"
        }[a, b]
        return "{} eats the {}{}".format(self.name, var, x)




#################################################################
"""
Solution 4
"""


class Person:
  def __init__(self,n,l_like,l_hate):
    self.n=n
    self.l_like=l_like
    self.l_hate=l_hate
    
  def taste(self,i):
    return "{} eats the {}{}!".format(self.n,i," and loves it" if i in self.l_like else " and hates it" if i in self.l_hate else "")



