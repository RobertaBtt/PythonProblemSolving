#!/bin/python3
__author__ = 'RobertaBtt'

import collections
import os

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    counter = collections.Counter(ar)
    return counter


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "/home/sock.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
