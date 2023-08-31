#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    pre_fix = [0 for _ in range(n+1)]
    
    for query in queries:
        a,b,k = query
        pre_fix[a-1] += k
        pre_fix[b] -= k
      
    max_ans = pre_fix[0]
    ans = max_ans
    for i in range(1,n):
        ans += pre_fix[i]
        max_ans = max(max_ans,ans)
        


    return max_ans
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
