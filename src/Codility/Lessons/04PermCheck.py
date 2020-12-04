__author__ = 'RobertaBtt'

import functools

import math

class PermCheck:

    #Detected time complexity: O(N) or O(N * log(N))
    def solutionRoby(A):
        lenA = len(A)
        if 1 <= lenA <= 100000:
            setA = set(A)
            if len(setA) != lenA:
                return 0
            sumGauss = (lenA * (lenA + 1)) // 2
        sumA = sum(A)
        if sumGauss != sumA:
            return 0
        return 1


print(PermCheck.solutionRoby([1,2,3,1,1,1,1,1,1,1,1,1]))
print(PermCheck.solutionRoby([1,2,3]))
print(PermCheck.solutionRoby([4,1,3,2]))
print(PermCheck.solutionRoby([4,1,3]))
print(PermCheck.solutionRoby([1, 4, 1])) # Test case antiSum2

# Test case: extreme_values:  all the same values, N = ~100,000