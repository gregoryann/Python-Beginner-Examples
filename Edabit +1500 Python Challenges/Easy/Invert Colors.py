"""
Invert Colors

Create a function that inverts the rgb values of a given tuple.

Examples
color_invert((255, 255, 255)) ➞ (0, 0, 0)
# (255, 255, 255) is the color white.
# The opposite is (0, 0, 0), which is black.

color_invert((0, 0, 0)) ➞ (255, 255, 255)

color_invert((165, 170, 221)) ➞ (90, 85, 34)

Notes
Must return a tuple.
255 is the max value of a single color channel.
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def color_invert(rgb):
	r,g,b=rgb
	m = 255
	return m-r, m-g, m-b

"""
Solution 2
"""

def color_invert(rgb):
    lst = []
    for x in rgb:
        lst.append(abs(x - 255))
    return tuple(lst)

"""
Solution 3
"""

def color_invert(rgb):
	r=255-rgb[0]
	g=255-rgb[1]
	b=255-rgb[2]
	return (r,g,b)

"""
Solution 4
"""

def color_invert(rgb):
	lst = list(rgb)
	for i in range(0,len(lst)):
		lst[i]=abs(255-lst[i])
	
	return tuple(lst)





