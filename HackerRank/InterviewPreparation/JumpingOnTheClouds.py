#!/bin/python3

import os


def get_next_start(the_enum):
    return 0

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while (i < n - 1):
        i += (c[i + 2] == 0) + 1
        jumps += 1
    return jumps

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "/tmp/jumpingClouds.txt"

    n = int(input())
    if 2 <= n <= 100 :

        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        c = list(map(int, input().rstrip().split()))
        c.insert(n, 0)
        result = jumpingOnClouds(c)

        fptr.write(str(result) + '\n')

        fptr.close()

# Inputs are:
# 0 0 0 1 0 0
# 0 0 0 0 1 0
