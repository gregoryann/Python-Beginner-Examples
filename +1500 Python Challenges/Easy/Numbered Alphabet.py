"""
Numbered Alphabet

Create a function that converts a string of letters to their respective number in the alphabet.

A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	...
0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	...

Examples
alph_num("XYZ") ➞ "23 24 25"

alph_num("ABCDEF") ➞ "0 1 2 3 4 5"

alph_num("JAVASCRIPT") ➞ "9 0 21 0 18 2 17 8 15 19"

Notes
Make sure the numbers are spaced.
"""


################################################################



"""
Solution 1
"""

def alph_num(txt):
	return ' '.join(str(ord(i) - ord('A')) for i in txt)

"""
Solution 2
"""

alph_num=lambda t:' '.join(str(ord(x)-65)for x in t)

"""
Solution 3
"""

def alph_num(txt):
		lst = [ord(i)-65 for i in txt]
		return " ".join([str(i) for i in lst])

"""
Solution 4
"""

import string
def alph_num(txt):
    x = string.ascii_uppercase
    y = {v:i for i,v in enumerate(x)}
    z = [i for i in txt]
    temp = y[z[0]]
    c = 0
    res = []
    for i in z:
        res.append(str(y[z[c]]))
        c += 1
    res = " ".join(res)
    return res




