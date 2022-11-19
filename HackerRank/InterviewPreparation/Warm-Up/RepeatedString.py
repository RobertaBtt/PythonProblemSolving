import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    count = 0
    len_s = len(s)

    for letter in range(0, len(s)):
        if s[letter] =='a':
            count +=1

    # Divido la stringa in parti uguali, tante quante sono le lettere
    # che compongono la stringa iniziale len(s)
    divided = n//len_s

    count *= divided

    len_s * divided

    remain = n % len(s)
    if remain ==0:
        return count
    else:
        for i in range (0,remain):
            if s[i] == 'a':
                count += 1


    print(count)
    return count

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "/tmp/repeatedStrings.txt"

    s = input()

    n = int(input())
    if 1<= n <= 1000000000000:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        result = repeatedString(s, n)

        fptr.write(str(result) + '\n')

        fptr.close()