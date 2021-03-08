"""
Calculate the Total Price of Groceries

Create a function that takes a list of dictionaries (groceries) which calculates the total price and returns it as a number. A grocery dictionary has a product, a quantity and a price, for example:

{
  "product": "Milk",
  "quantity": 1,
  "price": 1.50
}
Examples
# 1 bottle of milk:
get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 }
]) ➞ 1.5

# 1 bottle of milk & 1 box of cereals:
get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 },
  { "product": "Cereals", "quantity": 1, "price": 2.50 }
]) ➞ 4

# 3 bottles of milk:
get_total_price([
  { "product": "Milk", "quantity": 3, "price": 1.50 }
]) ➞ 4.5

# Several groceries:
get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 },
  { "product": "Eggs", "quantity": 12, "price": 0.10 },
  { "product": "Bread", "quantity": 2, "price": 1.60 },
  { "product": "Cheese", "quantity": 1, "price": 4.50 }
]) ➞ 10.4

# Some cheap candy:
get_total_price([
  { "product": "Chocolate", "quantity": 1, "price": 0.10 },
  { "product": "Lollipop", "quantity": 1, "price": 0.20 }
]) ➞ 0.3

Notes
There might be a floating point precision problem in here...
"""




################################################################
"""
Solution 1
"""


def get_total_price(groceries):
	return round(sum([i['price'] * i['quantity'] for i in groceries]), 1)




################################################################
"""
Solution 2
"""


def get_total_price(groceries):
  total = sum(x.get('quantity') * x.get('price') for x in groceries)
  return round(total, 1)


################################################################
"""
Solution 3
"""


def get_total_price(groceries): 
    values=[x['price']*x['quantity'] for x in groceries]
    if (sum(values)%1==0):
        return int(sum(values))
    else:
        return round(sum(values),1)



#################################################################
"""
Solution 4
"""


def get_total_price(groceries):
	total = 0
	for i in groceries:
		total += float(i["quantity"] * i["price"])
	return  float("%0.2f"%(total))



