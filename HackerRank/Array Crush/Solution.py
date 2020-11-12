#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for q in queries:
        a = q[0] - 1
        b = q[1]
        k = q[2]
        arr[a] += k
        arr[b] -= k
    
    biggest = 0
    running_total = 0
    for i in arr:
        running_total += i
        if running_total > biggest:
            biggest = running_total
    return biggest
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
