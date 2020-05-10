#!/bin/python3

import math
import os
import random
import re
import sys


# write your code here
def avg_function(*args):
    if len(args)==1:
        return args[0]
    total = sum(i for i in args)
    return total/len(args)

if __name__ == '__main__':
    print(avg_function( 2, 4, 5, 6, 9))