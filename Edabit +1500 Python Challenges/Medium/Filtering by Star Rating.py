"""
Filtering by Star Rating


Given a dictionary of some items with star ratings and a specified star rating, return a new dictionary of items which match the specified star rating. Return "No results found" if no item matches the star rating given.

Examples
filter_by_rating({
  "Luxury Chocolates" : "*****",
  "Tasty Chocolates" : "****",
  "Aunty May Chocolates" : "*****",
  "Generic Chocolates" : "***"
}, "*****") ➞ {
  "Luxury Chocolates" : "*****",
  "Aunty May Chocolates" : "*****"
}

filter_by_rating({
  "Continental Hotel" : "****",
  "Big Street Hotel" : "**",
  "Corner Hotel" : "**",
  "Trashviews Hotel" : "*",
  "Hazbins" : "*****"
}, "*") ➞ {
  "Trashviews Hotel" : "*"
}

filter_by_rating({
  "Solo Restaurant" : "***",
  "Finest Dinings" : "*****",
  "Burger Stand" : "***"
}, "****") ➞ "No results found"

"""



################################################################
"""
Solution 1
"""


def filter_by_rating(d, rating):
  return {k:v for k,v in d.items() if d[k]==rating} or 'No results found'




################################################################
"""
Solution 2
"""


def filter_by_rating(d, rating):
	if rating not in d.values(): return 'No results found'
	return {k:v for k,v in d.items() if v==rating}



################################################################
"""
Solution 3
"""


def filter_by_rating(d, rating):
	
	new_d = dict()
	
	for key in d.keys():
		if d[key] == rating:
			new_d[key] = rating
			
	return "No results found" if not len(new_d) else new_d



#################################################################
"""
Solution 4
"""


def filter_by_rating(d, rating):
	rate = {}
	if rating not in d.values():
		return 'No results found'
	else:
		for i in d:
			if d[i] == rating:
				rate.update({i:d[i]})
		return rate




