__author__ = 'RobertaBtt'

"""There are N given points on a plane.
The k-th point is located at coordinates X[K], Y[K] and its tag is S[K]
We want to draw a circle centered on coordinates (0,0)
The circle should not contain two points with the same tag.
What is the maximum number of points that can lie inside the circle ?"""

import functools

import math

import math


class CirclePoints:

    def dist(x1, y1, x2, y2):
        return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

    def solution(S,X,Y):
        x0 = 0
        y0 = 0
        distances = {}
        for k,x in enumerate(X):
            for j,y in enumerate(Y):
                distance = CirclePoints.dist(x,y,x0,y0)
                if S[j] in distances:
                    if distance < distances[S[j]]:
                        distances[S[j]] = distance
                else:
                    distances[S[j]] = distance
        print(distances)

print(CirclePoints.solution(['A','B','D','C','A'], [2,-1,-4, -3, 3], [2,-2,4,1,-3]))