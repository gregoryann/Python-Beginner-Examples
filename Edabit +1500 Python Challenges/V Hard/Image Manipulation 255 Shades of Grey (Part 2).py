"""
Image Manipulation: 255 Shades of Grey (Part 2)

Images can be described as 3D lists.

# This image has only one white pixel:

[
  [[255, 255, 255]]
]
# This one is a 2 by 2 black image:

[
  [[0, 0, 0], [0, 0, 0]],
  [[0, 0, 0], [0, 0, 0]]
]
Your task is to create a function that takes a 3D list representation of an image and returns the grayscale version of that.

Examples
grayscale([
  [[0, 0, 0], [0, 0, 157]],
  [[1, 100, 0], [0, 10, 0]]
]) ➞ [
  [[0, 0, 0], [52, 52, 52]],
  [[34, 34, 34], [3, 3, 3]]
]


Notes
A valid RGB value ranges from 0 to 255 (inclusive).
If the given list contains out of bound values, convert them to the nearest valid one.
Grayscaling an image is adjusting to have the same amount of (Red, Green, Blue) from their combined average to produce different shades of gray.
"""






################################################################
"""
Solution 1
"""


def grayscale(lst):
		for i in range(len(lst)):
				for j in range(len(lst[0])):
						vals = [0 if v < 0 else 255 if v > 255 else v for v in lst[i][j]]
						lst[i][j] = [round(sum(vals)/3)] * 3
		return lst




################################################################
"""
Solution 2
"""


MAX_RGB = 255
MIN_RGB = 0
def bound(lst):
	res = []
	for i in lst:
		res.append(min(max(MIN_RGB,i), MAX_RGB))
	return res
		
def grayscale(lst):
	grey_lst = []
	for i, row in enumerate(lst):
		grey_lst.append([])
		for px in row:
			px = bound(px)
			px = [round(sum(px) / len(px))] * len(px)
			grey_lst[i].append(px)
	return grey_lst




################################################################
"""
Solution 3
"""


def grayscale(lst):
	isGrey = lambda a: all([a[0]==x for x in a])
	prep = lambda a: [255 if x>255 else (0 if x<0 else x) for x in a]
	makeGrey = lambda a: [round(sum(a)/len(a)) for x in a]
	return [[pixels if isGrey(pixels) else makeGrey(prep(pixels))
					for pixels in pic]
						for pic in lst]



################################################################
"""
Solution 4
"""


grayscale=lambda l:[[[round(sum(((y,0)[y<0],255)[y>255]for y in x)/3)]*3for x in z]for z in l]





################################################################
"""
Solution 5
"""


def grayscale(lst):
  b = [[[k if 0<=k<=255 else 255 if k>255 else 0 for k in j]
	   for j in i]for i in lst]
  a = []
  for i in b:
        a.append([[round(sum(j)/3)]*len(j) for j in i])
  return a