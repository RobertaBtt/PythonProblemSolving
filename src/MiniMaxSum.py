#!/bin/python3
__author__ = 'RobertaBtt'

# Complete the miniMaxSum function below.
def miniMaxSum(arr):

    arr.sort()
    total = sum(arr)
    min_sum = total - arr[len(arr)-1]
    max_sum = total - arr[0]

    return str(min_sum) + " " +str(max_sum)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    print(miniMaxSum(arr))
