  
c = 20
x = 10
y = 5
try:
    print(c / 0)
except ZeroDivisionError:
    print(0)

try:
    z = x / y
except ZeroDivisionError:
    z = 0