#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_dictionary = dict((k, 2) for k in magazine)
    for n in note:
        if n not in magazine_dictionary:
            return "No"
        magazine_dictionary.pop(n)
    return "Yes"

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])
    if 1<= n <= 30000 and 1 <= m <= 30000:
        magazine = input().rstrip().split()

        note = input().rstrip().split()

        print(checkMagazine(magazine, note))