import math
import os
import random
import re
import sys

# Complete the primality function below.

# One of the first methods to generate the prime numbers was found by
# Eratostene di Cirene (273-194 a.C)
# Il crivello di Eratostene
# To find all the prime numbers <= n is enought to do a sieve (crivello)
# for the prime numbers <= √n


def primality(number_list):

    #n = max(numbers_list)
    dict = {}
    i = 2
    while (i*i <= n):
        if (n % i == 0):
            return "Not prime"
        i += 1
    return "Prime"


    # Mersenne_number_list = [2,3,5,7,13,17,19,31,61,89,107,127]
    # len_n = len(number_list)
    # sorted = sorted(number_list)
    #
    # for number in range (0,len_n):
    #
    #     print(number, end="\n")
    # return "ok"
if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "/tmp/Primality.txt"

    p = int(input())
    if 1<= p <= 30:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        for p_itr in range(p):
            n = int(input())
            if n == 1:
                result = "Not prime"
            elif 1 < n <= 2 * 1000000000:

                result = primality(n)
            print(result)
            fptr.write(result + '\n')

        fptr.close()
