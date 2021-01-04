#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numberOfTokens' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER expiryLimit
#  2. 2D_INTEGER_ARRAY commands
#

def numberOfTokens(expiryLimit, commands):
    # Write your code here
    return None

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    expiryLimit = int(input().strip())

    commands_rows = int(input().strip())
    commands_columns = int(input().strip())

    commands = []

    for _ in range(commands_rows):
        commands.append(list(map(int, input().rstrip().split())))

    result = numberOfTokens(expiryLimit, commands)

    fptr.write(str(result) + '\n')

    fptr.close()