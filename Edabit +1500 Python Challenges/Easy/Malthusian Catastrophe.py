"""
Malthusian Catastrophe
A man named Thomas Malthus described what is now called a Malthusian Catastrophe. According to him, food production grows by a fixed amount, but population grows by a percentage. So, the food supply would soon be insufficient for the population.

Your job is to find out when that will occur. For this challenge, assume 1 population needs 1 unit of food production. Food production and population both start at 100. The year starts at 0.

The catastrophe happens when the population is larger than food production.

The function will pass:

food_growth ⁠— an integer ⁠— food production increase per year.
pop_mult ⁠— a floating-point number ⁠— population growth multiplier per year.
Examples
malthusian(4255, 1.41) ➞ 20
# { food_prod: 85,200, pop: 96,467.77..., year: 20 }

malthusian(9433, 1.09) ➞ 107
# { food_prod: 1,009,431, pop: 1,010,730.28..., year: 107 }

malthusian(5879, 1.77) ➞ 12
# { food_prod: 70,648, pop: 94,553.84..., year: 12 }

Notes
Return the year that the overtake happens, not the next year.
Make sure you don't make the mistake of adding a year, then calculating the changes to food and population. That way, you miss year 0.
If the population and food production are equal, that is not a catastrophe.
"""





################################################################
"""
Solution 1
"""

def malthusian(food_growth, pop_mult):
	x,f,p = 0,100,100
	while f>=p:
		f += food_growth
		p *= pop_mult
		x += 1
	return x





################################################################
"""
Solution 2
"""

from itertools import*
malthusian=lambda f,p:next((x for x in count()if 100*p**x>100+f*x))






################################################################
"""
Solution 3
"""

def malthusian(food_growth, pop_mult):
	food_supply = 100
	population = 100
	i = 0
	while population <= food_supply:
		food_supply += food_growth
		population *= pop_mult
		i += 1
	return i






#################################################################
"""
Solution 4
"""

def malthusian(food_growth, pop_mult):
	y, f, p = 0, 100, 100
	while p <= f:
		f += food_growth
		p *= pop_mult
		y += 1
	return y




