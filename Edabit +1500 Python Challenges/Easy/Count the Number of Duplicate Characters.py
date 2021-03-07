"""
Count the Number of Duplicate Characters

Create a function that takes a string and returns the number of alphanumeric characters that occur more than once.

Examples
duplicate_count("abcde") ➞ 0

duplicate_count("aabbcde") ➞ 2

duplicate_count("Indivisibilities") ➞ 2

duplicate_count("Aa") ➞ 0
# Case sensitive

Notes
Duplicate characters are case sensitive.
The input string will contain only alphanumeric characters.
"""




################################################################
"""
Solution 1
"""

def duplicate_count(txt):
	return sum([1 for x in set(txt) if txt.count(x) > 1])




################################################################
"""
Solution 2
"""

def duplicate_count(txt):
  count = {}
  for char in txt:
    count[char] = count.get(char, 0) + 1
  return len([char for char, num in count.items() if num > 1])







################################################################
"""
Solution 3
"""

def duplicate_count(txt):
  dicty=dict()
  counter=0
  for i in txt:
    dicty[i]=dicty.get(i, 0)+1
  for key,val in dicty.items():
    if val>=2:
      counter+=1
  return counter






#################################################################
"""
Solution 4
"""


duplicate_count=lambda t:sum(t.count(x)>1for x in set(t))




#################################################################
"""
Solution 5
"""




import collections

def duplicate_count(txt):
  count = 0
  
  d = collections.defaultdict(int)
  for char in txt:
    d[char] += 1
    
  return(len([i for i in d.values() if i>1]))