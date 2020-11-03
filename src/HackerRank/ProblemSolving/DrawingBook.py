#!/bin/python3
import os
import math

def pageCount(n, p):
    if 1 <= n <= 100000 and 1<= p <=n:

        half = n // 2
        if p <= half:
            return p//2
        else:
            if (n % 2) == 0 and (n-p) ==1:
                return 1
            else:
                return math.ceil((n-p)//2)

if __name__ == '__main__':

    os.environ['OUTPUT_PATH'] = "/tmp/pageCount.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #This is a book    # n = number of the pages    # p = number to reach

    n, p = int(input()), int(input())
    result = pageCount(n, p)
    fptr.write(str(result) + '\n')
    fptr.close()

# Input Test n.1 / Output = 1
# 6
# 2

# Input Test n.26 / Ouput = 1
# 6
# 5

# Input Test n2 / Output = 0
#5
#4