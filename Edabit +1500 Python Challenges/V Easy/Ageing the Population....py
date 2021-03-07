"""
Ageing the Population...

Given a dictionary of people and their ages, return how old the people would be after n years have passed. Use the absolute value of n.

Examples
after_n_years({
  "Joel" : 32,
  "Fred" : 44,
  "Reginald" : 65,
  "Susan" : 33,
  "Julian" : 13
}, 1) ➞ {
  "Joel" : 33,
  "Fred" : 45,
  "Reginald" : 66,
  "Susan" : 34,
  "Julian" : 14
}

after_n_years({
  "Baby" : 2,
  "Child" : 8,
  "Teenager" : 15,
  "Adult" : 25,
  "Elderly" : 71
}, 19) ➞ {
  "Baby" : 21,
  "Child" : 27,
  "Teenager" : 34,
  "Adult" : 44,
  "Elderly" : 90
}

after_n_years({
  "Genie" : 1000,
  "Joe" : 40
}, 5) ➞ {
  "Genie" : 1005,
  "Joe" : 45
}
Notes
Assume that everyone is immortal (it would be a bit grim if I told you to remove names once they reached 75).
n should be a positive number because last time I checked, people don't tend to age backwards. Therefore, use the absolute value of n.

"""


"""
Solution 1
"""

def after_n_years(names, n):
	return {k: v + abs(n) for k, v in names.items()}

"""
Solution 2
"""

def after_n_years(names, n):
	d = {}
	for i, j in names.items():
		d[i] = j+abs(n)
	return d

"""
Solution 3
"""

def after_n_years(names, n):
    for key in names.keys():
        names[key] += abs(n)
    return names






