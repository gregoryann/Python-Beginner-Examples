"""
Good Match?

In this challenge you will be given a list of numbers. Your task is to "marry" each pair of adjacent numbers by adding them, and return the list of "couples" (i.e. sums).

If the list has an odd length, one number is (sadly) left out, so you should return "bad match".

Examples
is_good_match([1, 2, 4, 7]) ➞ [1+2, 4+7] ➞ [3, 11]

is_good_match([5, 7, 9, -1, 4, 2]) ➞ [12, 8, 6]

is_good_match([5, 7, 9, -1, 4, 2, 3]) ➞ "bad match"

is_good_match([2, 6, 7, -2, 4]) ➞ "bad match"
"""





################################################################
"""
Solution 1
"""

def is_good_match(lst):
    if len(lst)%2:
        return 'bad match'
    return [sum(lst[i:i+2]) for i in range(0, len(lst), 2)]




################################################################
"""
Solution 2
"""




################################################################
"""
Solution 3
"""




#################################################################
"""
Solution 4
"""






