""" 
---------------------------------------------------------
Exercise 5 : 
---------------------------------------------------------
Take two lists, and write a program that returns a list
that contains only the elements that are common between
the list (without duplicate). Make sure your program 
works on two lists of different sizes.
---------------------------------------------------------
Concepts : 
---------------------------------------------------------
1. List properties --> eg: >> a = [1, 2, 3, 4]
  >> 10 in a --> False >> 3 in a --> True
----------------------------------------------------------
 """

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = []

for a_element in a:
    # print(a_element)
    if a_element in b:
        result.append(a_element)


print(set(result))