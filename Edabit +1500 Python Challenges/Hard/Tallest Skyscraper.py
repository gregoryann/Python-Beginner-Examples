"""
Tallest Skyscraper

A city skyline can be represented as a 2-D list with 1s representing buildings. In the example below, the height of the tallest building is 4 (second-most right column).

[[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]
Create a function that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.

Examples
tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 3

tallest_skyscraper([
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 4

tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 2


"""




################################################################
"""
Solution 1
"""


def tallest_skyscraper(lst):
	return sum(1 for i in lst if sum(i)>0)




################################################################
"""
Solution 2
"""


def tallest_skyscraper(lst):
	s, lst2 = 0, []
	for i in range (len(lst[0])):
		for j in range(len(lst)):
			s += lst[j][i]
		lst2.append(s)
		s = 0
	return max(lst2)


################################################################
"""
Solution 3
"""


def tallest_skyscraper(lst):
	for i in range(len(lst)):
		if lst[i].count(1):
			return len(lst) - i


################################################################
"""
Solution 4
"""


def tallest_skyscraper(lst):
  result = []

  for row in lst:
    for i, floor in enumerate(row):
      if i < len(result):
        result[i] += floor
      else:
        result.insert(i , floor)

  result.sort(reverse=True)

  return result[0]



