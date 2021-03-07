"""
Invert Keys and Values
Write a function that inverts the keys and values of a dictionary.

Examples
invert({ "z": "q", "w": "f" })
➞ { "q": "z", "f": "w" }

invert({ "a": 1, "b": 2, "c": 3 })
➞ { 1: "a", 2: "b", 3: "c" }

invert({ "zebra": "koala", "horse": "camel" })
➞ { "koala": "zebra", "camel": "horse" }
"""



################################################################
"""
Solution 1
"""


def invert(d):
	return {v: k for k, v in d.items()}




################################################################
"""
Solution 2
"""


def invert(dct):
  return {dct[i]:i for i in dct}




################################################################
"""
Solution 3
"""


invert = lambda d: {y:x for x,y in d.items()}



#################################################################
"""
Solution 4
"""


def invert(dct):
    L=[i for i in dct.keys()]
    M=[j for j in dct.values()]
    d={}
    for x,y in list(zip(M,L)):
        d[x]=y
    return d



