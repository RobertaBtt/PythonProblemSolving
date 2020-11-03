#!/bin/python3
__author__ = 'RobertaBtt'

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar_count, ar):

    max_number = max(ar_count)
    print(max_number)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar_count, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

