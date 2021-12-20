#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    count =0
    sum=0
    li=[]
    for i in path:
        if i == "U":
            li.append(1)
        elif i == "D" :
            li.append(-1)
    for i in range(steps-1):
        sum = sum + li[i]
        if sum < 0 and   (sum + li[i+1]==0) :
            count += 1
    return count
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
