#!/bin/python3
import copy
import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr


def rotateLeft(n_rotations, array_to_rotate):

    if 1 <= n_rotations <= 100000:

        new_array = copy.deepcopy(array_to_rotate)
        for i in range(len(array_to_rotate)):
            new_index = i - n_rotations
            if new_index >=0 :
                new_array[new_index] = array_to_rotate[i]
            else:
                new_array[new_index + len(array_to_rotate)] = array_to_rotate[i]

    return new_array

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "/tmp/rotateLeft.txt"

    line_input = input().rstrip().split()

    array_size = int(line_input[0])
    n_rotations = int(line_input[1])

    array_to_rotate = list(map(int, input().rstrip().split()))

    if len(array_to_rotate) == array_size:
        if n_rotations == array_size:
            result = array_to_rotate
        else:
            # Avoid to run in circle. One rotation is enough,
            # the other rotations, if is a multiply of the base number, obtain the same effects.
            module = n_rotations % array_size
            if module == 0:
                result = array_to_rotate
            else:
                n_rotations = module
                result = rotateLeft(n_rotations, array_to_rotate)

        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

        fptr.close()


