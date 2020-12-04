__author__ = 'RobertaBtt'
import collections


class FindMissingElement:

    def get_counter(A):

        n = max(A)

        counter = [0] * (n-1) #Creates array of m+1 elements, that is the same as n
        for k in range(n+1):
            counter[A[k]] += 1  # This is the key concept of the counter
        return counter


    def solution(A):

        if max(A)<0:
            return 1
        counter = FindMissingElement.get_counter(A)
        zippo = ''.join(map(str, counter))

        result = zippo.find('0', 1)
        return result
        # A = set(A)
        # n = len(A)+1
        # result = n * (n +1)//2
        #
        # if sum(A) <=0: return 1
        # return result - sum(A)


print(FindMissingElement.solution([1,2,3,5,6,7,8]))
print(FindMissingElement.solution([1,2,3])) #Expected 4
print(FindMissingElement.solution([1, 3, 6, 4, 1, 2])) #expected 5
print(FindMissingElement.solution([-1, -3])) #Expected 1
#print(FindMissingElement.solution([4, 5, 6, 2])) #Expected 1
#print(FindMissingElement.solution([0]))'''
