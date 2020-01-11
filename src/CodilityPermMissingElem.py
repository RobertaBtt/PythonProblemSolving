__author__ = 'RobertaBtt'


class PermMissingElem:

    def solution(A):

        n = len(A)+1
        result = n * (n + 1)//2

        return result - sum(A)


print(PermMissingElem.solution([1,2,3,5,6,7,8,4]))
