"""
Expensive Orders

Write a function that has two parameters: orders and cost. Return any orders that are greater than the cost.

Examples
expensive_orders({ "a": 3000, "b": 200, "c": 1050 }, 1000)
➞ { "a": 3000, "c": 1050 }

expensive_orders({ "Gucci Fur": 24600, "Teak Dining Table": 3200, "Louis Vutton Bag": 5550, "Dolce Gabana Heels": 4000 }, 20000)
➞ { "Gucci Fur": 24600 }

expensive_orders({ "Deluxe Burger": 35, "Icecream Shake": 4, "Fries": 5 }, 40)
➞ {}
"""




################################################################
"""
Solution 1
"""


def expensive_orders(d, p):
	return {k: v for k, v in d.items() if v > p}



################################################################
"""
Solution 2
"""


def expensive_orders(d, k):
	result = {}
	for key, value in d.items():
		if value > k:
			result[key] = value
	return result




################################################################
"""
Solution 3
"""


expensive_orders = lambda d,l: {k:d[k] for k in d if d[k] > l}






#################################################################
"""
Solution 4
"""


def expensive_orders(d, k):
    orders = {}
    for key, value in d.items():
        if (value > k):
            orders.update({key: value})
    return orders





#################################################################
"""
Solution 5
"""


def expensive_orders(d, k):
 x={}
 for i in d:
  if d[i]>k:
   x.setdefault(i,d[i])
 return x




#################################################################
"""
Solution 6
"""

def expensive_orders(d, k):
    d_test = d.copy()
    for key in d:
        if d[key] < k:
            del d_test[key]
    return d_test

print(expensive_orders({ "a": 3000, "b": 200, "c": 1050 }, 1000))
