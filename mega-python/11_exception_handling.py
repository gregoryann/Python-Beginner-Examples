def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return("Zero division is meaningless!")


print(divide(1, 0))
print("End of program")