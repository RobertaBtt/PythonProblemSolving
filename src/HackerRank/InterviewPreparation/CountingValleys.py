#!/bin/python3
import os
import math

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
def countingValleys(steps, path):
    if 2<= steps <= 1000000:
        sum = 0
        started = False
        totalValleys = 0


        for element in path:
            if sum == 0:
                if started:
                    started = False
                    totalValleys += 1
                    if element == 'D':
                        started = True
                        sum -= 1
                    else:
                        sum += 1
                else:
                    if element == 'D':
                        started = True
                        sum -= 1
                    else:
                        sum += 1
            else:
                if element == 'D':
                    sum -= 1
                else:
                    sum += 1
        # To count the last element befor exiting from the for
        if (sum == 0 and started):
            totalValleys +=1
        return totalValleys

if __name__ == '__main__':

    os.environ['OUTPUT_PATH'] = "/tmp/countingValleys.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')
    fptr.close()
