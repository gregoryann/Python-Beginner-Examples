"""
Hamming Distance

Hamming distance is the number of characters that differ between two strings.

To illustrate:

String1: "abcbba"
String2: "abcbda"

Hamming Distance: 1 - "b" vs. "d" is the only difference.
Create a function that computes the hamming distance between two strings.

Examples
hamming_distance("abcde", "bcdef") ➞ 5

hamming_distance("abcde", "abcde") ➞ 0

hamming_distance("strong", "strung") ➞ 1

Notes
Both strings will have the same length.
"""


"""
Solution 1
"""

def hamming_distance(txt1, txt2):
	return sum(x!=y for (x,y) in zip(txt1,txt2))

"""
Solution 2
"""

def hamming_distance(txt1, txt2):
	count = 0
	for i in range (len(txt1)):
		if (txt1[i]!=txt2[i]):
			count+=1
	return count

"""
Solution 3
"""

hamming_distance=lambda a,b:len([1for i,j in zip(a,b)if i!=j])

"""
Solution 4
"""

def hamming_distance(txt1, txt2):
	h_d = 0
	for char in txt1:
		if char != txt2[txt1.index(char)]:
			h_d += 1
	return h_d




