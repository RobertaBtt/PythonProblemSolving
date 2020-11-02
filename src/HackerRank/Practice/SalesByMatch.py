#!/bin/python3

import os
from functools import reduce

# Complete the sockMerchant function below.
# Input n = Number of sokcs
# ar = n space-separated array of socks

def my_add(a, b):
    return a + b

# Return the total number of matching pairs of socks that John can sell.
def sockMerchant(n, ar):
    if 1 <= n <= 100 and len(ar) == n:

        new_map = {}
        for i in ar:
            # Constraint a[i] <n and a[1] >=1
            if i>=1 and i<=100:
                if i in new_map:
                    new_map.update({i:new_map[i]+1})
                else:
                    new_map.update({i: 1})

        lista = list(map(lambda x: x // 2, new_map.values()))
        result = reduce(my_add, lista)

    return result

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "/tmp/merchantStock.txt"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Constraint: n>=1, n<=100
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()


