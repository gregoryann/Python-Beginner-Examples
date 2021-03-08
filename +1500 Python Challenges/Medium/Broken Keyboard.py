"""
Broken Keyboard

Given what is supposed to be typed and what is actually typed, write a function that returns the broken key(s). The function looks like:

find_broken_keys(correct phrase, what you actually typed)
Examples
find_broken_keys("happy birthday", "hawwy birthday") ➞ ["p"]

find_broken_keys("starry night", "starrq light") ➞ ["y", "n"]

find_broken_keys("beethoven", "affthoif5") ➞ ["b", "e", "v", "n"]

Notes
Broken keys should be ordered by when they first appear in the sentence.
Only one broken key per letter should be listed.
Letters will all be in lower case.
"""



################################################################
"""
Solution 1
"""


def find_broken_keys(txt1, txt2):
	missing = [a for a, b in zip(txt1, txt2) if a != b]
	return sorted(set(missing), key=txt1.index)



################################################################
"""
Solution 2
"""


def find_broken_keys(txt1, txt2):
  broken=[]
  for i in range(len(txt1)):
    if txt2[i]!=txt1[i] and txt1[i] not in broken:
      broken.append(txt1[i])
  return broken



################################################################
"""
Solution 3
"""


from collections import OrderedDict
find_broken_keys=lambda a,b:list(OrderedDict.fromkeys(x for i,x in enumerate(a)if x!=b[i]))



#################################################################
"""
Solution 4
"""


from collections import OrderedDict
find_broken_keys=lambda a,b:list(OrderedDict.fromkeys(x for i,x in enumerate(a)if x!=b[i]))



