"""
Printer Levels
Given a dictionary of how many more pages each ink color can print, output the maximum number of pages the printer can print before any of the colors run out.

Examples
ink_levels({
  "cyan": 23,
  "magenta": 12,
  "yellow": 10
}) ➞ 10

ink_levels({
  "cyan": 432,
  "magenta": 543,
  "yellow": 777
}) ➞ 432

ink_levels({
  "cyan": 700,
  "magenta": 700,
  "yellow": 0
}) ➞ 0
Notes
A single printed page requires each color once, so printing is not possible if any of the slots lack ink (see example #3).

"""



"""
Solution 1
"""

def ink_levels(inks):
	return min(inks.values())

"""
Solution 2
"""

def ink_levels(inks):
    lst = []
    for i in inks:
            lst.append(inks.get(i))
    return min(lst)

"""
Solution 3
"""

def ink_levels(inks):
    return min([inks['cyan'], inks['magenta'], inks['yellow']])

"""
Solution 4
"""

def ink_levels(inks):
	pages = list(inks.values())
	pages.sort()
	return pages[0]

