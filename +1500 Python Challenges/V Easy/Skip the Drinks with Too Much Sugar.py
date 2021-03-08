"""
Skip the Drinks with Too Much Sugar
The function skip_the_sugar() takes in a list of drinks. Make sure the function only returns a list of drinks with no sugar in it or a little bit of sugar.

Drinks that contain too much sugar (in this challenge) are:

Cola
Fanta
Examples
skip_the_sugar(["fanta", "cola", "water"]) ➞ [water]

skip_the_sugar(["fanta", "cola"]) ➞ []

skip_the_sugar(["lemonade", "beer", "water"]) ➞ ["lemonade", "beer", "water"]
Notes
The skip_the_sugar() function returns a list of strings. All drink names are in lowercase.

"""


"""
Solution 1
"""

def skip_the_sugar(drinks):
	return [d for d in drinks if d not in ["cola", "fanta"]]

"""
Solution 2
"""

def skip_the_sugar(drinks):
    lst = []
    for i in drinks:
        if i not in ["cola", "fanta"]:
            lst.append(i)
    return lst

"""
Solution 3
"""

def skip_the_sugar(drinks):
	if 'cola' in drinks:
			drinks.remove('cola')
	if 'fanta' in drinks:
			drinks.remove('fanta')
	return drinks

"""
Solution 4
"""


def skip_the_sugar(drinks):
	list = []
	
	for i in range(0, len(drinks)):
		if drinks[i] != "fanta" and drinks[i] != "cola":
			list.append(drinks[i])
			
	return list

"""
Solution 5
"""


def skip_the_sugar(drinks):
	sugar_free = []
	sugar = "cola", "fanta"
	for i in drinks:
		if i not in sugar:
			sugar_free.append(i)
	return sugar_free