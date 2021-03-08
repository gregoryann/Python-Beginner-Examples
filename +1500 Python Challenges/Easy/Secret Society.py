"""
Secret Society

A group of friends have decided to start a secret society. The name will be the first letter of each of their names, sorted in alphabetical order.

Create a function that takes in a list of names and returns the name of the secret society.

Examples
society_name(["Adam", "Sarah", "Malcolm"]) ➞ "AMS"

society_name(["Harry", "Newt", "Luna", "Cho"]) ➞ "CHLN"

society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]) ➞ "CJMPRR"

Notes
The secret society's name should be entirely uppercased.
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def society_name(friends):
	return ''.join(sorted(i[0] for i in friends))

"""
Solution 2
"""
def society_name(friends):
	friends.sort()
	return "".join([i[0] for i in friends])
    
"""
Solution 3
"""
def society_name(friends):
	name=""
	friends.sort()
	for i in friends:
		name+=i[0]
	return name

"""
Solution 4
"""

def society_name(friends):

    initials = [name[0] for name in friends]
    return ''.join(sorted(initials))





