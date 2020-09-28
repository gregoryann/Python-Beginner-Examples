"""
Removing Enemies
Remove enemies from the list of people, even if the enemy shows up twice.

Examples
remove_enemies(["Fred"], []) ➞ ["Fred"]

remove_enemies(["Adam", "Emmy", "Tanya", "Emmy"], ["Emmy"]) ➞ ["Adam", "Tanya"]

remove_enemies(["John", "Emily", "Steve", "Sam"], ["Sam", "John"]) ➞ ["Emily", "Steve"]

Notes
All names to be removed will be in the enemies list; simply return the list, no fancy strings.
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def remove_enemies(names, enemies):
	return [i for i in names if i not in enemies]

"""
Solution 2
"""

def remove_enemies(names, enemies):
	return sorted(list(set(names)-set(enemies)),key=names.index)

"""
Solution 3
"""

def remove_enemies(names, enemies):
	for enemy in enemies:
		for name in names:
			if name == enemy:
				names.remove(name)
				
	return names





