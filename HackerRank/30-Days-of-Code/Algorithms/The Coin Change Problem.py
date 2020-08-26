# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 17:06:22 2020
@author: Ashima
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here
    m = len(c)
    table = [[0 for i in range(m)] for j in range(n+1)] 

    for i in range(m):
        table[0][i] = 1

    for i in range(1, n+1):
        for j in range(0, m):
            if (i - c[j]) >= 0:
                table[i][j] = table[i][j] + table[i-c[j]][j]
            if j >= 1:
                table[i][j] = table[i][j] + (table[i][j-1])

    return table[n][m-1]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
