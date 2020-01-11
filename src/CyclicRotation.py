__author__ = 'RobertaBtt'


class CyclicRotation:

    def solution(A, K):

        new_list = []
        reverse_index = 0

        if K > 0:
            for index in range(K):
                new_list.append(A[-K + reverse_index])
                reverse_index +=1

            new_list.extend(A[0:K-1])


        return new_list


print (CyclicRotation.solution([3, 8, 9, 7, 6], 8))
print (CyclicRotation.solution([1, 2, 3, 4], 4))
