"""
Find the Lost Dog

0 represents the dog.
Each list represents a house and each 1 represents an empty room.
Return the house and the room where it is located, there can be only one dog lost per building.
Examples
lost_dog([1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1])
➞ "Dog not found!"

lost_dog([1, 1, 1, 1, 1, 1],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1])
➞ {"Dog1": "House (2) and Room (1)", "Dog2": "House (3) and Room (2)"}

lost_dog([1, 1, 1, 1, 1, 0],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 0, 1, 1, 1])
➞ {"Dog1": "House (1) and Room (6)", "Dog2": "House (2) and Room (1)", "Dog3": "House (3) and Room (2)", "Dog4": "House (4) and Room (3)"}

Notes
Check the Resources if you're stuck.
"""



################################################################
"""
Solution 1
"""


def lost_dog(*lst):
	dogs, res = 0, {}
	
	for i in range(len(lst)):
		if 0 in lst[i]:
			dogs += 1
			k = 'Dog{}'.format(dogs)
			v = 'House ({}) and Room ({})'.format(i + 1, lst[i].index(0) + 1)
			res.update({k: v})

	return res if dogs else 'Dog not found!'





################################################################
"""
Solution 2
"""


def lost_dog(*houses):
	
	dog = lambda house: house.index(0) if 0 in house else None
	houses = {n+1: dog(houses[n]) for n in range(len(houses))}
	c = 1
	dogs = {}
	
	for n in houses.keys():
		print(n)
		house = houses[n]
		print(house)
		if house != None:
			dogs['Dog{}'.format(c)] = 'House ({}) and Room ({})'.format(n, house + 1)
			c += 1
			
	return dogs if 'Dog1' in dogs.keys() else 'Dog not found!'



################################################################
"""
Solution 3
"""


def lost_dog(*args):
    d = {}
    count = 0
    for i in range(len(args)):      
        if 0 in args[i]:
            count += 1
            d.update({"Dog{}".format(count):"House ({}) and Room ({})".format(i+1,args[i].index(0)+1)})
    return d if d else "Dog not found!"





