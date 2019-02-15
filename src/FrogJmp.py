__author__ = 'roby'

import math


class FrogJmp:

    def solution(X, Y, D):

        return math.ceil(((Y-X) / D))


print(FrogJmp.solution(10,85,30))

