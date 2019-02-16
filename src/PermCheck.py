__author__ = 'roby'

import functools

import math

class PermCheck:
    def solution(A):
        
        fact_list = functools.reduce(lambda x, y: x * y, A)
        if math.factorial(len(A)) == fact_list:
            return 1
        return 0


print(PermCheck.solution([1,2,3]))