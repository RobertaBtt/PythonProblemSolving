__author__ = 'RobertaBtt'

from itertools import accumulate

class TapeEquilibrum:

    #A is the array of Integers
    def solution(A):

        if 2 <= len(A) <= 100000:
            listDiff = sorted([]) #arr.array("i", [])
            for k in range(1, len(A)):
                if -1000 <= A[k] <= 1000:
                    listDiff.append(abs((sum(A[0:k]) - sum(A[k:len(A)]))))

            return min(listDiff)

    def solutionC(A):

        array_sum = sum(A)
        accumulated_list = accumulate(A[:-1])

        # x + array_sum is the right part of the sum
        # x is the left part of the sum.

        return min([abs((x - array_sum) + x) for x in accumulated_list])

print(TapeEquilibrum.solutionC([3,1,2,4,3]))
print(TapeEquilibrum.solution([3,1,2,4,3]))

