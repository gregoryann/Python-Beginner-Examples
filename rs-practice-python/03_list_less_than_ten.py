""" 
---------------------------------------------------------
Exercise 3 : 
---------------------------------------------------------
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of 
the list that are less than 5.
---------------------------------------------------------
Concepts : 
---------------------------------------------------------
1. List --> [] (for x in xs)
2. Conditionals --> if/else/while/elif
----------------------------------------------------------
 """

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for elements in a:
    if(elements < 5):
        print(elements)

""" 
-------------------------------------------------------------
Extras :
-------------------------------------------------------------
1. Instead of printing the elements one by one, make a new
    list that has all the elements less than 5 from the list
    and print out this new list
2. Write this in one line of Python
-------------------------------------------------------------
 """

b = []

for elements in a:
    if elements < 5:
        b.append(elements)

print(b)

line = ''

for elements in b:
    line = line + " " + str(elements)

print(line)

""" 
-------------------------------------------------------------
1. Ask the user for a number and return a list that contains
  only elements from the original list a that are smaller 
  than that number given by the user.
-------------------------------------------------------------
 """

num = int(input(f"Give me number? : "))

c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for elements in c:
    if elements < num:
        print(elements)