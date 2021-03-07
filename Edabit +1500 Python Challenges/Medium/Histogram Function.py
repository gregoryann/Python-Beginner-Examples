"""
Histogram Function

Build a function that creates histograms. Every bar needs to be on a new line and its length corresponds to the numbers in the list passed as an argument. The second argument of the function represents the character that needs to be used.

histogram(lst, char) -> str
Examples
histogram([1, 3, 4], "#") ➞ "#\n###\n####"

#
###
####

histogram([6, 2, 15, 3], "=") ➞ "======\n==\n===============\n==="

======
==
===============
===

histogram([1, 10], "+") ➞ "+\n++++++++++"

+
++++++++++

Notes
For better understanding try printing out the result.
"""




################################################################
"""
Solution 1
"""


def histogram(lst, char):
	return "\n".join(char * i for i in lst)



################################################################
"""
Solution 2
"""

def histogram(lst, char):
	
	class Histogram:
		
		def __init__(self, lst, char):
			self.l = lst
			self.c = char
			
			raw = []
			
			for n in range(len(self.l)):
				count = lst[n]
				item = char * count
				raw.append(item)
			
			self.gram = '\n'.join(raw)
	
	hist = Histogram(lst, char)
	
	return hist.gram




################################################################
"""
Solution 3
"""

def histogram(lst, char):
	hist = ""
	for n in lst:
		hist += n*char + "\n"
	return hist.rstrip("\n")



#################################################################
"""
Solution 4
"""


histogram = lambda n, c: '\n'.join(map(lambda x: x*c, n))





#################################################################
"""
Solution 5
"""


def histogram(lst, char):
	res = []
	for k in range(0, len(lst)):
		res.append(char*lst[k])
	return "\n".join(res)