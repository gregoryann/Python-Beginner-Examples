""" 
---------------------------------------------------------
Exercise 1 : 
---------------------------------------------------------
Create a program that asks the user to enter their name 
and their age. Print out a message addressed to them that 
tells them the year that they will turn 100 years old.
---------------------------------------------------------
Concepts : 
---------------------------------------------------------
1. input() --> To get user input in Python 3.
2. int() --> Turn the string into an integer.
3. str() --> Turn integer into strings.
----------------------------------------------------------
 """

import datetime

name = input(f"Give me your name? : ")
age = int(input(f"Now, Give me your age? : "))

current_year = datetime.datetime.now().year

year = ((current_year - age) + 100)

print(f"{name} will be 100 years old in the year {year}")

""" 
-------------------------------------------------------------
Extras :
-------------------------------------------------------------
1. Ask the user for another number and print out that many 
   copies of the previous message.
2. Print out that many copies of the previous message on 
   separate lines.
-------------------------------------------------------------
 """

another_num = int(input(f"Give me any number? : "))

""" while(another_num > 0):
    print(f"{name} will be 100 years old in the year {year}")
    another_num -= 1 """

print(another_num * f"{name} will be 100 years old in the year {year}")
print(another_num * f"{name} will be 100 years old in the year {year}\n")