"""
Turn That Frown Upside Down

It is important to be happy! Therefore, you must create a function that takes a sentence containing sad faces and turn them into happy ones! This involves changing only the mouths.

Sad face examples: :( 8( x( ;(
Happy face examples: :) 8) x) ;)
Make sure to only change the face if there are eyes before them, round(3.4) wouldn't become round)3.4) (for example).

Examples
make_happy("My current mood: :(") ➞ "My current mood: :)"

make_happy("I was hungry 8(") ➞ "I was hungry 8)"

make_happy("print('x(')") ➞ "print('x)')"

Notes
Faces such as :((((((( are not included.
"""



################################################################
"""
Solution 1
"""


def make_happy(s):
	for eye in ':8x;':
		s = s.replace(eye+'(',eye+')')
	return s



################################################################
"""
Solution 2
"""


def make_happy(s):
	frown = [':(','8(','x(',';(']; smile = [':)','8)','x)',';)']
	for i in range(4):
		s = s.replace(frown[i],smile[i])
	return s



################################################################
"""
Solution 3
"""


import re
make_happy=lambda s:re.sub(r"([8x:;])\(",r"\1)",s)


#################################################################
"""
Solution 4
"""


import re
def make_happy(txt):
	return re.sub('(?<=[:8x;])\(',')',txt)



