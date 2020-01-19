#!/bin/python3
__author__ = 'RobertaBtt'

import os
from time import strptime
#
# Complete the timeConversion function below.
#
def timeConversion(s):
    print(s)
    strptime(s, '%Y-%m-%d')
    return s



if __name__ == '__main__':

    os.environ['OUTPUT_PATH'] = "/home/time.txt"
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
