"""Changing letters
https://www.codewars.com/kata/changing-letters

When provided with a String, capitalize all vowels

For example:

Input : "Hello World!"

Output : "HEllO WOrld!"
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################



def swap(string_):
    return string_.translate(str.maketrans('aeiou', 'AEIOU'))
