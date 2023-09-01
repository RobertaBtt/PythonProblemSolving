__author__ = 'RobertaBtt'

"""A small frog wants to get to the other side of a river. 
The frog is initially located on one bank of the river (position 0) and wants to get to 
the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. 
A[K] represents the position where one leaf falls at time K, measured in seconds.

he goal is to find the earliest time when the frog can jump to the other side of the river. 
The frog can cross only when leaves appear at every position across the river from 1 to X 
(that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves).

Find the earliest time when leaves appear in every position across the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

"""

"""Here the is the concept of counter array
https://codility.com/media/train/2-CountingElements.pdf

"""

# 100% result on codility test https://app.codility.com/demo/results/trainingG34PNZ-ER2/
class FrogRiver:

    def solution(X, A):
        n = 0
        sum_leaves = 0
        len_a = len(A)
        dictionary = {}

        while n < len_a:
            if A[n] not in dictionary:
                sum_leaves += 1
            if sum_leaves == X:
                return n
            dictionary[A[n]] = 1  # It must be at least one leaf.
            # I don't care to sum up the leaves. I need just one leaf in that position
            n += 1
        return -1


print(FrogRiver.solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
print(FrogRiver.solution(1, [1]))  # must return 0
print(FrogRiver.solution(5, [3]))
