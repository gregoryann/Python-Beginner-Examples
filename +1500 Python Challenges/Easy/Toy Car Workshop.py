"""
Toy Car Workshop

You work in a toy car workshop, and your job is to build toy cars from a collection of parts. Each toy car needs 4 wheels, 1 car body, and 2 figures of people to be placed inside. Given the total number of wheels, car bodies and figures available, how many complete toy cars can you make?

Examples
cars(2, 48, 76) ➞ 0
# 2 wheels, 48 car bodies, 76 figures

cars(43, 15, 87) ➞ 10

cars(88, 37, 17) ➞ 8

"""




#############################################################
#                        MY SOLUTIONS                       #
#############################################################





"""
Solution 1
"""

def cars(wheels, bodies, figures):
	return min(wheels // 4, bodies, figures // 2)

"""
Solution 2
"""

cars = lambda a,b,c:min(a//4, b, c//2)

"""
Solution 3
"""

def cars(wheels, bodies, figures):
	w = wheels // 4
	f = figures //2
	
	return min(bodies,w,f)

"""
Solution 4
"""

def cars(wheels, bodies, figures):
    totalcars = 0
    check = True
    while check:
        if wheels >= 4 and bodies >= 1 and figures >= 2:
            wheels -= 4
            bodies -= 1
            figures -= 2
            totalcars += 1
        else:
            check = False
    return totalcars




