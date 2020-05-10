# Given an integer n perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird

# Input Format: A single line containing a positive integer, .
# Constraints: n<=100,  n>=1

#!/bin/python3
__author__ = 'RobertaBtt'

def function(n):
    string_not_weird = "Not Weird"
    string_weird = "Weird"

    if n >100: return
    elif n <1: return
    if n % 2 != 0:
        print(string_weird)
    else:
        if n>20 :
            print(string_not_weird)
        elif n<=20 and n >=6:
            print(string_weird)
        elif n<=5 and n>=2:
            print(string_not_weird)
            if n%2 : print ("Weird")
if __name__ == '__main__':
    n = int(input().strip())
    function(n)