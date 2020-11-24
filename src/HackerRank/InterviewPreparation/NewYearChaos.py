#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    count = 0

    for key,value in enumerate(q, start=1):
        if key != value:
            if value - key >2:
                print("Too chaotic")
                return

                count += 1
        


    print(count)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
