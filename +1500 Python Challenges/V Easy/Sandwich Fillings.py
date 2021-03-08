"""
Sandwich Fillings
Given a sandwich (as a list), return a list of fillings inside the sandwich. This involves ignoring the first and last elements.

Examples
get_fillings(["bread", "ham", "cheese", "ham", "bread"]) ➞ ["ham", "cheese", "ham"]

get_fillings(["bread", "sausage", "tomato", "bread"]) ➞ ["sausage", "tomato"]

get_fillings(["bread", "lettuce", "bacon", "tomato", "bread"]) ➞ ["lettuce", "bacon", "tomato"]
Notes
The first and last elements will always be "bread".

"""






"""
Solution 1
"""

def get_fillings(sandwich):
  return sandwich[1:-1]

"""
Solution 2
"""

def get_fillings(sandwich):
	return([s for s in sandwich if s != 'bread'])

"""
Solution 3
"""

def get_fillings(sandwich):
	del sandwich[0]
	del sandwich[-1]
	return sandwich

"""
Solution 4
"""

def get_fillings(sandwich):
	sandwich.remove('bread')
	sandwich.remove('bread')	
	return sandwich



def get_fillings(sandwich):
	sandwich.pop(0)
	sandwich.pop(len(sandwich)-1)
	return sandwich



def get_fillings(sandwich):
	n = len(sandwich)
	return sandwich[1:n-1]