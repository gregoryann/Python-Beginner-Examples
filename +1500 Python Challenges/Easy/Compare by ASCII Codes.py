"""
Compare by ASCII Codes

Create a function that compares two words based on the sum of their ASCII codes and returns the word with the smaller ASCII sum.

Examples
ascii_sort(["hey", "man"]) ➞ "man"
# ["h", "e", "y"] ➞ sum([104, 101, 121]) ➞ 326
# ["m", "a", "n"] ➞ sum([109, 97, 110]) ➞ 316

ascii_sort(["majorly", "then"]) ➞ "then"

ascii_sort(["victory", "careless"]) ➞ "victory"

Notes
Both words will have strictly different ASCII sums.
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def ascii_sort(lst):
	return sorted(lst, key=lambda l: sum(map(ord, l)))[0]

"""
Solution 2
"""

def ascii_sort(lst):
	word1 = sum([ord(i) for i in lst[0]])
	word2 = sum([ord(i) for i in lst[1]])
	return lst[0] if word1 < word2 else lst[1]

"""
Solution 3
"""

def ascii_sort(arr):
        wrd1total = 0
        wrd2total = 0
        word1 = list(arr[0])
        word2 = list(arr[1])
        for ltr in word1:
                wrd1total += ord(ltr)
        for ltr in word2:
                wrd2total += ord(ltr)
        if wrd1total < wrd2total:
                return arr[0]
        else:
                return arr[1]

"""
Solution 4
"""

ascii_sort=lambda l:min(l,key=lambda x:sum(map(ord,x)))




