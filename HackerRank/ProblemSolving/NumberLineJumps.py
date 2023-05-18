# You have to figure out a way to get both kangaroos at the same
# location at the same time as part of the show.
# If it is possible, return YES, otherwise return NO.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
# Sample input : 0 3 4 2

"""x1 = starting location of animal 1
v2 = speed of the animal 1
x2 = starting location of animal 2
v3 = speed of the animal 2"""


def kangaroo(x1, v1, x2, v2):
    if v1 > v2 and ((x2 - x1) % (v1 - v2)) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':

    os.environ['OUTPUT_PATH'] = "/tmp/jump.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
