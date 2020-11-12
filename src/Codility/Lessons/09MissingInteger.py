__author__ = 'RobertaBtt'


class FindMissingElement:

    def solution(A):

        A = set(A)
        n = len(A)+1
        result = n * (n + 1)//2

        if sum(A) <0: return 1
        return result - sum(A)


#print(PermMissingElem.solution([1,2,5,6,7,8]))
#print(FindMissingElement.solution([1, 3, 6, 4, 1, 2]))
print(FindMissingElement.solution([-1, -3]))
