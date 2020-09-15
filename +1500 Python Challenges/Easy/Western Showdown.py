"""
Western Showdown

Wild Roger is participating in a Western Showdown, meaning he has to draw (pull out and shoot) his gun faster than his opponent in a gun standoff.

Given two strings,p1 and p2, return which person drew their gun the fastest. If both are drawn at the same time, return "tie".

Examples
showdown(
  "   Bang!        ",
  "        Bang!   "
) ➞ "p1"

# p1 draws his gun sooner than p2

showdown(
  "               Bang! ",
  "             Bang!   "
) ➞ "p2"

showdown(
  "     Bang!   ",
  "     Bang!   "
) ➞ "tie"

Notes
Both strings are the same length.
"""


"""
Solution 1
"""

def showdown(p1, p2):
	v = p1.find('B') - p2.find('B')
	return 'p1' if v < 0 else 'p2' if v > 0 else 'tie'

"""
Solution 2
"""

def showdown(p1, p2):
	shot1, shot2 = p1.index('B'), p2.index('B')
	return 'p1' if shot1 < shot2 else 'p2' if shot2 < shot1 else 'tie'

"""
Solution 3
"""
def showdown(p1, p2):
  p1 = len(p1.split('B')[0])
  p2 = len(p2.split('B')[0])
  return 'tie' if p1 == p2 else 'p1' if p1 < p2 else 'p2'

"""
Solution 4
"""

def showdown(p1, p2):
	t1 = p1.index('Bang!')
	t2 = p2.index('Bang!')
	return 'p1' if t1 < t2 else 'p2' if t1 > t2 else 'tie'





