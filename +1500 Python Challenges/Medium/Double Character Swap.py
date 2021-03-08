"""
Double Character Swap
Write a function to replace all instances of character c1 with character c2 and vice versa.

Examples
double_swap("aabbccc", "a", "b") ➞ "bbaaccc"

double_swap("random w#rds writt&n h&r&", "#", "&")
➞ "random w&rds writt#n h#r#"

double_swap("128 895 556 788 999", "8", "9")
➞ "129 985 556 799 888"

Notes
Both characters will show up at least once in the string.
"""





################################################################
"""
Solution 1
"""


def double_swap(txt, c1, c2):
	return txt.translate(str.maketrans(c1+c2, c2+c1))



################################################################
"""
Solution 2
"""


def double_swap(txt, c1, c2):
	dct = {c1:c2,c2:c1}
	return ''.join(dct[x] if x in dct else x for x in txt)


################################################################
"""
Solution 3
"""


def double_swap(txt, c1, c2):
	return c2.join(u.replace(c2,c1) for u in txt.split(c1))



#################################################################
"""
Solution 4
"""


def double_swap(txt, c1, c2):
	t = list(txt)
	t1 = [i.replace(c2, c1) for i in t]
	t2 = [t1[i].replace(c1, c2) if t1[i]==t[i] else t1[i] for i in range(len(t1))]
	return ''.join(t2)



