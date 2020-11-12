#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    Fizz = "Fizz"
    Buzz = "Buzz"

    # Write your code here
    for i in range(n):
        i=i+1
        if i % 3 == 0 and i % 5 == 0:
            print(Fizz + Buzz)
        elif i % 3 == 0 and i % 5 != 0:
                print(Fizz)
        elif i % 3 != 0 and i % 5 == 0:
            print(Buzz)
        else: print(i)

if __name__ == '__main__':
    fizzBuzz(15)
