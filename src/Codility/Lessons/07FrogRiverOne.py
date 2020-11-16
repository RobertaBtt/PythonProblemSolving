__author__ = 'RobertaBtt'

class FrogRiver:

    def get_counter(A, m):
        n = len(A)
        counter = [0] * (m + 1) #Creates array of m+1 elements, that is the same as n
        for k in range(n):
            counter[A[k]] += 1  # This is the key concept of the counter
        return counter

    def get_min_time(counter, A, X):

        time = -1
        for key, value in enumerate(A):
            time += 1
            if counter[value] > 0:

                if value == X:
                     return time


    def solution(X,A):
        m = max(A)
        counter = FrogRiver.get_counter(A, m)
        min_time = FrogRiver.get_min_time(counter,A,X)
        return min_time

print(FrogRiver.solution(5,[1,3,1,4,2,3,5,4]))
print(FrogRiver.solution(1, [1]))
print(FrogRiver.solution(5, [3]))