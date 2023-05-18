#!/bin/python3
#Given two strings, determine if they share a common substring. A  substringmay be as small as one character.


import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)

    if len_s2 > len_s1:
        for char_s2 in s2:
            if char_s2 in s1:
                return 'YES'
    elif len_s1 >= len_s2:
        for char_s1 in s1:
            if char_s1 in s2:
                return 'YES'
    return 'NO'
    #
    # s1 = set(s1)
    # s2 = set(s2)
    # if s1.intersection(s2):
    #     return 'YES'
    # else:
    #     return 'NO'

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "/tmp/tmp.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)
        print(result)
        fptr.write(result + '\n')

    fptr.close()
