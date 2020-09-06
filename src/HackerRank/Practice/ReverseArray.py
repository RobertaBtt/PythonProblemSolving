#!/bin/python3

import os


# Complete the reverseArray function below.
def reverseArray(a):
    a.reverse()

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "/tmp/reverse.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    if arr_count == len(arr):
        reverseArray(arr)

        fptr.write(' '.join(map(str, arr)))
        fptr.write('\n')

        fptr.close()
