""" 
---------------------------------------------------------
Exercise 2 : 
---------------------------------------------------------
Ask the user for a number. Depending on wheteher the 
number is even or odd, print out an appopriate message 
to the user.
---------------------------------------------------------
Concepts : 
---------------------------------------------------------
1. Modular Operator --> %
2. Conditionals --> if/else/while/elif
3. Equality --> ==/!==/===/!=
----------------------------------------------------------
 """

num = int(input(f"Enter any number of your choice? : "))

if num % 2 == 0:
    print(f"{num} is a even number.")
else:
    print(f"{num} is a odd number.")


""" 
-------------------------------------------------------------
Extras :
-------------------------------------------------------------
1. If the number is a multiple of 4, print out a different
    message
2. Ask the user for two numbers : one number to check and one
    number to divided by. If check divides evenly, tell that 
    to the user. If not, print a different appropriate message
-------------------------------------------------------------
 """

if num % 4 == 0:
    print(f"{num} is a even number and divisible by 4")
elif num % 2 == 0:
    print(f"{num} is even number and divisible by 2")
else:
    print(f"{num} is a odd number")


check = int(input(f"Enter a number of choice to CHECK? : \n"))
num_to_divide = int(input(f"Enter a number to divide by? : \n"))

if num_to_divide % check == 0:
    print(f"{check} divides {num_to_divide} evenly.")
else:
    print(f"{check} divides {num_to_divide} unevenly.")