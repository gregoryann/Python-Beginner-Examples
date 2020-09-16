"""
Luke, I Am Your ...

Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.

Person	Relation
Darth Vader	father
Leia	sister
Han	brother in law
R2D2	droid

Examples
relation_to_luke("Darth Vader") ➞ "Luke, I am your father."

relation_to_luke("Leia") ➞ "Luke, I am your sister."

relation_to_luke("Han") ➞ "Luke, I am your brother in law."

"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""

def relation_to_luke(name):
	solutions = {'Leia':'sister',
	'Darth Vader':'father',
	'Han':'brother in law',
	'R2D2':'droid'}
	return 'Luke, I am your {}.'.format(solutions[name])

"""
Solution 2
"""

def relation_to_luke(name):
  return "Luke, I am your "+ {"Darth Vader":"father.","Leia":"sister.","Han":"brother in law.","R2D2":"droid."}[name]

"""
Solution 3
"""

def relation_to_luke(name):
 if name == "Darth Vader":
  return "Luke, I am your father."
 elif name == "Leia":
  return "Luke, I am your sister."
 elif name == "Han":
  return "Luke, I am your brother in law."
 else:
  return "Luke, I am your droid."
