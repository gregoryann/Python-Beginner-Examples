def positive_sum(arr):
    return sum(x for x in arr if x > 0)


print(positive_sum([1,2,3,-4,5]))

'''
Description:

You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: array may be empty, in this case return 0.
'''
