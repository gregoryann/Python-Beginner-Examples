"""
Noddy's Mystery Function

Noddy has written a mysterious function which takes in a word and returns True if it's passed a specific test. Solve the riddle of what Noddy's function is by having a look at some of the examples below.

Examples
noddy_function("FANTASTIC") ➞ True

noddy_function("wonderful") ➞ False

noddy_function("NODDY") ➞ False

Notes
Check the Tests tab for more examples.
This isn't really a coding challenge, more of a fun riddle ;)
"""




################################################################
"""
Solution 1
"""


def noddy_function(s):
	return not 'd' in s.lower()



################################################################
"""
Solution 2
"""

noddy_function=lambda s:'d'not in s.lower()




################################################################
"""
Solution 3
"""

def noddy_function(s):
    position = 0
    for num in range(len(s)):
        if s[num].lower() == 'd':
            position = num
    if s[position].lower() == 'd':
        return False
    else:
        return True




#################################################################
"""
Solution 4
"""

def noddy_function(s):
	for x in s:
		if x == 'd' or x == 'D':
			return False
	return True





#################################################################
"""
Solution 5
"""

def noddy_function(s):
 for i in s:
  if i in "dD": return False
 else: return True