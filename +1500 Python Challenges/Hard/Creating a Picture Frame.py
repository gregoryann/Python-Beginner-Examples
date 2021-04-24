"""
Creating a Picture Frame

Create a function that takes the width, height and character and returns a picture frame as a 2D list.

Examples
get_frame(4, 5, "#") ➞ [
  ["####"],
  ["#  #"],
  ["#  #"],
  ["#  #"],
  ["####"]
]
# Frame is 4 characters wide and 5 characters tall.


get_frame(10, 3, "*") ➞ [
  ["**********"],
  ["*        *"],
  ["**********"]
]
# Frame is 10 characters and wide and 3 characters tall.


get_frame(2, 5, "0") ➞ "invalid"
# Frame's width is not more than 2.

Notes
Remember the gap.
Return "invalid" if width or height is 2 or less (can't put anything inside).
"""


################################################################
"""
Solution 1
"""


def get_frame(w, h, ch):
    if w < 3 or h < 3:
        return 'invalid'
    result = [[ch * w]]
    for i in range(h - 2):
        result.append([ch + (w - 2) * ' ' + ch])
    result.append([ch * w])
    return result




################################################################
"""
Solution 2
"""


def get_frame(w, h, ch):
    if w<3 or h<3:
        return 'invalid'
    else:
        lst = [[w*ch], [w*ch]]
        lst1 = [ch + " " * (w-2) + ch]
        while h>=3:
            lst.insert(1, lst1)
            h -= 1
        return lst



################################################################
"""
Solution 3
"""


import numpy as np


def get_frame(w, h, ch):
	if w < 3 or h < 3: return 'invalid'
	frame = np.array([
		[0 for _ in range(w)]
		for _ in range(h)
	])
	frame[1:-1, 1:-1] += 1
	result = []
	for row in frame:
		new = [''.join(ch if i == 0 else ' ' for i in row)]
		result.append(new)
	return result



################################################################
"""
Solution 4
"""


def get_frame(w, h, ch):
	frame = []
	if w <= 2 or h <= 2: return "invalid"
	for i in range(h):
		if i in [0, h - 1]: frame.append(["".join([ch] * w)])
		else: frame.append(["".join([ch] + ([" "] * (w -2)) + [ch])])
	return frame




