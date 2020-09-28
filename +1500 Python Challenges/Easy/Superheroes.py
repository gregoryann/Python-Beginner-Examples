"""
Superheroes
Create a function that takes a list of names of superheroes and superheroines and returns a list of only the names of superheroes ending in "man" in alphabetical order.

Examples
superheroes(["Batman", "Superman", "Spider-man", "Hulk", "Wolverine", "Wonder-Woman"])
➞ ["Batman", "Spider-man", "Superman"]

superheroes(["Catwoman", "Deadpool", "Dr.Strange", "Captain-America", "Aquaman", "Hawkeye"])
➞ ["Aquaman"]

superheroes(["Wonder-Woman", "Catwoman", "Invisible-Woman"])
➞ []

Notes
Wonder-Woman, Catwoman and Invisible-Woman are superheroines.
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################





"""
Solution 1
"""

superheroes=lambda h:sorted(filter(lambda x:'man'in x and'wo'not in x.lower(),h))

"""
Solution 2
"""

def superheroes(heroes):
	return sorted(h for h in heroes if h.lower().endswith("man") and not h.lower().endswith("woman"))

"""
Solution 3
"""

def superheroes(heroes):
	substring = 'man'
	returnlst = []
	for item in heroes:
		if substring in item and 'Woman' not in item and 'woman' not in item:
			returnlst.append(item)
		else:
			pass
	returnlst.sort()
	return returnlst

"""
Solution 4
"""

def superheroes(heroes):
        ans = []
        for hero in heroes:
            if hero[(len(hero) - hero[::-1].lower().find('w')-1) :].lower() == 'woman':
                    pass
            elif hero[len(hero) - hero[::-1].lower().find('m')-1:].lower() == 'man':
                ans.append(hero)
        ans.sort()
        return ans





