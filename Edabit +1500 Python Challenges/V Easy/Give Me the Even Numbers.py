"""
Give Me the Even Numbers
Create a function that takes two parameters (start, stop), and returns the sum of all even numbers in the range.

Examples
sum_even_nums_in_range(10, 20) ➞ 90
# 10, 12, 14, 16, 18, 20

sum_even_nums_in_range(51, 150) ➞ 5050

sum_even_nums_in_range(63, 97) ➞ 1360
Notes
Remember that the start and stop values are inclusive.

"""



"""
Solution 1
"""

def sum_even_nums_in_range(start, stop):
    return sum(i for i in range(start, stop+1) if not i%2)

"""
Solution 2
"""

def sum_even_nums_in_range(start, stop):
    zbior = []
    for x in range(start,stop+1):
        if x % 2 == 0:
            zbior.append(x)
    suma= sum(zbior)
    return suma

"""
Solution 3
"""

def sum_even_nums_in_range(start, stop):
  return sum([i for i in range(start, stop + 1) if i % 2 == 0])

