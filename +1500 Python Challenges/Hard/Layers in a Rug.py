"""
Layers in a Rug

Write a function that counts how many concentric layers a rug.

Examples
count_layers([
  "AAAA",
  "ABBA",
  "AAAA"
]) ➞ 2

count_layers([
  "AAAAAAAAA",
  "ABBBBBBBA",
  "ABBAAABBA",
  "ABBBBBBBA",
  "AAAAAAAAA"
]) ➞ 3

count_layers([
  "AAAAAAAAAAA",
  "AABBBBBBBAA",
  "AABCCCCCBAA",
  "AABCAAACBAA",
  "AABCADACBAA",
  "AABCAAACBAA",
  "AABCCCCCBAA",
  "AABBBBBBBAA",
  "AAAAAAAAAAA"
]) ➞ 5


Notes

Multiple layers can share the same component so count them separately (example #2).
Layers will be horizontally and vertically symmetric.
There will be at least one layer for each rug.
"""



################################################################
"""
Solution 1
"""


def count_layers(rug):
	layers = list()
	count = 0
	for layer in rug:
		if layer not in layers:
			layers.append(layer)

	return len(layers)




################################################################
"""
Solution 2
"""


import itertools
def count_layers(rug):
	result = (len([1 for k,g in itertools.groupby(rug[len(rug)//2])])+1)//2
	return result



################################################################
"""
Solution 3
"""


def count_layers(rug, layers = 1):
	x = len(rug) // 2
	y = len(rug[x]) // 2 + 1
	for i in range(1, len(rug[x][:y])):
		if rug[x][i] == rug[x][-i]: continue
		else: layers += 1
	return layers




################################################################
"""
Solution 4
"""


def count_layers(rug):
	list = []
	ans = 0
	if len(rug) == 1:
		return 1
	for layer in rug:
		if layer not in list:
			ans += 1
			list.append(layer)
	return ans




