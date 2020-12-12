"""
Return the Objects Keys and Values

Create a function that takes a dictionary and returns the keys and values as separate lists. Return the keys sorted alphabetically, and their corresponding values in the same order.

Examples
keys_and_values({ "a": 1, "b": 2, "c": 3 })
➞ [["a", "b", "c"], [1, 2, 3]]

keys_and_values({ "a": "Apple", "b": "Microsoft", "c": "Google" })
➞ [["a", "b", "c"], ["Apple", "Microsoft", "Google"]]

keys_and_values({ "key1": True, "key2": False, "key3": True })
➞ [["key1", "key2", "key3"], [True, False, True]]

Notes
Remember to sort the keys.
"""



################################################################
"""
Solution 1
"""


def keys_and_values(d):
  return list(map(list, zip(*sorted(d.items()))))



################################################################
"""
Solution 2
"""


def keys_and_values(d):
	lst = sorted(list(d.keys()))
	return [lst, [d[n] for n in lst]]


################################################################
"""
Solution 3
"""


def keys_and_values(d):
 k = []
 v = []
 for i, j in sorted(d.items()):
  k.append(i)
  v.append(j)
 return [k, v]



#################################################################
"""
Solution 4
"""


from collections import OrderedDict 
def keys_and_values(d):
	d_list = []
	for k, v in d.items():
		d_list.append({"key": k, "val": v})
	newlist = sorted(d_list, key=lambda k: k['key'])
	k_list = [x['key'] for x in newlist]
	v_list = [x['val'] for x in newlist]
	return [k_list, v_list]



