#!/bin/python3
import os
import math

import itertools

# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, budget):
    n = len(keyboards)
    m = len(drives)
    if 1 <= n <=1000 and 1 <= m <=1000 and 1 <= budget <= 1000000:
        c = [x + y for x in keyboards for y in drives]
        iterator_budget = filter(lambda number: number <= budget, c)
        filtered_numbers = list(iterator_budget)
        if len(filtered_numbers) >=1:
            return max(filtered_numbers)
        else:
            return -1

if __name__ == '__main__':

    os.environ['OUTPUT_PATH'] = "/tmp/electronicShop.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))

    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items

    moneySpent = getMoneySpent(keyboards, drives, b)
    fptr.write(str(moneySpent) + '\n')
    fptr.close()
