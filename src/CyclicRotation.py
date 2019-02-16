__author__ = 'roby'


class CyclicRotation:

    def solution(A, K):
        num = 7
        mylist = [num for num in range(100)]
        print(mylist)

        new_list = []
        reverse_index = 0
        size = len(A)
        if K > 0:
            for index in range(K):
                new_list.append(A[-K + reverse_index])
                reverse_index +=1

            new_list.extend(A[0:K-1])


        return new_list


print (CyclicRotation.solution([3, 8, 9, 7, 6], 3))
print (CyclicRotation.solution([1, 2, 3, 4], 4))
