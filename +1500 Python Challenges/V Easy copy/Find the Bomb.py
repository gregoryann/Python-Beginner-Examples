"""
Find the Bomb
Create a function that finds the word "bomb" in the given string. If found, return "Duck!!!", otherwise, return "There is no bomb, relax.".

Examples
bomb("There is a bomb.") ➞ "Duck!!!"

bomb("Hey, did you think there is a bomb?") ➞ "Duck!!!"

bomb("This goes boom!!!") ➞ "There is no bomb, relax."
Notes
"bomb" may appear in different cases (i.e. uppercase, lowercase, mixed).

"""


"""
Solution 1
"""

def bomb(s): 
	return ['There is no bomb, relax.', 'Duck!!!']['bomb' in s.lower()]

"""
Solution 2
"""

def bomb(txt):
	return "Duck!!!" if "bomb" in txt.lower() else "There is no bomb, relax."

"""
Solution 3
"""

def bomb(txt):
	txt = txt.lower()
	if 'bomb' in txt:
		return 'Duck!!!'
	else:
		return 'There is no bomb, relax.'

"""
Solution 4
"""

def bomb(txt):
  return "Duck!!!" if txt.lower().find("bomb") > 0 else "There is no bomb, relax."


"""
Solution 5
"""


def bomb(txt):

   a=txt.split()
  
   for i in txt:
     if "bomb" in txt.lower():
       return "Duck!!!"
     else:
       return "There is no bomb, relax."