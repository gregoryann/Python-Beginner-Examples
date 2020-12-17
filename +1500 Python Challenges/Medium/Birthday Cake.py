"""
Birthday Cake
Create a function which constructs a rectangular birthday cake, based on someone's name and age! Build it out of strings in a list and makes sure to surround the birthday message with the character that fits the rule:

If the age is an even number, surround the message with "#".
If the age is an odd number, surround the message with "*".
Other important rules:

The message should be in the format: {age} Happy Birthday {name}! {age}
Leave a space between the edge of the cake and the age numbers.
Examples
get_birthday_cake("Jack", 10) ➞ [
  "##############################",
  "# 10 Happy Birthday Jack! 10 #",
  "##############################"
]

get_birthday_cake("Russell", 19) ➞ [
  "*********************************",
  "* 19 Happy Birthday Russell! 19 *",
  "*********************************"
]

get_birthday_cake("Isabelle", 2) ➞ [
  "################################",
  "# 2 Happy Birthday Isabelle! 2 #",
  "################################"
]

"""



################################################################
"""
Solution 1
"""


def get_birthday_cake(name, age):
	char = ['#', '*'][age%2]
	msg = '{0} {1} Happy Birthday {2}! {1} {0}'.format(char, age, name)
	wall = char * len(msg)
	return [wall, msg, wall]



################################################################
"""
Solution 2
"""


def get_birthday_cake(name, age):
    line2 = " {0} Happy Birthday {1}! {0} ".format(age, name)
    tot_len = len(line2) + 2
    cake = []
    for line in range(3):
        if line == 0 or line == 2:
            if age % 2 == 0:
                cake.append("#" * tot_len)
            else:
                cake.append("*" * tot_len)
        else:
            if age % 2 == 0:
                cake.append("#" + line2 + "#")
            else:
                cake.append("*" + line2 + "*")
    return cake



################################################################
"""
Solution 3
"""


# 10 Happy Birthday Jack! 10 #

def get_birthday_cake(name, age):
	ans = []
	if age % 2 == 0:
		s = '#'
	else:
		s = '*'
	v = s + " " + str(age) + " Happy Birthday " + name + "! " + str(age) + " " + s
	ans.append(s * len(v))
	ans.append(v)
	ans.append(s*len(v))
	return ans



#################################################################
"""
Solution 4
"""


def get_birthday_cake(name, age):
  m = '#*'[age % 2].join(["", " {} Happy Birthday {}! {} ".format(age, name, age), ""])
  return ['#*'[age % 2]*len(m), m, '#*'[age % 2]*len(m)]



