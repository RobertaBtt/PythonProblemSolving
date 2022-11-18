__author__ = 'RobertaBtt'


class CyclicRotation:
    def __init__(self):
        pass

    @staticmethod
    def solution(n, k):
        # k is the shift
        length = len(n)
        if length == 0:
            return []
        if k < 0:
            return []

        a = [None] * length

        if k > length:
            k = k % length
        if k == len(n):
            return n
        if k == 0:
            return n

        for element in enumerate(n):
            result = element[0] + k
            if result <= (length - 1):
                a[result] = element[1]
            a[result - (length - 1) - 1] = element[1]
        return a


print(CyclicRotation.solution([], 19))
print(CyclicRotation.solution([1, 2, 3, 4], 1))
print(CyclicRotation.solution([1, 2, 3, 4], 0))
