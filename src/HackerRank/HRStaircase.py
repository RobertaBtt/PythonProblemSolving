#!/bin/python3
__author__ = 'RobertaBtt'


# Complete the staircase function below.
def staircase(n):
    if 100 >= n > 0:
        for index in range(n):
            for index2 in range(n):
                if index2 < (n - (index + 1)):
                    print(" ", end='')
                else:
                    print("#", end='')
            print("")


if __name__ == '__main__':
    n = int(input())

    staircase(n)
