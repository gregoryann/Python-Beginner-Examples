"""
State Names and Abbreviations

Create a function that filters out a list of state names into two categories based on the second parameter.

Abbreviations abb
Full names full
Examples
filter_state_names(["Arizona", "CA", "NY", "Nevada"], "abb")
➞ ["CA", "NY"]

filter_state_names(["Arizona", "CA", "NY", "Nevada"], "full")
➞ ["Arizona", "Nevada"]

filter_state_names(["MT", "NJ", "TX", "ID", "IL"], "abb")
➞ ["MT", "NJ", "TX", "ID", "IL"]

filter_state_names(["MT", "NJ", "TX", "ID", "IL"], "full")
➞ []

Notes
State abbreviations will always be in uppercase.

"""



"""
Solution 1
"""

def filter_state_names(lst, cat):
	if cat == 'full':
		return [x for x in lst if len(x)>2]
	return [x for x in lst if len(x) == 2]


"""
Solution 2
"""


def filter_state_names(lst, cat):
	if cat=="abb":
		return list(filter(lambda x: len(x) == 2, lst))
	else:
		return list(filter(lambda x: len(x) != 2, lst))

"""
Solution 3
"""

def filter_state_names(lst, cat):
	x = []
	for i in lst:
		if len(i) == 2 and cat == "abb":
			x.append(i)
		elif len(i) > 2 and cat == "full":
			x.append(i)
	return x

"""
Solution 4
"""

def filter_state_names(lst, cat):
  if cat == "abb":
    return [x for x in lst if len(x)==2]
  else:
    return [x for x in lst if len(x)!=2]





