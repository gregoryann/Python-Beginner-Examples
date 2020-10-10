"""
Find the Second Occurrence of "zip" in a String

Write a function that returns the position of the second occurrence of "zip" in a string, or -1 if it does not occur at least twice. Your code should be general enough to pass every possible case where "zip" can occur in a string.

Examples
find_zip("all zip files are zipped") ➞ 18

find_zip("all zip files are compressed") ➞ -1

Notes
Uppercase "Zip" is not the same as lowercase "zip".
"""




################################################################
"""
Solution 1
"""


def find_zip(txt):
	return txt.find("zip", txt.find("zip")+1)






################################################################
"""
Solution 2
"""


def find_zip(txt):
	if txt.count('zip') < 2:
		return -1
	else:
		return txt.rfind("zip")






################################################################
"""
Solution 3
"""


import re

def find_zip(txt):
	zip_search = re.compile(r"zip")
	match1 = zip_search.search(txt)
	if not match1 is None:
		match2 = zip_search.search(txt, match1.start() + 3)
		if not match2 is None:
			return match2.start()
	return -1





#################################################################
"""
Solution 4
"""


def find_zip(txt):
	return txt.rindex('zip') if txt.count('zip')>1 else -1






#################################################################
"""
Solution 5
"""


def find_zip(txt):
	if txt.count("zip")>1:
		a=txt.find("zip")
		b=txt.find("zip",a+1)
		return b
	else: return -1
