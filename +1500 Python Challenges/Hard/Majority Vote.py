"""
Majority Vote

Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).

Examples
majority_vote(["A", "A", "B"]) ➞ "A"

majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"

majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None


Notes
The frequency of the majority element must be strictly greater than 1/2.
If there is no majority element, return None.
If the list is empty, return None.
"""


################################################################
"""
Solution 1
"""


def majority_vote(lst): 
  for i in set(lst):
    if lst.count(i)>len(lst)//2:
      return i
  return None



################################################################
"""
Solution 2
"""


def majority_vote(l):
 for e in l:
  if l.count(e)>len(l)/2:return e



################################################################
"""
Solution 3
"""


from collections import Counter
def majority_vote(lst):
  if len(lst) == 0:
    return None
  votovi = Counter(lst)
  if len(list(votovi.keys())) == 1:
    return max(votovi, key=votovi.get)
  values = list(votovi.values())
  return max(votovi, key=votovi.get) if sum(values) / len(values) != values[0] el



################################################################
"""
Solution 4
"""


def majority_vote(lst):
	if len([x for x in lst if (len(lst) / 2) < lst.count(x)]) == 0:
		return None
	return ''.join(set(x for x in lst if (len(lst) / 2) < lst.count(x)))




################################################################
"""
Solution 5
"""


def majority_vote(l):
	if not l: return None 
	p = [l.count(x)/len(l) for x in list(dict.fromkeys(l))]
	return list(dict.fromkeys(l))[p.index(max(p))] if max(p) > .5 else None