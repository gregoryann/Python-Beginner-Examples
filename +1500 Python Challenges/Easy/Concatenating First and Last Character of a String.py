"""

Concatenating First and Last Character of a String
Creates a function that takes a string and returns the concatenated first and last character.

Examples
first_last("ganesh") ➞ "gh"

first_last("kali") ➞ "ki"

first_last("shiva") ➞ "sa"

first_last("vishnu") ➞ "vu"

first_last("durga") ➞ "da"
Notes
There is no empty string.


"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""



def first_last(name):
	return name[0]+name[-1]



"""
Solution 2
"""


first_last=lambda n:n[0]+n[-1]


"""
Solution 3
"""

def first_last(name):
	return name[0]+name[len(name)-1]



"""
Solution 4
"""


def first_last(name):
  return "{}{}".format(name[0], name[-1])







  def first_last(name):
	return(name[0]+name[-1])
print(first_last("kali"))





