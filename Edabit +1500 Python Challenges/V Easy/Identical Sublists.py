"""
Identical Sublists

Create a function that takes in a two-dimensional list and returns the number of sub-lists with identical elements.

Examples
count_identical([
  [1],
  [2],
  [3],
  [4]
]) ➞ 4

# Single-item lists still count as having identical elements.

count_identical([
  [1, 2],
  [2, 3],
  [3, 4],
  [4, 4]
]) ➞ 1

count_identical([
  [33, 33],
  [5],
  ["a", "a"],
  [2, 2, 2],
  [1, 2, 2],
  [3, 1]
]) ➞ 4

# 4 lists with identical elements: [33, 33], [5], ["a", "a"], and [2, 2, 2]

count_identical([
  ["@", "@", "@", "@"],
  [2, 3], [3, 4], [4, 4]
]) ➞ 2
Notes
Single-element lists count as (trivially) having identical elements.

"""




"""
Solution 1
"""

def count_identical(lst):
	return len([c for c in lst if len(set(c))==1])

"""
Solution 2
"""

def count_identical(lst):
	filtered_lst = list(filter(lambda x: len(set(x)) == 1, lst))
	return len(filtered_lst)

"""
Solution 3
"""

def count_identical(lst):
	count=0
	for i in lst:
		if len(set(i))==1: count+=1
	return count

"""
Solution 4
"""

def count_identical(lst):
	a=0
	for i in range(len(lst)):
		if len(lst[i])==1 or lst[i].count(lst[i][0])==len(lst[i]):
			a+=1
	return a


"""
Solution 5
"""
def count_identical(lst):
        count = 0
        for l in lst:
                if (all(x==l[0] for x in l)):
                        count += 1
        return count
