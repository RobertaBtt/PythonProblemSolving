#!/bin/python3

import os

def findNumber(A, n):
    if len(A) == n and 2 <= n<=10:
        arr = sorted(A)
        for i in reversed(arr):
            if i!= max(arr):
               return i

if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    print(findNumber(arr, n))



