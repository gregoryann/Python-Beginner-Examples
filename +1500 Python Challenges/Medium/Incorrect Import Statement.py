"""
Incorrect Import Statement

When importing objects from a module in Python, the syntax usually is as follows:

from module_name import object
Given a string of an incorrect import statement, return the fixed string. All import statements will be the wrong way round.

Examples
fix_import("import object from module_name") ➞ "from module_name import object"

fix_import("import randint from random") ➞ "from random import randint"

fix_import("import pi from math") ➞ "from math import pi"

Notes
All Tests will be valid strings.
"""



################################################################
"""
Solution 1
"""


def fix_import(s):
	return 'from {} import {}'.format(s.split()[-1], s.split()[1])



################################################################
"""
Solution 2
"""


def fix_import(s):
	return ' '.join(s.split()[-2:] + s.split()[:2])



################################################################
"""
Solution 3
"""


def fix_import(s):
   
	k=s.split(' ')
	return 'from {} import {}'.format(k[3],k[1])



#################################################################
"""
Solution 4
"""


def fix_import(s):
				R=''
				L=s.split(' ')
				for i in [2,3,0,1]:
								R=R+L[i]+' ' if i!=1 else R+L[i]
				return R



