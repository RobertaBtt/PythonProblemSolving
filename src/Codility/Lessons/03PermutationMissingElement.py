__author__ = 'RobertaBtt'


class PermMissingElem:

    def solution(A):

        n = len(A)+1
        result = n * (n + 1)//2

        return result - sum(A)


print(PermMissingElem.solution([1,2,4,5,6,7,8]))
print(PermMissingElem.solution([2,3,1,5]))
