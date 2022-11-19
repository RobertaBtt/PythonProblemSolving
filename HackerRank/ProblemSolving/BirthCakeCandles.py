#!/bin/python3
__author__ = 'RobertaBtt'

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
# Returns: int: the number of candles that are tallest
def birthdayCakeCandles(candles):
    # Write your code here

    count = 0
    max_number = max(candles)
    for c in candles:
        if str(max_number) == str(c):
            count +=1

    return count

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "/tmp/output.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


