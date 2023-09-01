__author__ = 'RobertaBtt'

"""A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

Write a function:

    def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.


"""


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

        # Sum of all the elements
        array_sum = sum(A)

        # progressive sum of the elements to the left (excluding the last one)
        accumulated_list = accumulate(A[:-1])

        # for every element in the accumulated list,
        # I subtract the total array_sum to the element in the left,
        # and I obtain what remains (right total)
        # y=array_sum-x;

        # the difference between the two is:
        #
        # abs(y-x)

        return min([abs(array_sum-x-x) for x in accumulated_list])

print(TapeEquilibrum.solutionC([3,1,2,4,3]))
print(TapeEquilibrum.solution([3,1,2,4,3]))
print(TapeEquilibrum.solution([5,4,3,2,3,23,3,2,3,4,3,2,11]))

