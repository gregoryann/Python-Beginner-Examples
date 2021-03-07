"""
Negative Image

Suppose an image can be represented as a 2D list of 0s and 1s. Create a function to reverse an image. Replace the 0s with 1s and vice versa.

Examples
reverse_image([
  [1, 0, 0],
  [0, 1, 0],
  [0, 0, 1]
]) ➞ [
  [0, 1, 1],
  [1, 0, 1],
  [1, 1, 0]
]

reverse_image([
  [1, 1, 1],
  [0, 0, 0]
]) ➞ [
  [0, 0, 0],
  [1, 1, 1]
]

reverse_image([
  [1, 0, 0],
  [1, 0, 0]
]) ➞ [
  [0, 1, 1],
  [0, 1, 1]
]

"""


################################################################
"""
Solution 1
"""


def reverse_image(image):

    return [[1 if element == 0 else 0 for element in part] for part in image]



################################################################
"""
Solution 2
"""


reverse_image=lambda m:[[1-e for e in r]for r in m]



################################################################
"""
Solution 3
"""


def reverse_image(image):
	output = []
	for i in range(len(image)):
		output.append([])
		for j in range(len(image[i])):
			if image[i][j] == 0:
				output[i].append(1)
			else:
				output[i].append(0)
	return output



#################################################################
"""
Solution 4
"""


def reverse_image(image):
 return [[0 if (k == 1) else 1 for k in j] for j in image]






