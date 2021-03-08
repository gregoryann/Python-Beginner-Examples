"""
Height of the Tallest Building

Given a list of strings (depicting a skyline of several buildings), return in meters the height of the tallest building. Each line in the list represents 20m.

Examples
tallest_building_height([
  "            ##",
  "            ##",
  "            ##",
  "###   ###   ##",
  "###   ###   ###",
  "###   ###   ###",
  "###   ###   ###"
]) ➞ "140m"

# Tallest building is 7 characters
# 7 x 20m = 140m

tallest_building_height([
  "               ",
  "               ",
  "               ",
  "       #    ###",
  "      # #   ###",
  "###   ###   ###",
  "###   ###   ###"
]) ➞ "80m"

# Tallest building is 4 characters
# 4 x 20m = 80m

tallest_building_height([
  "                              ",
  "                         ###  ",
  "                         ###  ",
  "###                    #####  ",
  "###      #             #####  ",
  "###     ###            #####  ",
  "######  ###            #######",
  "######  ######  ###    #######",
  "###################    #######",
  "###############################",
  "###############################"
]) ➞ "200m"

# Tallest building is 10 characters
# 10 x 20m = 200m


Notes
There may be some open sky above buildings (can't just find the length of the list).
There may be multiple tallest buildings (see example #2).
"""



################################################################
"""
Solution 1
"""


def tallest_building_height(lst):
	return str(20*sum('#' in h for h in lst))+'m'



################################################################
"""
Solution 2
"""


def tallest_building_height(lst):
	for i in lst:
		if '#' in i:
			g=lst.index(i)
			break
	return str((len(lst)-g)*20) + 'm'



################################################################
"""
Solution 3
"""


def tallest_building_height(lst):
	lst = [i for i in lst if i.strip()]
	return '{}m'.format(len(lst)*20)



#################################################################
"""
Solution 4
"""


def tallest_building_height(lst):
	for line in lst:
		if line.find("#") >=0:
			roof_index = lst.index(line)
			break
	return "{}m".format((len(lst)-roof_index)*20)




