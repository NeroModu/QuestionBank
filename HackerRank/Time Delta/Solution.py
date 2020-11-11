#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
months = {
    'Jan': 0,
    'Feb': 31,
    'Mar': 59,
    'Apr': 90,
    'May': 120,
    'Jun': 151,
    'Jul': 181,
    'Aug': 212,
    'Sep': 243,
    'Oct': 273,
    'Nov': 304,
    'Dec': 334
}

def parse_timezone(xxxx):
    hours = xxxx[1:3]
    minutes = xxxx[3:]
    sign = -1 if xxxx[0] == '+' else 1
    
    seconds = (int(minutes) * 60) + (int(hours) * 3600)
    return seconds * sign

def time_delta(t1, t2):
    t1 = t1.split()[1:]
    t2 = t2.split()[1:]
    
    # dd mon yyyy hh:mm:ss +xxxx
    # 0   1   2      3       4
    
    t1_Time = [int(i) for i in t1[3].split(':')]
    t2_Time = [int(i) for i in t2[3].split(':')]
    
    # hh mm ss
    # 0  1  2
    
    # Add seconds in seconds, minutes and hours
    t1_Seconds = t1_Time[2] + (t1_Time[1] * 60) + (t1_Time[0] * 3600)
    t2_Seconds = t2_Time[2] + (t2_Time[1] * 60) + (t2_Time[0] * 3600)
    
    # Add seconds in timezone differences
    t1_Seconds += parse_timezone(t1[4])
    t2_Seconds += parse_timezone(t2[4])
    
    # Add seconds in day
    t1_Seconds += int(t1[0]) * 86400
    t2_Seconds += int(t2[0]) * 86400
    
    # Add seconds in month
    t1_Seconds += months[t1[1]] * 86400
    t2_Seconds += months[t1[1]] * 86400
    
    # Add seconds in year
    t1_Seconds += int(t1[2]) * 86400 * 365
    t2_Seconds += int(t2[2]) * 86400 * 365
    
    # Return difference
    return str(abs(t1_Seconds - t2_Seconds))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
