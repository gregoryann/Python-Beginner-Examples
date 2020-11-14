"""
Capitalize the Last Letter

Create a function that capitalizes the last letter of every word.

Examples
cap_last("hello") ➞ "hellO"

cap_last("My Name Is Edabit") ➞ "MY NamE IS EdabiT"

cap_last("HELp THe LASt LETTERs CAPITALISe") ➞ "HELP THE LAST LETTERS CAPITALISE"

Notes
There won't be any cases of punctuation in the tests.
"""




################################################################
"""
Solution 1
"""


cap_last=lambda t:" ".join(i[:-1]+i[-1].upper() for i in t.split())



################################################################
"""
Solution 2
"""


def cap_last(txt):
	txt = txt.split(" ")
	lst = []
	for i in txt:
		i = i[0:-1]+i[-1].upper()
		lst.append(i)
	return ' '.join(lst)


################################################################
"""
Solution 3
"""


def cap_last(st):
    l2 = []
    for a in st.split():
        l1 = []
        for b in a:
            l1.append(b)
        l1[-1] = l1[-1].upper()
        l2.append(''.join(l1))
    return ' '.join(l2)



#################################################################
"""
Solution 4
"""


def cap_last(txt):
  return " ".join([word[:-1] + word[-1].upper() for word in txt.split(" ")])




