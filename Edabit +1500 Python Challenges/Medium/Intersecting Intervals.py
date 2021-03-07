"""
Intersecting Intervals

Create a function that takes in a list of intervals and returns how many intervals overlap with a given point.

An interval overlaps a particular point if the point exists inside the interval, or on the interval's boundary. For example the point 3 overlaps with the interval [2, 4] (it is inside) and [2, 3] (it is on the boundary).

To illustrate:

count_overlapping([[1, 2], [2, 3], [1, 3], [4, 5], [0, 1]], 2) ➞ 3
# Since [1, 2], [2, 3] and [1, 3] all overlap with point 2
Examples
count_overlapping([[1, 2], [2, 3], [3, 4]], 5) ➞ 0

count_overlapping([[1, 2], [5, 6], [5, 7]], 5) ➞ 2

count_overlapping([[1, 2], [5, 8], [6, 9]], 7) ➞ 2

Notes
Each interval is represented as a list with a start point and an endpoint.
Intervals count as intersecting even if they only intersect at one point, i.e. [2, 3] and [3, 4] both intersect at point 3.
If it's helpful, you can draw these intervals on a line on a piece of paper.
"""




################################################################
"""
Solution 1
"""


def count_overlapping(intervals, point):
	return sum(min(x)<=point<=max(x) for x in intervals)



################################################################
"""
Solution 2
"""


def count_overlapping(intervals, point):
	count=0
	for x in intervals:
		if point>= x[0] and point<=x[1]:
			count+=1
	return count

    


################################################################
"""
Solution 3
"""


def count_overlapping(intervals, point):
	firNum = [a[0] for a in intervals]
	secNum = [b[1] for b in intervals]
	cnt = 0
	sumVal = 0
	while cnt < len(intervals):
		if point in range(firNum[cnt],(secNum[cnt] + 1)):
			sumVal += 1
			cnt += 1
		else:
			cnt += 1
	return(sumVal)





#################################################################
"""
Solution 4
"""


def count_overlapping(intervals, point):
    overlaps = [1 for interval in intervals
                if point >= interval[0] and point <= interval[1]]
    return len(overlaps)



