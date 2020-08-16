""" 
---------------------------------------------------------
Exercise 4 : 
---------------------------------------------------------
Create a program that asks the user for a number and then
prints out a list of all the divisors of that number.
eg: 13 is a divisor of 26 because 26/13 has no remainder.
---------------------------------------------------------
Concepts : 
---------------------------------------------------------
1. range() : eg: x = range(2, 11) will create a list of 
  numbers from 2 to 10.
----------------------------------------------------------
 """

divident = int(input(f"Give me any number of your choice? : "))

divisors = range(1, divident+1)

divisor_list = []

for divisor in divisors:
    if divident % divisor == 0:
        divisor_list.append(divisor)

print(divisor_list)