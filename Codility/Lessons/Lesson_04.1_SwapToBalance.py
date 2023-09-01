__author__ = 'RobertaBtt'

'''You have an inger m    

1<= m<= 1000000
array A
array B

The goal is to check whether there is a swap operation which can be performed 
on these arrays in such a way that the sum of elements
in array A equals the sum of elements in array B after the swap.

This approach calculates the sum of elements at the beginning, 
and check only how the totals change during the swap operation
'''


class SwapToBalance:

    #Complexity O(n*n)
    def slow_solution(A,B,m):

        n = len(A)
        sumA = sum(A)
        sumB = sum(B)

        for a in range(n):
            for b in range(n):
                diff_AB = B[b] - A[a]
                sumA += diff_AB #I add the difference to A
                sumB -= diff_AB #I substract the difference to B
                if sumA == sumB:
                    return True
                #Else we are here, and we restore the sum for both
                sumA -= diff_AB #RESTORING A
                sumB += diff_AB #RESTORING B

        return False


print(SwapToBalance.slow_solution([1,3,4,5,2,5],[1,5,9,5,2,1],6))

