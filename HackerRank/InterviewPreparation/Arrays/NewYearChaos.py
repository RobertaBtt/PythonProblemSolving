#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#The first line contains an integer , the number of test cases.

# Each of the next  pairs of lines are as follows:
# - The first line contains an integer , the number of people in the queue
# - The second line has  space-separated integers describing the final state of the queue.


def minimum_bribes(q):
    max_movements = 2
    total_sum = 0
    for index, value in enumerate(q):

        correct_position = value -1
        actual_difference = correct_position - index

        if actual_difference > 0:
            if actual_difference > max_movements:
                return("Too chaotic")
            total_sum += actual_difference
    return total_sum


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        print(minimum_bribes(q))
