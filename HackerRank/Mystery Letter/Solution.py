#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'mystery' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY letter as parameter.
#

def mystery(letter):
    # Write your code here
    conversions = []
    for word in letter:
        total = 0
        if len(word) == 1:
            conversions.append(0)
            continue
        
        start = 0
        end = len(word) - 1
        
        while start < end:
            startChar = ord(word[start])
            endChar = ord(word[end])
            difference = abs(startChar - endChar)
            total += difference
            start += 1
            end -= 1
                    
        
        conversions.append(total)
    return conversions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    letter_count = int(input().strip())

    letter = []

    for _ in range(letter_count):
        letter_item = input()
        letter.append(letter_item)

    result = mystery(letter)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
