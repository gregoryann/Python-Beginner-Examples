"""
Barbecue Skewers

You are in charge of the barbecue grill. A vegetarian skewer is a skewer that has only vegetables (-o). A non-vegetarian skewer is a skewer with at least one piece of meat (-x).

For example, the grill below has 4 non-vegetarian skewers and 1 vegetarian skewer (the one in the middle).

["--xo--x--ox--",
"--xx--x--xx--",
"--oo--o--oo--",      <<< vegetarian skewer
"--xx--x--ox--",
"--xx--x--ox--"]
Given a BBQ grill, write a function that returns [# vegetarian skewers, # non-vegetarian skewers]. For example above, the function should return [1, 4].

Examples
bbq_skewers([
  "--oooo-ooo--",
  "--xx--x--xx--",
  "--o---o--oo--",
  "--xx--x--ox--",
  "--xx--x--ox--"
]) ➞ [2, 3]

bbq_skewers([
  "--oooo-ooo--",
  "--xxxxxxxx--",
  "--o---",
  "-o-----o---x--",
  "--o---o-----"
]) ➞ [3, 2]

"""


"""
Solution 1
"""

def bbq_skewers(grill):
	meat = sum(x.count('x')>0 for x in grill)
	return [len(grill)-meat,meat]

"""
Solution 2
"""

def bbq_skewers(grill):
	v = 0
	m = 0	
	for skew in grill:
		if "x" in skew:
			m =	m + 1
		else:
			v = v + 1
	return [v, m]

"""
Solution 3
"""

def bbq_skewers(grill):
  return [len(list(filter(lambda x: x.count('x')==0,grill))),len(list(filter(lambda x: x.count('x')>0,grill)))]

"""
Solution 4
"""

def bbq_skewers(grill):

    vegetable, meat = 'o', 'x'
    vegetarian_skewers, non_vegetarian_skewers = 0, 0

    for skewer in grill:
        if vegetable in skewer and not meat in skewer:
            vegetarian_skewers += 1
        else:
            non_vegetarian_skewers += 1

    return [vegetarian_skewers, non_vegetarian_skewers]




