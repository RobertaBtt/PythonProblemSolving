#!/bin/python3

import os

def findNumber(A, n):
    if len(A) == n and 2 <= n<=10:
        arr = sorted(A)
        for i in reversed(arr):
            if i!= max(arr):
               return i

def findNumberSimple(A,n):


    result = 1 in A
    return result
if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().rstrip().split()))


    findNumberSimple([1, 2, 3, 4, 5],1)
    print(findNumber(arr, n))



