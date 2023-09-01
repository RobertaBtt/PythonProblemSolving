__author__ = 'RobertaBtt'

"""An array A consisting of N integers is given. Rotation of the array means that each element is
 shifted right by one index, and the last element of the array is moved to the first place. For example, 
the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index 
and 6 is moved to the first place)."""

"""The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.
Write a function:

def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.
"""


class CyclicRotation:
    def __init__(self):
        pass

    @staticmethod
    def solution(array_numbers, k):
        # k is the shift
        length = len(array_numbers)
        if length == 0:
            return []
        if k < 0:
            return []

        # Pythonic way to create an array of length of None
        a = [None] * length

        if k > length:
            # If I group the rotations for the number of elements,
            # I avoid to rotate for a useless times.
            k = k % length

        # I am rotating to the start situation,
        # hence I directly return the array
        if k == len(array_numbers):
            return array_numbers

        # no rotation.
        if k == 0:
            return array_numbers

        for element in enumerate(array_numbers):
            current_position = element[0]
            current_number = element[1]

            new_position = current_position + k

            a[new_position - (length - 1) - 1] = current_number
        return a

print(CyclicRotation.solution([5,6,1], 2))

print(CyclicRotation.solution([], 19))
print(CyclicRotation.solution([1, 2, 3, 4], 3))
print(CyclicRotation.solution([1, 2, 3, 4], 0))
