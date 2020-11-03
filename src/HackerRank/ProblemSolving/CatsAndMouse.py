#!/bin/python3
import os
import math

import itertools


# Complete the catAndMouse function below.
def catAndMouse(catA, catB, Mouse):

    distanceA_Mouse = abs(catA - Mouse)
    distanceB_Mouse = abs(catB - Mouse)
    if distanceA_Mouse != distanceB_Mouse:
        if distanceA_Mouse > distanceB_Mouse:
            return "Cat B"
        else:
            return "Cat A"
    return "Mouse C"


if __name__ == '__main__':

    os.environ['OUTPUT_PATH'] = "/tmp/catsAndMouse.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())
    if  1<= q <= 100:
        for q_itr in range(q):
            xyz = input().split()
            x = int(xyz[0])
            y = int(xyz[1])
            z = int(xyz[2])
            if 1 <= x <= 100 and 1 <= y <= 100 and 1 <= y <= 100:
                result = catAndMouse(x, y, z)
                fptr.write(result + '\n')
    fptr.close()
