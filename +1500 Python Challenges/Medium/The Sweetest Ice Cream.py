"""
The Sweetest Ice Cream

Create a function which takes a list of objects from the class IceCream and returns the sweetness value of the sweetest icecream. Note that there is a class is provided for you in the Tests tab.

class IceCream:
  def __init__(self, flavor, num_sprinkles):
    self.flavor = flavor
    self.num_sprinkles = num_sprinkles
Each sprinkle has a sweetness value of 1
Check below for the sweetness values of the different flavors.
Flavors	Sweetness Value
Plain	0
Vanilla	5
ChocolateChip	5
Strawberry	10
Chocolate	10
Examples
ice1 = IceCream("Chocolate", 13)         # value of 23
ice2 = IceCream("Vanilla", 0)           # value of 5
ice3 = IceCream("Strawberry", 7)         # value of 17
ice4 = IceCream("Plain", 18)             # value of 18
ice5 = IceCream("ChocolateChip", 3)      # value of 8
sweetest_icecream([ice1, ice2, ice3, ice4, ice5]) ➞ 23

sweetest_icecream([ice3, ice1]) ➞ 23

sweetest_icecream([ice3, ice5]) ➞ 17


Notes
Remember to only return the sweetness value.
IceCream class is provided (check Tests tab).
"""




################################################################
"""
Solution 1
"""


def sweetest_icecream(lst):
	flavor_values = {
	'Plain' :	0,
	'Vanilla' :	5,
	'ChocolateChip' :	5,
	'Strawberry' : 10,
	'Chocolate'	: 10
	}
	
	return max(i.num_sprinkles + flavor_values[i.flavor] for i in lst)



################################################################
"""
Solution 2
"""


def sweetest_icecream(lst):
    value = {'Plain': 0, 'Vanilla': 5, 'ChocolateChip': 5,
             'Strawberry': 10, 'Chocolate': 10}
    return max(map(lambda x: value[x.flavor]+x.num_sprinkles, lst))



################################################################
"""
Solution 3
"""


def sweetest_icecream(lst):
	sw={'Plain':0,'Vanilla':5,'ChocolateChip':5,'Strawberry':10,'Chocolate':10}
	total=[]
	for i in lst:	
		total.append(sw[i.flavor]+i.num_sprinkles)
	return max(total)



#################################################################
"""
Solution 4
"""


def sweetest_icecream(lst):
 dic={"Plain":0,"Vanilla":5,"ChocolateChip":5,"Strawberry":10,"Chocolate":10}
 lst_1=[]
 for i in lst:
  lst_1.append(dic[i.flavor]+i.num_sprinkles)
 return max(lst_1)



