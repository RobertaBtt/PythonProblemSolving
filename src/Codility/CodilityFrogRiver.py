__author__ = 'RobertaBtt'

class FrogRiver:

    def solution(X,A):
        size = len(A)
        for i in range(size):
            if A[i] < X:
                print("Ancora no" + str(i))
        print(set(A))
        min = X
        return min

print(FrogRiver.solution(5,[1,3,1,4,2,3,5,4]))
