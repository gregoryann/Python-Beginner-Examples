"""
Compounding Letters

Create a function that takes a string and returns a new string with each new character accumulating by +1. Separate each set with a dash.

Examples
accum("abcd") ➞ "A-Bb-Ccc-Dddd"

accum("RqaEzty") ➞ "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

accum("cwAt") ➞ "C-Ww-Aaa-Tttt"

Notes
Capitalize the first letter of each set.
All tests contain valid strings with alphabetic characters (a-z, A-Z).
"""





################################################################
"""
Solution 1
"""

def accum(txt):
  return '-'.join([(l*i).capitalize() for i, l in enumerate(txt, 1)])







################################################################
"""
Solution 2
"""


accum = lambda txt:  '-'.join([n*(txt.index(n)+1) for n in txt]).title()






################################################################
"""
Solution 3
"""


def accum(txt):
  lst = []
  for i in range(len(txt)):
    lst.append(txt[i].capitalize() + txt[i].lower() * i)
  new_txt = "-".join(lst)
  return new_txt







#################################################################
"""
Solution 4
"""

def accum(txt):
    out = []
    length = len(txt)
    for i in range(length):
        out.append((txt[i]*(i+1)) + "-")
        out[i] = out[i].capitalize()
    final = ''.join(group for group in out)
    final = final[:-1]
    
    return(final)





#################################################################
"""
Solution 5
"""

def accum(txt):
    lst = list(txt)
    y = 1
    for x in range(0, len(lst)):
        lst[x] = lst[x] * y
        y += 1

    lst = [x.capitalize() for x in lst]

    return '-'.join(lst)






#################################################################
"""
Solution 6
"""



    def accum(txt):
	return "-".join((ch*(idx+1)).capitalize() for idx,ch in enumerate(txt))








#################################################################
"""
Solution 7
"""


def accum(txt):
    lst = list(txt)
    newtxt =""
    n=1
    for i in range(len(lst)):
        for j in range(n):
            if( j == 0 ):
                newtxt= newtxt + lst[i].upper()
            else:
                newtxt= newtxt + lst[i].lower()
        if( i != (len(lst)-1) ):
            newtxt= newtxt + "-"
        n += 1
    return newtxt