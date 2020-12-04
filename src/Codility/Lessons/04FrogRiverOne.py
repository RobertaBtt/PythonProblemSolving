__author__ = 'RobertaBtt'

# 100% result on codility test https://app.codility.com/demo/results/trainingG34PNZ-ER2/
class FrogRiver:

    def solution(X, A):
        n=0
        sum = 0
        len_A = len(A)
        dictionary = {}
        while n < len_A:
            if A[n] not in dictionary:
                sum += 1
            if sum == X:
                return n
            dictionary[A[n]] = 1 #It must be at least one leaf.
            # I don't care to sum up the leaves. I need just one leaf in that position
            n += 1
        return -1


print(FrogRiver.solution(5,[1,3,1,4,2,3,5,4]))
print(FrogRiver.solution(1, [1])) #must return 0
print(FrogRiver.solution(5, [3]))