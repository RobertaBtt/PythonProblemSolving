__author__ = 'RobertaBtt'

'''
You have an inger m    

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

    #This is an array of counters.
    #Each number can be counted in the array using the index.
    # So for example, if in the index 2 we have "4",
    # it means that we have 4 occurrences of the value 2
    # [2,0,1,0,2,1] --> 2 occurrences of the number 0, 1 occurrence of the number 2 etc etc

    def get_counter(A, m):
        n = len(A)
        counter = [0] * (m + 1) #Creates array of m+1 elements, that is the same as n
        for k in range(n):
            counter[A[k]] += 1  # This is the key concept of the counter
        return counter

    #Complexity O(n+m)
    # Best approach
    # - Count elemtents of A and B
    # - Get the difference between them
    # - For every element in B we assume that we swap it with some element in A
    # - The difference d tells us the value from the array A that we are interested in swapping,
    # because only one value will cause the two totals to be equals.
    # The occurrence of this value can be found in constant time
    def fast_solution(A, B, m):
        n = len(A)
        sum_a = sum(A)
        sum_b = sum(B)
        d = sum_b - sum_a

        if d%2 == 1:
            return False

        d //= 2

        counter = SwapToBalance.get_counter(A, m)
        for i in range(n):
            # Poossible to swap and balance the two arrays ?
            if 0 <= B[i] -d and B[i] -d <= m and counter[B[i] -d] >0:
                return True
        return False

print(SwapToBalance.fast_solution([1,3,4,5,2],[1,5,4,5,2],5))
