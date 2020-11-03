#!/bin/python3
__author__ = 'RobertaBtt'

from decimal import *

# Complete the plusMinus function below.
def plusMinus(n, arr):
    if n > 0 and len(arr) > 0:
        getcontext().prec = 6
        count_positives = 0
        count_negatives = 0
        count_zeros = 0

        fraction_positives = Decimal(0)
        fraction_negatives = Decimal(0)
        fraction_zeros = Decimal(0)

        for integer in arr:
            if integer > 0:
                count_positives += 1
                fraction_positives = Decimal(count_positives) / Decimal(n)
            elif integer < 0:
                count_negatives += 1
                fraction_negatives = Decimal(count_negatives) / Decimal(n)
            else:
                count_zeros += 1
                fraction_zeros = Decimal(count_zeros) / Decimal(n)
        return "" + fraction_positives.to_eng_string() + "\n" + fraction_negatives.to_eng_string() + "\n" + fraction_zeros.to_eng_string()


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(plusMinus(n, arr))
