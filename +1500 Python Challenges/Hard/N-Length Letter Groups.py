"""
N-Length Letter Groups

Write a function that returns a list of strings populated from the slices of n-length characters of the given word (a slice after another while n-length applies onto the word).

Examples
collect("intercontinentalisationalism", 6)
➞ ["ationa", "interc", "ntalis", "ontine"]

collect("strengths", 3)
➞ ["eng", "str", "ths"]

collect("pneumonoultramicroscopicsilicovolcanoconiosis", 15)
➞ ["croscopicsilico", "pneumonoultrami", "volcanoconiosis"]


Notes
Ensure that the resulting array is lexicographically ordered.
Return an empty array if the given string is less than n.
A recursive version of this challenge can be found via this link.
"""





################################################################
"""
Solution 1
"""


import re

def collect(s, n):
	return sorted(re.findall(".{%d}" % n, s))




################################################################
"""
Solution 2
"""


def collect(s, n):
	if len(s)< n:
		return []
	output= []
	while len(s) > 0:
		output.append(s[:n])
		s = s[n:]
	if len(output[-1]) < n:
		output = output[:-1]
	return sorted(output)



################################################################
"""
Solution 3
"""





################################################################
"""
Solution 4
"""






