__author__ = 'RobertaBtt'

import math


class FrogJmp:

    def __init__(self):
        pass

    @staticmethod
    def solution(X, Y, D):

        return math.ceil((Y-X) / D)


print(FrogJmp.solution(10,85,30))

