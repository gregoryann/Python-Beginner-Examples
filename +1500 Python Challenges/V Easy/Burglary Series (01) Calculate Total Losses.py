"""
Burglary Series (01): Calculate Total Losses
You just returned home to find your mansion has been robbed! Given a dictionary of the stolen items, return the total amount of the burglary (number). If nothing was robbed, return the string "Lucky you!".

Examples
calculate_losses({
  "tv" : 30,
  "skate" : 20,
  "stereo" : 50,
}) ➞ 100

calculate_losses({
  "painting" : 20000,
}) ➞ 20000

calculate_losses({}) ➞ "Lucky you!"
Notes
The item value is always positive.

"""


"""
Solution 1
"""

def calculate_losses(items):
   return sum(items.values()) if items else "Lucky you!"

"""
Solution 2
"""

def calculate_losses(items):
	if items == {}:
		return "Lucky you!"
	else:
		return sum(items.values())

"""
Solution 3
"""

def calculate_losses(items):
     return sum(items.values()) if len(items.values())>0 else "Lucky you!"

"""
Solution 4
"""






