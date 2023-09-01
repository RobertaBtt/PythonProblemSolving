__author__ = 'RobertaBtt'

import math

"""A small frog wants to get to the other side of the road. 
The frog is currently located at position X and wants to get to a position greater than or equal to Y. 
The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

def solution(X, Y, D)

that, given three integers X, Y and D, 
returns the minimal number of jumps from position X to a position equal to or greater than Y."""


class FrogJmp:

    def __init__(self):
        pass

    @staticmethod
    def solution(X, Y, D):

        # I simply count how many times the number D
        # is inside the interval Y-X
        return math.ceil((Y-X) / D)


print(FrogJmp.solution(2,16,4))

print(FrogJmp.solution(10,85,30))

