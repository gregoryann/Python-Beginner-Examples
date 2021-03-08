"""
Capitalize the Names
Create a function that takes a list of names and returns a list where only the first letter of each name is capitalized.

Examples
cap_me(["mavis", "senaida", "letty"]) ➞ ["Mavis", "Senaida", "Letty"]

cap_me(["samuel", "MABELLE", "letitia", "meridith"]) ➞ ["Samuel", "Mabelle", "Letitia", "Meridith"]

cap_me(["Slyvia", "Kristal", "Sharilyn", "Calista"]) ➞ ["Slyvia", "Kristal", "Sharilyn", "Calista"]

Notes
Don't change the order of the original list.
Notice in the second example above, "MABELLE" is returned as "Mabelle".

"""


"""
Solution 1
"""

def cap_me(lst):
  return [name.capitalize() for name in lst]


"""
Solution 2
"""

def cap_me(lst):
  newLst = []
  for l in lst:
    changed = l.title()
    newLst.append(changed)
  return newLst


"""
Solution 3
"""

def cap_me(lst):
  for i in range(len(lst)):
    name = lst[i].lower()
    capital_name = name[0].upper() + name[1:]
    lst[i] = capital_name
  return lst


"""
Solution 4
"""

def cap_me(lst):
  return [name[0].upper()+name[1:].lower() for name in lst]



"""
Solution 5
"""


cap_me=lambda l:[i.title()for i in l]



"""
Solution 6
"""


def cap_me(lst):
  result = []
  for name in lst:
    result.append(name.capitalize())
  return result

print(cap_me(['samuel', 'MABELLE', 'letitia', 'meridith'] ))