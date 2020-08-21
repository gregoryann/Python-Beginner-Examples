def mango(quantity, price):
    return (quantity - quantity // 3) * price

'''
before refactoring
def mango(quantity, price):
    if quantity % 3 == 0:
        return ((quantity/3)*2)*price
    else :
        remainder = quantity % 3
        return (((quantity/3)*2) + remainder) * price
'''

print(mango(4,1))

'''
Description:

There's a 3 for 2 offer on mangoes. For a given price and quantity, calculate the total cost of the mangoes.
'''