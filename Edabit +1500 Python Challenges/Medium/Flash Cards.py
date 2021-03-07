"""
Flash Cards

Create a function that outputs the results of a flashcard. A flashcard is a list of three elements: a number, an operator symbol, and another number. Return the mathematical result of that expression.

There are 4 operators: + (addition), - (subtraction), x (multiplication), and / (division). If the flashcard displays a number being divided by zero, e.g. [3, "/", 0], then return None. For division, round to the hundredths place. So [10, "/", 3] should return 3.33.

Examples
flash([3, "x", 7]) ➞ 21

flash([5, "+", 7]) ➞ 12

flash([10, "-", 9]) ➞ 1

flash([10, "/", 0]) ➞ None

flash([10, "/", 3]) ➞ 3.33

Notes
Flash cards contain only zero or positive numbers.
"""


################################################################
"""
Solution 1
"""


def flash(flashcard):
	card =  (' '.join([str(i) for i in flashcard]))
	card = card.replace('x', '*')
	if '/ 0' in card:
		return None
	return round(eval(card), 2)



################################################################
"""
Solution 2
"""


def flash(flashcard): 
	if flashcard[1] == "/":
		try:
			return round(flashcard[0] / flashcard[2],2)
		except ZeroDivisionError:
			return None
	elif flashcard[1] == "x":
		return flashcard[0] * flashcard[2]
	else:
		return eval(''.join(list(map(lambda x: str(x),flashcard))))



################################################################
"""
Solution 3
"""


def flash(flashcard):
    try:
        return round(eval( str(flashcard[0])+ flashcard[1].replace('x', '*') +str(flashcard[2]) ), 2)
    except ZeroDivisionError:
        return None



#################################################################
"""
Solution 4
"""


def flash(flashcard):
	try:
		r=eval((str(flashcard[0])+flashcard[1]+str(flashcard[2])).replace('x','*'))
		if flashcard[1]=='/': r=round(r,2)
		return r	
	except: return None





