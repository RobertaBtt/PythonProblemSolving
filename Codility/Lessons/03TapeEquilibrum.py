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

        # x is the accumulated part, in the left side
        # array_sum -x is the is the right part of the sum
        # the difference between the two is:
        # y=array_sum-x;
        # abs(y-x)

        return min([abs(array_sum-x-x) for x in accumulated_list])

print(TapeEquilibrum.solutionC([3,1,2,4,3]))
print(TapeEquilibrum.solution([3,1,2,4,3]))
print(TapeEquilibrum.solution([5,4,3,2,3,23,3,2,3,4,3,2,11]))

