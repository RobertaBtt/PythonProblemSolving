__author__ = 'RobertaBtt'

import functools

import math

#O(N + M)
# https://app.codility.com/demo/results/trainingB5JAHK-966/
def create_counter(max_number, dimension):
    return [max_number] * dimension

def solution(N,A):
    max = 0
    counter = create_counter(max, N)

    for k, value in enumerate(A):
        if value == N+1:
            counter = create_counter(max, N)
        elif 1<= value <= N:
            counter[value -1] +=1
            if counter[value-1] > max:
                max = counter[value-1]

    return counter





print(solution(5, [3,4,4,6,1,4,4]))
